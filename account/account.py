import account
import json

def setting(lt, lf, st): # login_true, login_false, signup_true
    with open("account\config\config.json", mode="r") as file:
        user = json.load(file)
    if lt != "none":
        user["login_true"] = lt
    if lf != "none":
        user["login_false"] = lf
    if st != "none":
        user["signup_true"] = st
    with open("account\config\config.json", mode="w") as file:
        json.dump(user, file)         

def signup(un, pw):
    with open("account\config\config.json", mode="r") as file:
        user = json.load(file)
    user["username"] = un
    user["password"] = pw
    with open("account\config\config.json", mode="w") as file:
        json.dump(user, file)
    return(user["signup_true"])

def recovery():
    user = {"username": "none", "password": "none", "login_true":"Login Success", "login_false":"Wrong Username or Password", "signup_true":"Signup Success"}
    with open("account\config\config.json", mode="w") as file:
        json.dump(user, file)

def login(un, pw):
    with open("account\config\config.json", mode="r") as file:
        user = json.load(file)
    un_1 = user["username"]
    pw_1 = user["password"]
    if un == un_1 and pw == pw_1:
        return(user["login_true"])
    else:
        return(user["login_false"])

def get_config(type):
    with open("account\config\config.json", mode="r") as file:
        if type == "all":
            file_get = json.load(file)
            return(file_get)
        elif type == "account_state":
            file_get = json.load(file)
            if file_get["username"] != "none":
                return("true")
            else:
                return("false")

