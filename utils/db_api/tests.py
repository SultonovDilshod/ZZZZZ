from postgresql_tmc import DataBase

import asyncio


async def test():
    db = DataBase()
    await db.create()
    print("Javal yaratildi.....")
    await db.create_table_users()
    print("YARATDIK")

    await db.add_user('Umidjon', 'hope', 123456, 566556, "sjsjkd@gamil.com0", "+998494494")
    await db.add_user('Odiljon', 'sariqdev', 123457, 566556, "sjsjkd@gamil.com0", "+998494494")
    await db.add_user('Ali', 'sqriqdev', 123458, 566556, "sjsjkd@gamil.com0", "+998494494")
    await db.add_user('Vali', 'sqriqdev', 123459, 566556, "sjsjkd@gamil.com0", "+998494494")
    await db.add_user('Sobir', 'sobir', 123450, 566556, "sjsjkd@gamil.com0", "+998494494")
    print("QO'SHDIK")

    users = db.select_all_users()
    print(f"Barcha foydalanuvchilar {users}")

    user = db.select_user(id=5)
    print(f"Foydalanuvchi {user}")


asyncio.run(test())
