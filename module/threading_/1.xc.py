
import gevent
import requests


def f(url):
    print('GET: %s' % url)
    html = requests.get(url).text
    print(url, len(html))


gevent.joinall([
    gevent.spawn(f, 'http://i.maxthon.cn/'),  # 先执行这个函数，发送请求,等待的时候发送第二个请求
    gevent.spawn(f, 'http://www.jianshu.com/u/3cfeb3395a95'),
    gevent.spawn(f, 'http://edu.51cto.com/?jydh'),
])
