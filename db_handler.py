import dbconnection as DB


def log_in(log, passw, signal):
    conn = DB.dbconnection.getconn()
    cursor = conn.cursor()

    # Проверяем есть ли такой пользователь
    cursor.execute(f"SELECT * FROM users WHERE login='{log}'")
    value = cursor.fetchall()

    if value == [] or value[0][2] != passw:
        signal.emit('!')



def register(log_2, passw_2, sur, na, pat, id_ins, id_pos, signal):
    conn = DB.dbconnection.getconn()
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM users WHERE login='{log_2}')")
    value = cursor.fetchall()

    if value != []:
        signal.emit('Такой ник уже используется!')

    elif value == []:
        print(log_2)
        cursor.execute(f"INSERT INTO users (login, password, surname, name, patronymic, ID_POSITION, ID_INSTITUTE) "
                       f"VALUES ('{log_2}','{passw_2}','{sur}','{na}','{pat}','{id_ins},'{id_pos}')")
        signal.emit('Вы успешно зарегистрированы!')
