import psycopg2
from db_config import get_db_info

filename='db_info.ini'
section='postgres-sample-db'
db_info = get_db_info(filename,section)

try:
    with psycopg2.connect(**db_info) as db_connection:
        print("Успешно подключено к базе данных.")
         
        with db_connection.cursor() as db_cursor:
            n = int(input("Введите номер заказа: "))
            db_cursor.execute('SELECT * FROM kupiflakon WHERE number = %s;', (n,))
            print(db_cursor.fetchone())
#except OperationalError:
#    print("Ошибка подключения к базе данных :/")
except (ValueError, NameError, TypeError):
    print("Ошибка ввода данных")
#except NameError:
#    print("Неверный ввод")

finally:
    if db_connection:
        db_connection.close()
        print("Соединение с PostgreSQL закрыто.")
