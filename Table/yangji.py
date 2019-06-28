# _*_coding: utf-8 _*_

import pymysql
import pandas as pd
from django.http import JsonResponse
from sqlalchemy import create_engine


class TableOperation:
    def __init__(self, user='root', password='123456', host='localhost', port=3306, db='yangji_0626'):
        """
        :param user: 用户名
        :param password: 密码
        :param host: 主机IP
        :param port: 端口
        :param db:数据库名
        :return:
        """
        self.user = user
        self.password = password
        self.host = host
        self.db = db
        self.port = port
        self.insert_id = None

    def get_py_connect(self):
        conn = pymysql.connect(user=self.user, password=self.password, host=self.host, db=self.db)
        try:
            conn.ping(True)
        except pymysql.Error:
            ret = {
                'code': 1,
                'msg': '数据库连接失败'}
            return JsonResponse(ret)
        return conn

    def get_sql_connect(self):
        db_info = {'user': self.user, 'password': self.password, 'host': self.host, 'port': self.port, 'db': self.db}
        engine = create_engine("mysql+pymysql://{user}:{password}@{host}:{port}/{db}".format(**db_info))
        connect = engine.connect()
        return connect

    # 查询一条数据
    def query_one_data(self, conn, sql):
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
        return data

    # 生成字典 --- {1: '上下挂', 2: '上下挂', 3: '上下挂'}
    def query_tuple_table(self, conn, sql):
        cursor = conn.cursor()
        cursor.execute(sql)
        data_tuple = cursor.fetchall()
        return data_tuple

    # 生成列表 --- [{'no':1, 'name': '上下挂'}，{'no':2, 'name': '上下挂'}]
    def query_table(self, conn, sql):
        """
        查询指定表的数据
        :param sql: 查询语句
        :return:
        """
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        try:
            cursor.execute(sql)
            conn.commit()
            data = cursor.fetchall()
            return data
        except:
            conn.rollback()


    def append_data(self, conn, sql):
        """
        追加数据
        :param sql: 追加数据语句
        :return:
        """
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()

    def replace_not_reset(self, connect, table_name, data_list):
        df = pd.DataFrame(data_list)
        df.to_sql(table_name, con=connect, if_exists='replace', index_label='id')

    # 替换表
    def replace_table(self, connect, table_name, data_list, sort_columns, dtype_dict=None):
        """
        替换表
        :param table_name: 表名
        :param data_list: 插入的数据 [{}]
        :param sort_columns:  按照某列排序
        :param dtype_dict:  定制 生成字段类型
        :return:
        """
        # 将插入的数据转成df
        df = pd.DataFrame(data_list)
        # 按照某一列排序
        df.sort_values(by=sort_columns, inplace=True)
        if not dtype_dict:
            #重置索引
            df.reset_index(inplace=True)
            assert df['slot'].unique().shape[0] == df.shape[0]
            # 替换原表的数据
            df.to_sql(table_name, con=connect, if_exists='replace', index_label='id')

        else:
            # 删除index列
            df.drop(columns='index', inplace=True)
            # 再添加一列index
            df['index'] = range(1, len(df) + 1)
            # 替换原表的数据
            df.to_sql(table_name, con=connect, if_exists='replace', dtype=dtype_dict, index=False)

    def insert_data(self, connect, table_name, query_sql, insert_list, sort_columns, dtype_dict, have_id=False):
        """
        在表之间插入一条数据，并且重新排序

        :param table_name: 表名
        :param query_sql: 查询表数据
        :param insert_list: 插入的数据  [{}]
        :param sort_columns:  按照某列排序
        :param dtype_dict:  定制 生成字段类型
        :return:
        """
        # 读取表中数据，转成df
        df = pd.read_sql(query_sql, connect)
        # 将插入的数据转成df
        insert_df = pd.DataFrame(insert_list)

        # 插入的位置
        no = insert_list[0].get("index")
        df1 = df.loc[:no - 1]
        df2 = df.loc[no:]
        #合并
        new_df = pd.concat([df1, insert_df, df2], ignore_index=True)

        # 合并
        # new_df = pd.concat([df, insert_df])
        # 按照某一列排序
        # new_df.sort_values(by=sort_columns, inplace=True)


        # 重置排序
        new_df[sort_columns] = range(1, len(new_df)+1)
        # 替换原表的数据
        if have_id:
            new_df.to_sql(table_name, con=connect, if_exists='replace', dtype=dtype_dict, index_label='id')
        else:
            new_df.to_sql(table_name, con=connect, if_exists='replace', dtype=dtype_dict, index=False)


    def update_data(self, conn, sql):
        """
        更新数据
        :param conn:
        :param sql:
        :return:
        """
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()

    def delete_data(self, conn, sql):
        """
        删除某一条数据
        :param sql: 删除语句
        :return:
        """
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()

    def delete_and_sort(self, connect, table_name, query_sql, del_values, sort_columns, dtype_dict):
        """
        在表之间插入一条数据，并且重新排序

        :param table_name: 表名
        :param query_sql: 查询表数据
        :param del_values: 删除行中的某个特定数值
        :param sort_columns:  按照某列排序
        :param dtype_dict:  定制 生成字段类型
        :return:
        """
        # 读取表中数据，转成df
        df = pd.read_sql(query_sql, connect)
        # # 删除指定的行索引
        # df.drop(index=del_index, inplace=True)
        # 删除某个特定数值
        df_cp = df.copy()
        df_cp = df_cp[~df_cp[sort_columns].isin([del_values])]
        # 重置排序
        df_cp[sort_columns] = range(1, len(df_cp)+1)
        # 替换原表的数据
        df_cp.to_sql(table_name, con=connect, if_exists='replace', dtype=dtype_dict, index=False)

    def copy_table(self, connect, new_table_name, query_sql, dtype_dict):
        """
        复制表
        """
        df = pd.read_sql(query_sql, connect)
        df.to_sql(new_table_name, con=connect, if_exists='replace', dtype=dtype_dict, index=False)







