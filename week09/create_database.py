import sqlite3

DB_NAME = "hospital.db"
db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()
#
# drop_db = """DROP TABLE IF EXISTS PATIENT"""
# c.execute(drop_db)
# db.commit()
#
# create_patients_table = """
# CREATE TABLE IF NOT EXISTS PATIENT (
#   ID INTEGER PRIMARY KEY AUTOINCREMENT,
#   FIRSTNAME TEXT NOT NULL,
#   LASTNAME TEXT NOT NULL,
#   AGE INTEGER NOT NULL
# )
# """
# c.execute(create_patients_table)
# db.commit()

# firstname = 'Viktor'
# lastname = 'Barzin'
# age = 18
#
# insert_patient = """
# INSERT INTO PATIENT (FIRSTNAME, LASTNAME, AGE)
# VALUES(?, ?, ?)
# """


# c.execute(insert_patient, (firstname, lastname, age))
# db.commit()

# patients = [("Baba", "Tonka", 90),
#             ("Dqdo", "Toni", 80),
#             ("Lelq", "Mariq", 59)]
#
# c.executemany(insert_patient, patients)
# db.commit()


list_patients = """SELECT * FROM patients """
result = c.execute(list_patients)
for row in result:
    print(row[0])
    print(row['firstname'])
# c.execute(list_patients)
# print(c.fetchall())
# print(c.fetchone())
# print(c.fetchone())
db.commit()
