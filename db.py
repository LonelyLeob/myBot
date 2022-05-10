import sqlite3 as sql
from datetime import datetime as dt
import string, random

conn = sql.connect('tgdb.db')
curs = conn.cursor()

def add_db():
    """Create tables"""
    if conn:
        print('БД и курсор успешно включены')
    conn.executescript(
        'CREATE TABLE IF NOT EXISTS users(\n'
                        'us_id INTEGER PRIMARY KEY,\n'
                        'name VARCHAR(100),\n'
                        'pwd VARCHAR(8),\n'
                        'regdate DATETIME,\n'
                        'permission VARCHAR(50) references permissions(level));\n'

        'CREATE TABLE IF NOT EXISTS permissions(\n'
                        'level TEXT PRIMARY KEY)\n;'
        )
    conn.commit()

def gen_pwd():
    """Generate new pwd for user"""
    lenght = 8
    allowchars = string.ascii_letters + string.digits
    new_pwd = ''.join(random.choice(allowchars) for _ in range(lenght))
    return str(new_pwd)


def add_user(msg_id, name, pwd):
    """Adding user"""
    query = "INSERT into users values (?, ?, ?, ?, ?, ?, ?, ?)"
    row = (msg_id,
        name,
        pwd,
        dt.now(),
        False,
        'Гость',
        None,
        None
        )

    curs.execute(query, row)
    conn.commit()


def is_opened(func):
    """Check for userstate for using main commands"""
    async def wrapper(message):
        query = 'select is_opened from users where us_id = ?'
        data = (message['from']['id'],)

        curs.execute(query, data)
        conn.commit()

        user_state = curs.fetchone()
        if False == user_state[0]:
            return await message.reply('Вы не вошли в систему!\nИспользуйте /auth', reply=False)
        else:
            None
        return await func(message)

    return wrapper


def session_state(stt, us_id):
    """State and update user session"""
    upd_state = "update users set is_opened = ? where us_id = ?"
    data = (stt,
            us_id,)
    
    curs.execute(upd_state, data)
    conn.commit()


def get_auth(us_id, msg):
    """Auth by unique password"""
    query = 'select pwd from users where us_id = ?'
    data = (us_id,)

    curs.execute(query, data)
    conn.commit()

    user_pwd = curs.fetchone()
    if msg == user_pwd[0]:
        session_state(True, us_id)
        return True
    else: 
        return False

def get_user(us_id):
    """Get user information"""
    query = 'select * from users where us_id = ?'
    data = (us_id,)

    curs.execute(query, data)
    conn.commit()

    user_info = curs.fetchone()
    return user_info
