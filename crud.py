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
        VALUES(%s, %s, %s)
        """

        cmd_id = """
        SELECT *
        FROM users 
        WHERE login_user = %s
        """

        values = (nm_user, login_user, pwd_user)
        connection.execute(cmd_insert, values)
        connection.commit()
        defined_id = connection.execute(cmd_id, (login_user,)).fetchone()
        print(defined_id)
        print("Cara é pra funcionar")

    # R ead
    def read(columns, table, id): # for read ID
        cmd_read = f"""
        SELECT {columns}
        FROM {table}
        WHERE id_user= %s
        """

        row = connection.execute(cmd_read,(id,)).fetchall()
        for i in row:
            print(i)

        
    # U pdate 
    def update(nm_user, login_user, id): # is acording for user's id
        cmd_update = """
        UPDATE users 
        SET nm_user = %s,
        login_user = %s
        WHERE id_user = %s
        """

        cmd_condition = """SELECT EXISTS(
        SELECT * FROM users
        WHERE id_user = %s)
        """
        veryfing = connection.execute(cmd_condition, (id,)).fetchone()
        if veryfing == (True,):
            connection.execute(cmd_update, (nm_user, login_user, id)) # remenber, use '' simple quotes for indicate string, no tables
            connection.commit()
            print("atualizdo com sucesso")
        else:
            print(f"Vish man nem tem usuario com esse ID {id}")


    # D elete
    def delete(id):
        cmd_delete = """
        DELETE FROM users
        WHERE id_user = %s
        """

        cmd_condition = """SELECT EXISTS(
        SELECT * FROM users
        WHERE id_user = %s)
        """
        veryfing = connection.execute(cmd_condition, (id,)).fetchone()
        
        if veryfing == (True,):
            connection.execute(cmd_delete, (id,))
            connection.commit()
            print("USUÁRIO DELETADO")
        else:
            print(f"Vish man nem tem usuario com esse ID {id}")



    # create("Gabriel", "gabiru_plus", "no_hash_test")
    # delete(10)
    update("G2_cabeludo", "A_VOLTA_DOS_Q_N_FORAM", 11)
    delete(11)

    close_conec(connection)


if __name__ == "__main__":
    main()