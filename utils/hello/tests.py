from sqlite import DataBase


def test():
    db = DataBase()
    db.create_table_users()
    db.add_user(1, "one", 'email', 465465, "dnsjdnj", "+55115195", "+55115195")
    db.add_user(2, "two", 'email', 465465, "dnsjdnj", "+55115195", "+55115195")
    db.add_user(3, "three", 'email', 465465, "dnsjdnj", "+55115195", "+55115195")
    db.add_user(4, "four", 'email', 465465, "dnsjdnj", "+55115195", "+55115195")
    db.add_user(5, "five", 'email', 465465, "dnsjdnj", "+55115195", "+55115195")

    users = db.select_all_users()
    print(f"Barcha foydalanuvchilar: {users}")

    user = db.select_user(full_name="five", id=5)
    print(f"Bitta foydalanuvchini ko'rish {user}")


test()
