# классы - виды запросов (select, update, insert)

# класс - структура/сущность со структурой, которую реализует какой-то конкретный объект
# например пользователь Elena или Irina

class EmptyFileException(Exception):
  def __init__(self, text):
    self.text = text

class User():
    def __init__(self, name, height):

        if (self.__check_name(name) and self.__check_height(height)):
          self.__name = name
          self.__height = height
        else:
          raise ValueError("Имя должно содержать не менее 3 букв, а рост должен быть числом")


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, name):
        if (self.__check_name(name) == 1):
          self.__name = name
        else:
          raise ValueError
          

    @name.deleter
    def name(self):
        pass


    @property
    def height(self):
        return self.__height


    def __check_height(self, height):
        try:
          float(height)
        except ValueError:
          return False
        else:
          return True


    def __check_name(self, name):
        if (len(name) < 3):
          return False
        else:
          return True



def singleton(cls):
    import functools

    instance = None
    
    @functools.wraps(cls)
    def inner(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs) # == Connection(dbfile)
        return instance

    return inner

@singleton
class Connection():
    """

    """
    def __init__(self, dbfile):
        import os
        try:
          if(not os.path.getsize(dbfile)):
            raise EmptyFileException('Файл пустой!')
        except OSError:
          print('Файл не найден')
          import sys
          sys.exit(1)
          
        self.__filename = dbfile
        self.__conn = None
        self.__cursor = None
        # проверка наличия файла с БД и выбрасываем исключение, если файла нет или он пустой

    def connect(self):
        import sqlite3
        self.__conn = sqlite3.connect(self.__filename)
        self.__cursor = self.__conn.cursor()
        return self.__conn

    @property
    def conn(self):
        return self.__conn

    @property
    def cursor(self):
        return self.__cursor


#someUser = User('Naaa', '1.11')
#print(someUser.name)
#print(someUser.height)

c = Connection('z.db')
c.connect() # 
c.conn # используем getter
#c1 = Connection('zhukov.db')

#print(id(c1), id(c))

#print(type(c))



# # Insert a row of data
# sql = "INSERT INTO user(name, height) VALUES(?, ?)"
# names = [('Elena', 1.69), ('Irina', 1.80)]

# conn.executemany(sql, names)

# # Save (commit) the changes
# # conn.commit()

# # READ aka SELECT
#crud_read_str = "SELECT * FROM user"
# "SELECT * FROM user WHERE name='Konstantin'"
#curs = c.cursor
#crud_res = curs.execute(crud_read_str)

#for r in crud_res:
#    print(r)

# # We can also close the connection if we are done with it.
# # Just be sure any changes have been committed or they will be lost.
# conn.close()
