
import requests

print('获取格言信息（双语）...')
resp = requests.get('http://open.iciba.com/dsapi')
if resp.status_code == 200 :
    content_dict = resp.json()
    content = content_dict.get('content')
    note = content_dict.get('note')
    print('{}   {}'.format(content, note))

