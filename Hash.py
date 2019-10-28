"""
How to use :
copy this file in to your python3's libraries directory
Linux path :
Windows path :
and the you can import " Hash " into your personal prohram

For example :
input>>> import Hash
input>>> print(Hash.sha256("sam"))
output>>> e96e02d8e47f2a7c03be5117b3ed175c52aa30fb22028cf9c96f261563577605
input>>> print(Hash.md5("sam"))
output>>> 332532dcfaa1cbf61e2a266bd723612c

Or :
input>>> from Hash import *
input>>> print(sha256("sam"))
output>>> e96e02d8e47f2a7c03be5117b3ed175c52aa30fb22028cf9c96f261563577605
input>>> print(md5("sam"))
output>>> 332532dcfaa1cbf61e2a266bd723612c


        md5
        sha1
        sha224
        sha256
        sha384
        sha512


"""

import hashlib

def sha256(a):
    data = a
    m = hashlib.sha256();
    m.update(data.encode('utf-8'));
    finaly = m.hexdigest();
    return finaly

def md5(a):
    data = a
    m = hashlib.md5();
    m.update(data.encode('utf-8'));
    finaly = m.hexdigest();
    return finaly

def sha1(a):
    data = a
    m = hashlib.sha1();
    m.update(data.encode('utf-8'));
    finaly = m.hexdigest();
    return finaly

def sha224(a):
    data = a
    m = hashlib.sha1();
    m.update(data.encode('utf-8'));
    finaly = m.hexdigest();
    return finaly

def sha328(a):
    data = a
    m = hashlib.sha1();
    m.update(data.encode('utf-8'));
    finaly = m.hexdigest();
    return finaly


def sha512(a):
    data = a
    m = hashlib.sha1();
    m.update(data.encode('utf-8'));
    finaly = m.hexdigest();
    return finaly
