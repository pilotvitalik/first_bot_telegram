import sqlite3


def open_con():
    connection = sqlite3.connect("telegram_bot.db")
    db = connection.cursor()

    check_avaialabe_table = db.execute("SELECT name FROM sqlite_master")
    is_avaialabe_table = check_avaialabe_table.fetchone()

    if is_avaialabe_table is None:
        db.execute("CREATE TABLE user_id(user_id, first_name, last_name)")

    return db, connection


def insert_data(args):
    args[0].execute("INSERT INTO user_id VALUES (?, ?, ?)", [args[2]['id'], args[2]['first_name'], args[2]['last_name']])
    args[1].commit()


def is_data_in_stock(cursor, id_user):
    result = cursor.execute("SELECT user_id from user_id WHERE user_id=(?)", [id_user])
    return result.fetchone is None


def close_connect():
    db.close()
    connection.close()