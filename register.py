from crud import *
import bcrypt


def verify_login(login):
    verify_existence = read('login_user', 'users', 'login_user', login)
    print(verify_existence)
    if verify_existence == []:
        print(f"RELAX, you can pass")
        return True
    else:
        print(f"You can't pass")
        return False


def hash_password(pwd):
    hashed_pwd = bcrypt.hashpw(pwd, bcrypt.gensalt())
    return hashed_pwd

def register(name, login, password):
    if verify_login(login):
        new_pwd = hash_password(password)
        create(name, login, new_pwd)

if __name__ == "__main__":
    password = bytes('legal_man', 'UTF-8')
    name_user = "Gabrielsin_Boleras"
    login_user = 'gabrielegal'
    register(name=name_user, login=login_user, password=password)