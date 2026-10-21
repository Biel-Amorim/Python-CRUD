from database import conec, close_conec

"""
CRUD
- C - CREATE
- R - READ
- U - UPDATE
- D - DELETE
"""

def main():
    connection =  conec()
    cursor = connection.cursor()

    # C reate
    def create(nm_user, login_user, pwd_user):
        cmd_insert = """
        INSERT INTO users(
        nm_user, login_user, pwd_user)
        VALUES(%s, %s, %s)"""
        values = (nm_user, login_user, pwd_user)
        cursor.execute(cmd_insert, values)
        connection.commit()
        print("Cara é pra funcionar")

    # R ead
    def read(columns, table, id): # for read ID
        cmd_read = """
        SELECT {0}
        FROM {1}
        WHERE id_user={2}"""
        for i in cursor.execute(cmd_read.format(columns, table, id)):
            print(i)

        
    # U pdate 
    def update(nm_user, login_user, id): # is acording for user's id
        cmd_update = """
        UPDATE users 
        SET nm_user = '{0}',
            login_user = '{1}'
        WHERE id_user = {2}""" 
        cursor.execute(cmd_update.format(nm_user, login_user, id)) # remenber, use '' simple quotes for indicate string, no tables
        connection.commit()
        print("atualizdo com sucesso")



    # D elete
    def delete(id):
        cmd_delete = """
        DELETE FROM users
        WHERE IF EXISTid_user = {0}
        """
        try:
            cursor.execute(cmd_delete.format(id))
            connection.commit()
            print("USUÁRIO DELETADO")
        except:
            print("este usuário não existe")


    # read("*", "users", "1")
    # update("Gabiruses", "GABIRU_MASTER", "1")
    # read("*", "users", "1")
    delete(5)
    delete(5)
    # update("Gabiruses", "GABIRU_MASTER", "5")

    # read("*", "users", "5")



if __name__ == "__main__":
    close_conec(main())