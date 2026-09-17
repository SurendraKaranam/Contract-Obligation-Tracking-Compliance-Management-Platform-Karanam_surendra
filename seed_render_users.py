from app.database.database import SessionLocal
from app.models.user import User
from app.core.security import hash_password


users = [
    {
        "full_name": "Administrator",
        "email": "admin@contractiq.com",
        "role": "Administrator",
        "password": "Admin@12345",
    },
    {
        "full_name": "Legal Manager",
        "email": "legal@contractiq.com",
        "role": "Legal Manager",
        "password": "Legal@12345",
    },
    {
        "full_name": "Compliance Officer",
        "email": "compliance@contractiq.com",
        "role": "Compliance Officer",
        "password": "Cofficer@12345",
    },
    {
        "full_name": "Contract Manager",
        "email": "manager@contractiq.com",
        "role": "Contract Manager",
        "password": "Cmanager@12345",
    },
    {
        "full_name": "Department Head",
        "email": "head@contractiq.com",
        "role": "Department Head",
        "password": "Dhead@12345",
    },
    {
        "full_name": "Employee",
        "email": "employee@contractiq.com",
        "role": "Employee",
        "password": "Employee@12345",
    },
]


db = SessionLocal()

try:
    print("========== CONTRACTIQ USER SEED ==========")

    created = 0
    existing = 0

    for data in users:
        user = (
            db.query(User)
            .filter(User.email == data["email"])
            .first()
        )

        if user:
            print(f"EXISTS: {data['email']}")
            existing += 1
            continue

        new_user = User(
            full_name=data["full_name"],
            email=data["email"],
            role=data["role"],
            is_active=True,
            hashed_password=hash_password(data["password"]),
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        print(f"CREATED: {data['email']} | ROLE: {data['role']}")
        created += 1

    print("------------------------------------------")
    print(f"CREATED: {created}")
    print(f"ALREADY EXISTED: {existing}")
    print("==========================================")

finally:
    db.close()