import base64

encoded= "COOKIE URL-DECODED"


decoded = base64.b64decode(encoded).decode()
print(decoded)#REVEALS THE FLAG
