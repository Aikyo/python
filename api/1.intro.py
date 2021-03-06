from flask import Flask,jsonfy,request
data = {'huhy':{'age':24,'sex':'女'},
        'liuer':{'age':12,'sex':'男'}
        }
app = Flask(__name__)#创建一个服务，赋值给APP

@app.route('/get_user',methods=['get'])#指定接口访问的路径，支持什么请求方式get，post
#讲的是封装成一种静态的接口，无任何参数传入
def get_user():#-----这里的函数名称可以任意取
    return  jsonify(data)#把字典转成json串返回

@app.route('/get_user_byname',methods=['get'])
def get_user():
    username = request.form.get('username')#获取接口请求中form-data的username参数传入的值
    if username in data:#判断请求传入的参数是否在字典里
        return jsonify(data[username])
#如果在的话，则返回data对应key的值转成的json串信息
    else:
        return jsonify(err[username])
#如果不在的话，返回err对应key的value转成的json串信息


app.run(host='0.0.0.0',port=8802,debug=True)
#这个host：windows就一个网卡，可以不写，而liux有多个网卡，写成0:0:0可以接受任意网卡信息,
#通过访问127.0.0.1:8802/get_user，可返回data信息
#debug:调试的时候，可以指定debug=true；如果是提供接口给他人使用的时候，debug要去掉