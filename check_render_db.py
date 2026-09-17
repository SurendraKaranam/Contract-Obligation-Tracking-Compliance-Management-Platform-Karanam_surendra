from app.database.database import SessionLocal
from app.models import User

db = SessionLocal()

try:
    users = db.query(User).all()

    print("========== RENDER USERS ==========")

    for user in users:
        print(
            "ID:", user.id,
            "| EMAIL:", user.email,
            "| ROLE:", user.role,
            "| ACTIVE:", user.is_active
        )

    print("TOTAL USERS:", len(users))
    print("==================================")

finally:
    db.close()