from peewee import *
from peewee import SqliteDatabase
import datetime

db = SqliteDatabase('news_articles.db')


class BaseModel(Model):
    class Meta:
        database = db


class NewsArticle(BaseModel):
    id = TextField(primary_key=True, unique=True)
    # id = UUIDField(primary_key==True, unique=True)
    headline = TextField()
    URL = TextField()
    # publish_time = DateTimeField(default=datetime.datetime.now)
    publish_time = TextField()
    source_name = TextField()


if __name__ == '__main__':
    db.connect()
    # db.drop_tables([NewsArticle])
    db.create_tables([NewsArticle])
    db.close()
