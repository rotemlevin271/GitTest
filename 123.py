import pymysql

DB_HOST = ""
DB_PASSWORD = ""
DB_PORT = ""
DB_USER = ""
DB_NAME = ""


def insert_user_to_db(cursor, user_id, user_name):
    query = 'INSERT INTO USERS (user_id, user_name) VALUES (%s, %s)'
    cursor.execute(query, (user_id, user_name))
    output = cursor.fetchall()

    return output

if _name_ == '_main_':
    conn = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME,
    )
    cursor = conn.cursor()
    cursor.autocommit(True)

    result = insert_user_to_db(cursor=cursor, user_id=1, user_name="ishai")


    # שורה שאני שומרת למקרה ואצטרך, לא ידעתי מה היא עודה ואם אני צריכה אותה

    user = next((u for u in users if u['id'] == user_id), None)