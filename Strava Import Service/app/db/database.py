from sqlmodel import SQLModel, create_engine

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# def update_db_and_tables():
#     # save old data
#     # drop tables
#     # create new tables
#     # migrate old data to new schema
#     # insert new data
#
#     SQLModel.metadata.drop_all(engine)
#     SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()
