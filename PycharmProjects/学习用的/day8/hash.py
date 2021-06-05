__author__ = "Alex Li"

import hashlib,os

m = hashlib.md5()
m.update(b"test")
m.update(b"http://p1.pstatp.com/origin/pgc-image/150c20a743d242c7a2b931e2d185e885")
print(m.hexdigest())
m2 = hashlib.md5()
m2.update(b"testabc")
print(m2.hexdigest())
print(os.getcwd())