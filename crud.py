from database import conec, close_conec

"""
CRUD
- C - CREATE
- R - READ
- U - UPDATE
- D - DELETE
"""


# cursor = connection.cursor() apenas para onde for mais fácil, para não causar cursor leak
# use connection.execute() método do psycopg para fazer execução de código sem risco de cursor leak

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
    connection =  conec()
    connection.execute(cmd_insert, values)
    connection.commit()
    defined_id = connection.execute(cmd_id, (login_user,)).fetchone()
    close_conec(connection) # connection closed
    
    print(defined_id)


# R ead
def read(columns, table, condition, value): # for read ID

    cmd_read = f"""
    SELECT {columns}
    FROM {table}
    WHERE {condition}= %s
    """

    connection =  conec()

    row = connection.execute(cmd_read,(value,)).fetchall()
    close_conec(connection)
    return row

    
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

    connection =  conec()
    veryfing = connection.execute(cmd_condition, (id,)).fetchone()

    if veryfing == (True,):
        connection.execute(cmd_update, (nm_user, login_user, id)) # remenber, use '' simple quotes for indicate string, no tables
        connection.commit()
        print("atualizdo com sucesso")
    else:
        print(f"Vish man nem tem usuario com esse ID {id}")
    close_conec(connection)
    


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

    connection =  conec()
    veryfing = connection.execute(cmd_condition, (id,)).fetchone()
    
    if veryfing == (True,):
        connection.execute(cmd_delete, (id,))
        connection.commit()
        print("USUÁRIO DELETADO")
    else:
        print(f"Vish man nem tem usuario com esse ID {id}")
    close_conec(connection)



# create("Gabriel", "gabiru_plus", "no_hash_test")
# delete(10)
# update("G2_cabeludo", "A_VOLTA_DOS_Q_N_FORAM", 11)
# delete(11)


if __name__ == "__main__":
    # testing

    # create OK
    # read OK
    # update OK
    # delete OK
    ...