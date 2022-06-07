from api import database as d


def get_db():
    DB=d.Sessionlocal()

    try:
        yield DB
    finally:
        DB.close()