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
    # if i == (login,):
    #     return f'The name {login} always exist'
    # else:
    #     return f'you can pass'

def hash_password():
    ...

def register():
    ...

if __name__ == "__main__":
    password = bytes('legal_man', 'UTF-8')
    name_user = "Gabrielsin_Boleras"
    login_user = 'gabriel'
    verify_login(login_user)
    hash_password()
    register()