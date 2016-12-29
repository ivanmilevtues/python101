DROP_USER_TABLE = '''
    DROP TABLE IF EXISTS USER
'''

DROP_PATIENT_TABLE = '''
    DROP TABLE IF EXISTS PATIENT
'''

DROP_DOCTOR_TABLE = '''
    DROP TABLE IF EXISTS DOCTOR
'''

DROP_HOSPITAL_STAY_TABLE = '''
    DROP TABLE IF EXISTS HOSPITAL_STAY
'''

DROP_VISITATION_TABLE = '''
    DROP TABLE IF EXISTS VISITATION
'''


CREATE_USER_TABLE = '''
    CREATE TABLE IF NOT EXISTS USER (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USERNAME TEXT NOT NULL,
        PASSWORD TEXT NOT NULL,
        IS_ACTIVE INTEGER NOT NULL DEFAULT 0,
        AGE INTEGER
    )
'''

CREATE_DOCTOR_TABLE = '''
    CREATE TABLE IF NOT EXISTS DOCTOR (
        ID INTEGER PRIMARY KEY,
        ACADEMIC_TITLE TEXT,
        FOREIGN KEY (ID) REFERENCES USER(ID)
    )
'''

CREATE_PATIENT_TABLE = '''
    CREATE TABLE IF NOT EXISTS PATIENT (
        ID INTEGER PRIMARY KEY,
        DOCTOR_ID INTEGER,
        FOREIGN KEY (ID) REFERENCES USER(ID),
        FOREIGN KEY (DOCTOR_ID) REFERENCES DOCTOR(ID)
    )
'''

CREATE_HOSPITAL_STAY_TABLE = '''
    CREATE TABLE IF NOT EXISTS HOSPITAL_STAY (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        STARTDATE TEXT NOT NULL,
        ENDDATE TEXT,
        ROOM INTEGER NOT NULL,
        INJURY TEXT NOT NULL,
        PATIENT_ID INTEGER,
        FOREIGN KEY (PATIENT_ID) REFERENCES PATIENT(ID)
    )
'''

CREATE_VISITATION_TABLE = '''
    CREATE TABLE IF NOT EXISTS VISITATION (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PATIENT_ID INTEGER,
        DOCTOR_ID INTEGER NOT NULL,
        START_HOUR TEXT NOT NULL,
        FOREIGN KEY (PATIENT_ID) REFERENCES PATIENT(ID),
        FOREIGN KEY (DOCTOR_ID) REFERENCES DOCTOR(ID)
    )
'''

INSERT_INTO_USER = '''
	INSERT INTO USER (USERNAME, PASSWORD, AGE, IS_ACTIVE)
	VALUES (?,?,? ,0)
			       '''
INSERT_INTO_HOSPITAL_STAY = '''
	INSERT INTO HOSPITAL_STAY (STARTDATE, ENDDATE, ROOM, INJURY, PATIENT_ID)
	VALUES (?, ?, ?, ?, ?)
'''

INSERT_VISITATION_HOUR = """
INSERT INTO visitation (PATIENT_ID, DOCTOR_ID, START_HOUR)
VALUES(?, ?, ?)
"""

SELECT_USERS = '''
	SELECT *
	FROM USER
'''

SELECT_DOCTORS = '''
	SELECT *
	FROM DOCTOR
'''

SELECT_PATIENTS = '''
	SELECT *
	FROM PATIENT
'''

PROMOTE_TO_DOCTOR = '''
	INSERT INTO DOCTOR (ID, ACADEMIC_TITLE)
	VALUES (?, ?)
'''

PROMOTE_TO_PATIENT = '''
	INSERT INTO PATIENT (ID, DOCTOR_ID)
	VALUES (?, ?)
'''

UPDATE_ACTIVE = '''
	UPDATE USER
	SET IS_ACTIVE = ?
	WHERE ID = ?
'''

SELECT_DOCTOR_PATIENTS = """
	SELECT DISTINCT *
	FROM USER, PATIENT
	WHERE patient.doctor_id = ? and  user.id = patient.id
"""

SELECT_PATIENT_DOCTOR = """
	SELECT u.id, u.username
	FROM DOCTOR as d, PATIENT as p, user as u
	WHERE d.id = p.DOCTOR_ID and p.id = ? and u.id = d.id
"""

SELECT_DOCTOR_TITLE = """
	SELECT d.ACADEMIC_TITLE
	FROM doctor as d
	WHERE d.id = ?
"""

GET_HOSPITAL_STAY = """
	SELECT *
	FROM hospital_stay as h
	WHERE h.PATIENT_ID = ?
"""

DELETE_VISITATION_HOUR = """
	DELETE FROM VISITATION
	WHERE START_HOUR = ?
"""
