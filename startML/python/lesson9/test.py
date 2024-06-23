from fastapi import FastAPI
import datetime
from pydantic import BaseModel
import json
import psycopg2
import pandas as pd


def get_user(id: int):
    conn = psycopg2.connect("postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml")
    cursor = conn.cursor()
    query = """
            SELECT gender, age, city FROM "user"
            WHERE id = %(id)s
            """
    cursor.execute(query, {'id': id})

    return cursor.fetchall()

print(get_user(200))