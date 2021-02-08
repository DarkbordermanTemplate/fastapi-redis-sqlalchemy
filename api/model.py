from sqlalchemy import INT, VARCHAR, Column
from sqlalchemy.ext.declarative import declarative_base

from db import SESSION

BASE = declarative_base()


class Fruit(BASE):

    __tablename__ = "fruit"

    name = Column(VARCHAR, primary_key=True)
    count = Column(INT, nullable=False)

    def dumps(self):
        return {"name": self.name, "count": self.count}


def init_db():
    SESSION.merge(Fruit(**{"name": "apple", "count": 1}))
    SESSION.commit()
