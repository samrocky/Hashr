# Hasher
## How to use :
  copy Hash.py in your python3's libraries directory
### Linux path :
    /usr/lib/python3.6/
### Windows path :
    C:\Users\<username>\Appdata\local\programs\python3\

and then you can import " Hash " into your personal program
## For example :
    input>>> import Hash
    input>>> print(Hash.sha256("sam"))
    output>>> e96e02d8e47f2a7c03be5117b3ed175c52aa30fb22028cf9c96f261563577605
    input>>> print(Hash.md5("sam"))
    output>>> 332532dcfaa1cbf61e2a266bd723612c
  #### Or :
  
    input>>> from Hash import *
    input>>> print(sha256("sam"))
    output>>> e96e02d8e47f2a7c03be5117b3ed175c52aa30fb22028cf9c96f261563577605
    input>>> print(md5("sam"))
    output>>> 332532dcfaa1cbf61e2a266bd723612c
