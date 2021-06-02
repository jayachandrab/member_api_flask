from flask import Flask,g
import sqlite3
from datetime import datetime


app = Flask(__name__)

def db_connect():
    sql=sqlite3.connect('member_api.db')
    sql.row_factory=sqlite3.Row
    return sql
def get_db():
    if not hasattr(g,'sqlite_db'):
        g.sqlite_db=db_connect()
    return g.sqlite_db

