from peewee import *
from peewee import SqliteDatabase
import datetime

db = SqliteDatabase('new_articles.db')


class BaseModel(Model):
    class Meta:
        database = db


class NewsArticle(BaseModel):
    id = TextField(primary_key=True, unique=True)
    headline = TextField()
    URL = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    source_name = TextField()


if __name__ == '__main__':
    db.connect()
    db.drop_tables([NewsArticle])
    db.create_tables([NewsArticle])
    db.close()
