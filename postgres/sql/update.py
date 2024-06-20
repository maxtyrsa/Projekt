import psycopg2
from db_config import get_db_info
import pprint

filename='db_info.ini'
section='postgres-sample-db'
db_info = get_db_info(filename,section)

try:
    with psycopg2.connect(**db_info) as db_connection:
        print("Успешно подключено к базе данных.")

        with db_connection.cursor() as db_cursor:
            db_cursor.execute("SELECT * FROM kupiflakon WHERE date = CURRENT_DATE;")
            x = db_cursor.fetchall()
            print(str(x).replace('), (', '\n'))
        # Insert one update
            i = int(input("Введите id: "))
            a = int(input("Введите новое количество: "))
            insert_record = 'UPDATE kupiflakon SET place = %s WHERE date = CURRENT_DATE and id = %s;'
            insert_value = (a, i)
            db_cursor.execute(insert_record, insert_value)
#except OperationalError:
#    print("Ошибка подключения к базе данных :/")

except (ValueError, NameError, TypeError):
    print("Ошибка ввода данных")

finally:
    if db_connection:
        db_connection.close()
        print("Соединение с PostgreSQL закрыто.")
