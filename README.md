# Account_Package-for-Python

It is a package can code a simple account system in Python.

### Steps:

Step-1:
  Extract the account package.

Step-2:
  Put the account package and your main project into a same folder.

Step-3:
  Import the account package using code: ``from account.account import *`` to your main project.
  
Step-4:
  Now you can code a simple account system:
```  
from account.account import* # import account package
state = get_config("account_state") # get the account_state
# (if the username is none, the state is `false`, that mean user haven't created account yet, else the state is true, that mean user have created account)

if state == "false": # if the state is false(User haven't created account yet)
    print("SIGNUP:")
    result = signup(input("username:"), input("password:")) # get username and password then run signup process get the result put it to variable: `result` 
    print(result)
elif state == "true": # if the state is true(User have created account)
    print("LOGIN:")
    result = login(input("username:"), input("password:")) # get username and password then run login process get the result put it to variable: `result` 
    print(result)
```

### Package codes:

`recovery()`: Reset all settings to default

`login(username, password)`: Login with username and password and return a result

`signup(username, password)`: Signup with username and password and return a result

`get_config(src)`: Get config
- src: `all` / `account_state`
- `account_state`: 
-   output: `true`/`false`
-   `true`: User have created account
-   `false`: User haven't created account yet

`setting(login_true, login_false, signup_true)`: Change the result texts(use `None` to skip the blanks)
- (login_true, login_false, signup_true): result texts
- use `none` to skip the blanks if you don't want to change it
- login_true: if login success(correct username and password)
- login_false: if username or password wrong
- signup_true: if signup success
