# Python_Account-Package
It is a package can code a simple account system in Python.

Step-1:
  Put the account package and your main project into a same folder.

Step-2:
  Enter ``from account.account import *`` in your main project.
  
Step-3:
  Now you can code a simple account system:
  
`from account.account import*`\n`state = get_config("account_state")`\n`if state == "false":`\n`    print("SIGNUP:")`\n`    result = signup(input("Username:")`\n` input("Password:"))`\n`    print(result)`\n`elif state == "true":`\n`    print("LOGIN:")`\n`    result = login(input("Username:")`\n`input("Password:"))`\n`    print(result)`
