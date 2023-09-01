import psycopg2
import datetime
import random

#from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
from psycopg2.extras import NamedTupleCursor

import config

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def NOW():
    dt = datetime.datetime.now()
    return dt

try:
    connection = psycopg2.connect(user=config.DB_USER,
                                  password=config.DB_PASS,
                                  host=config.DB_HOST,
                                  port=config.DB_PORT)
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    cursor.execute("""CREATE DATABASE network_bot""")
    print('База данных "network_bot" создана')
    cursor.close()
    connection.close()
except Exception as e:
    pass


def add_user(chat_id, username):
    connect = psycopg2.connect(user=config.DB_USER,
                                  password=config.DB_PASS,
                                  host=config.DB_HOST,
                                  port=config.DB_PORT,
                                  database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = connect.cursor(cursor_factory=NamedTupleCursor)
    cursor.execute(f"""INSERT INTO users (chat_id, username, state_conf) VALUES
                                         ({chat_id}, '{username}', {False})""")

    connect.commit()
    connect.close()

def get_all_chat_id():
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor()
    cursor.execute("""SELECT chat_id FROM users""")
    chat_ids = cursor.fetchall()
    connect.commit()
    connect.close()
    return chat_ids


def get_state_conf(chat_id):
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor()
    cursor.execute(f"""SELECT state_conf FROM users WHERE chat_id = {chat_id}""")
    state_conf = cursor.fetchone()[0]
    connect.commit()
    connect.close()
    return state_conf


def set_state_conf(chat_id):
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor()
    cursor.execute(f"""UPDATE users SET state_conf = {True} WHERE chat_id = {chat_id}""")
    connect.commit()
    connect.close()


def set_name(chat_id, name):
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor()
    cursor.execute(f"""UPDATE users SET name = '{name}' WHERE chat_id = {chat_id}""")
    connect.commit()
    connect.close()


def set_prof(chat_id, prof):
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor()
    cursor.execute(f"""UPDATE users SET prof = '{prof}' WHERE chat_id = {chat_id}""")
    connect.commit()
    connect.close()


def set_company(chat_id, company):
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor()
    cursor.execute(f"""UPDATE users SET company = '{company}' WHERE chat_id = {chat_id}""")
    connect.commit()
    connect.close()

def set_phone(chat_id, phone):
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor()
    cursor.execute(f"""UPDATE users SET phone = '{phone}' WHERE chat_id = {chat_id}""")
    connect.commit()
    connect.close()

def get_slot_status(speaker_id, slot_id, date):
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor()
    cursor.execute(f"""SELECT status FROM slots WHERE speaker_id = {speaker_id} AND slot_id = {slot_id} AND date={date}""")
    status = cursor.fetchone()
    connect.commit()
    connect.close()
    return status


def add_approve(chat_id, speaker_id, theme_id, date, slot_id):
    connect = psycopg2.connect(user=config.DB_USER,
                                  password=config.DB_PASS,
                                  host=config.DB_HOST,
                                  port=config.DB_PORT,
                                  database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = connect.cursor(cursor_factory=NamedTupleCursor)
    cursor.execute(f"""INSERT INTO approves (chat_id, speaker_id, theme_id, date, slot_id) VALUES
                                         ({chat_id}, {speaker_id}, {theme_id}, {date}, {slot_id}) RETURNING ID""")
    res = cursor.fetchone()[0]
    connect.commit()
    connect.close()
    return res


def get_user(chat_id):
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor(cursor_factory=NamedTupleCursor)
    cursor.execute(f"""SELECT * FROM users WHERE chat_id = {chat_id}""")
    res = cursor.fetchall()[0]
    connect.commit()
    connect.close()
    return res


def get_approve(id):
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor(cursor_factory=NamedTupleCursor)
    cursor.execute(f"""SELECT * FROM approves WHERE id = {id}""")
    res = cursor.fetchall()
    connect.commit()
    connect.close()

    if res != []:
        return res[0]
    return res


def set_approve_status(id, status):
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor()
    cursor.execute(f"""UPDATE approves SET status = {status} WHERE id = {id}""")
    connect.commit()
    connect.close()


def add_slot(speaker_id, date, slot_id):
    connect = psycopg2.connect(user=config.DB_USER,
                                  password=config.DB_PASS,
                                  host=config.DB_HOST,
                                  port=config.DB_PORT,
                                  database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = connect.cursor(cursor_factory=NamedTupleCursor)
    cursor.execute(f"""INSERT INTO slots (speaker_id, date, slot_id, status) VALUES
                                         ({speaker_id}, {date}, {slot_id}, {True})""")

    connect.commit()
    connect.close()


def get_approve_by_chat_id(chat_id):
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor(cursor_factory=NamedTupleCursor)
    cursor.execute(f"""SELECT * FROM approves WHERE chat_id = {chat_id}""")
    res = cursor.fetchall()
    connect.commit()
    connect.close()
    return res

def del_approve(approve_id):
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor(cursor_factory=NamedTupleCursor)
    cursor.execute(f"""DELETE FROM approves WHERE id = {approve_id}""")
    connect.commit()
    connect.close()
