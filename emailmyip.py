from urllib import request

req = request.Request("https://checkip.amazonaws.com", data=None)
res = request.urlopen(req, timeout=5)

print(res.read().decode().strip())
