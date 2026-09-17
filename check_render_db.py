from app.database.database import engine
from sqlalchemy import text

with engine.connect() as c:
    print("========== RENDER DATABASE CHECK ==========")
    print("USERS:", c.execute(text("SELECT to_regclass('public.users')")).scalar())
    print("CONTRACTS:", c.execute(text("SELECT to_regclass('public.contracts')")).scalar())
    print("ALEMBIC:", c.execute(text("SELECT to_regclass('public.alembic_version')")).scalar())

    version_table = c.execute(
        text("SELECT to_regclass('public.alembic_version')")
    ).scalar()

    if version_table:
        print("ALEMBIC VERSION:", c.execute(
            text("SELECT version_num FROM alembic_version")
        ).fetchall())
    else:
        print("ALEMBIC VERSION: TABLE DOES NOT EXIST")

    print("===========================================")
