import json

a = [1,23,4,5]

#s = json.dump({'a':'herman'})
d={'谦谦':{'sex':'男','addr':'北京','age':34},'千千':{ 'sex':'女','addr':'北京', 'age':34},}
print(json.dumps(d,ensure_ascii=False,indent=4))
#字典转成json,字典转换成字符串 加上ensure_ascii=False以后，可以识别中文， indent=4是间隔4个空格显示
#print(s)





