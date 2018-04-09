from hashlib import md5
#加密
def gethash(pwd):
    p = md5()
    p.update(pwd.decode('utf-8'))
    return p.hexdigest()