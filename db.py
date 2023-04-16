from sqlmodel import SQLModel, create_engine
from models import Joke

engine = create_engine("mysql://root@localhost/squadmakers?charset=utf8mb4")


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()