from db import SESSION
from sqlalchemy import INT, VARCHAR, Column
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()


class ModelMixin:
    """A class that implements some operation methods for inherence"""

    @staticmethod
    def commit():
        SESSION.commit()

    @classmethod
    def query(cls):
        return SESSION.query(cls)

    def add(self):
        SESSION.add(self)


class Fruit(BASE, ModelMixin):  # type: ignore

    __tablename__ = "fruit"

    name = Column(VARCHAR, primary_key=True)
    count = Column(INT, nullable=False)

    def dumps(self):
        return {"name": self.name, "count": self.count}


def init_db():
    SESSION.merge(Fruit(**{"name": "apple", "count": 1}))
    SESSION.commit()
