# Account_Package-for-Python

It is a package can code a simple account system in Python.

Step-1:
  Put the account package and your main project into a same folder.

Step-2:
  Import the account package using code: ``from account.account import *`` to your main project.
  
Step-3:
  Now you can code a simple account system:
```  
from account.account import*
state = get_config("account_state")
if state == "false":
    print("SIGNUP:")
    result = signup(input("username:"), input("password:"))
    print(result)
elif state == "true":
    print("LOGIN:")
    result = login(input("username:"), input("password:"))
    print(result)
```
