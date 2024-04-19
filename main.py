import classes.mitarbeiter as us

mitarbeiter = []

user1 = us.Users(123, 1, "Tester")
user2 = us.Users(124, 2, "Tester2")
admin1 = us.Admins(125, 5, "Admin1", True)
admin2 = us.Admins(126, 6, "Admin2", True)

mitarbeiter.append(user1)
mitarbeiter.append(user2)

mitarbeiter.append(admin1)
mitarbeiter.append(admin2)

admin1.add_user(127, "Tester2", 6)

admin1.delete_user(124, mitarbeiter)
