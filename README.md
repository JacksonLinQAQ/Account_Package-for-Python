# Account_Package-for-Python

It is a package can code a simple account system in Python.

Step-1:
  Put the account package and your main project into a same folder.

Step-2:
  Import the account package using code: ``from account.account import *`` to your main project.
  
Step-3:
  Now you can code a simple account system:
```  
from account.account import* # import account package
state = get_config("account_state") # get the account_state (if the username is none, the state is `false`, that mean user haven't created account yet, else                                                                the state is true, that mean user have created account)
if state == "false": # if the state is false(User haven't created account yet)
    print("SIGNUP:")
    result = signup(input("username:"), input("password:")) # get username and password then run signup process get the result put it to variable: `result` 
    print(result)
elif state == "true": # if the state is true(User have created account)
    print("LOGIN:")
    result = login(input("username:"), input("password:")) # get username and password then run login process get the result put it to variable: `result` 
    print(result)
```
