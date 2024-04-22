import re

def sign_in(in_usr, in_pwd):
    if isValid_email(in_usr):
        with open("user.json", "r") as f:
            if in_usr in f:
                if in_pwd == f[in_usr]["password"]:
                    return True
                else:
                    return False
            else:
                return False
    else:
        return False

def sign_out():
    return True

def register():
    with open("user.json", "a") as f:
        usr = input()
        usr_name = input()
        pwd = input()
        word = {usr : {"username" : usr_name, "password" : pwd, "identity" : "user"}}
        if usr not in f:
            f.write(word)
            return True
        return False

def isValid_email(usr):
    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-z]{2,3}|[0-9]{1,3})(\\]?)$", usr) != None:
        return True
    else:
        return False