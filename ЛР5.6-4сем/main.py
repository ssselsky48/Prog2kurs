import sqlite3
from decorator import logger

def connect_to_db(path_to_db: str) -> object:
    """
    Connect to sqlite database
    
    :return sqlite3.Connection
    """
    try:
      conn = sqlite3.connect(path_to_db)
      print("Успешное подключение к базе данных!")
    except sqlite3.Error:
      print("Ошибка подключения к базе данных")
      return
    return conn


@logger
def create_table(table_name, domens_lst, conn):
    if(not conn):
      print("Ошибка с подключением")
      return
    cursor = conn.cursor()
    
    try:
      cursor.execute("""SELECT count(*) FROM sqlite_master WHERE type='table' AND name=?""", (table_name,))
      result = cursor.fetchone()[0]
    except sqlite3.Error:
      print("Ошибка!")
      return 0
    if (not result):
      print("Таблица не существует")
      print("Создаю таблицу")
      try:
        cursor.execute(""" CREATE TABLE user (
          id INTEGER,
          height REAL,
          name TEXT,
          deleted BOOLEAN,
          created_at, DATETIME
        ); """)
        print("Таблица успешно создана!")
      except sqlite3.Error:
        print("Ошикба!")
        return
    else:
      print("Таблица уже существует")
      return

    conn.commit()
    cursor.close()


@logger
def insert_param_data(conn, values):
    # TODO: Реализовать тело функции
    # параметризованый запрос на добавление данных в таблицу user
    if(not conn):
      print("Ошибка с подключением")
      return None

    cursor = conn.cursor()
    try:
      cursor.executemany(""" INSERT INTO `user`(name, height) VALUES (?, ?); """, values)
      print("Данные успешно добавлены!")
    except sqlite3.Error:
      print("Ошибка!")
    
    conn.commit()
    cursor.close()


@logger
def show_all_from_user(conn):
  if(not conn):
      print("Ошибка с подключением")
      return None

  cursor = conn.cursor()
  res = cursor.execute(""" SELECT * FROM `user` """)

  for r in res:
    print(r)


@logger
def update_entry_in_user(conn, values):
  if(not conn):
      print("Ошибка с подключением")
      return None

  cursor = conn.cursor()
  try:
    cursor.execute(""" 
    UPDATE `user` 
    SET height = ?, name = ?, deleted = ?
    WHERE id = ?
    """, values)
    print("Данные успешно обновлены!")

  except sqlite3.Error:
    print("Ошибка!")

  conn.commit()
  cursor.close()


@logger
def delete_entry_from_user(conn, user_id):
  if(not conn):
      print("Ошибка с подключением")
      return 

  cursor = conn.cursor()
  try:
    cursor.execute(""" DELETE FROM `user` WHERE `id` = ? """, (user_id,))
    print("Запись успешно удалена!")

  except sqlite3.Error:
    print("Ошикба!")

  conn.commit()
  cursor.close()


if __name__ == "__main__":
  conn = connect_to_db("zhukov.db")
  # create_table("user", ["1", "2"], conn)
  # insert_param_data(conn, [('Dima', 1.60)])
  # show_all_from_user(conn)
  # update_entry_in_user(conn, (1.64, 'Dma', 0, 17))
  # delete_entry_from_user(conn, 17)
  show_all_from_user(conn)

  
