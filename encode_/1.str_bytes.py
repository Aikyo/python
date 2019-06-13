import base64


msg = "i am kiko"

msg_encode = msg.encode()
#msg_encode_base64 = msg.encode(encoding="utf8")
print(msg_encode)
#print(msg_encode_base64)
print(type(msg_encode))

msg_encode_base64 = base64.b64encode(msg_encode)
print(msg_encode_base64)
msg_base64_encode = str(msg_encode_base64,'utf-8')

print(msg_base64_encode)
print(type(msg_encode_base64))
print("---------base64 decoder----------")

msg_decode = base64.b64decode(msg_base64_encode.encode('utf8'))
print(str(msg_decode,encoding='utf8'))



