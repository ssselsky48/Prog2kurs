from time import gmtime, strftime

def logger(func):
  try:
    file = open("logs.txt", 'a')
  except PermissionError:
    print("Недостаточно прав на запись файла")

    import os
    import stat

    try:
        os.chmod('logs.txt', stat.S_IRWXU)
        print("Смена прав произошла успешно")
    except OSError as e:
        print(f'Попытка смены прав не удалась: {e}')

  file.write("-----------------------------------------------------\n")
  file.write("Function name: " + func.__name__ + "\n")
  file.write("Values: " + ", ".join(func.__code__.co_varnames) + "\n")
  file.write("Time of start: " + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "\n")
  file.close()

  return func