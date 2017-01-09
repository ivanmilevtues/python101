DROP_MOVIE_TABLE = """
    DROP TABLE IF EXISTS MOVIE
"""

DROP_PROJECTION_TABLE = """
    DROP TABLE IF EXISTS PROJECTION
"""

DROP_USER_TABLE = """
    DROP TABLE IF EXISTS USER
"""

DROP_RESETVATION_TABLE = """
    DROP TABLE IF EXISTS RESETVATION
"""

CREATE_MOVIE_TABLE = '''
    CREATE TABLE IF NOT EXISTS MOVIE (
         ID INTEGER PRIMARY KEY AUTOINCREMENT,
         NAME TEXT NOT NULL,
         RATING REAL NOT NULL DEFAULT 0
    )
'''

CREATE_PROJECTION_TABLE = '''
    CREATE TABLE IF NOT EXISTS PROJECTION (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        MOVIE_ID INTEGER NOT NULL,
        TYPE TEXT NOT NULL,
        DATE_ TEXT NOT NULL,
        TIME_ TEXT NOT NULL,
        FOREIGN KEY (MOVIE_ID) REFERENCES MOVIE(ID)
    )
'''

CREATE_USER_TABLE = '''
    CREATE TABLE IF NOT EXISTS USER (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USERNAME TEXT NOT NULL,
        PASSWORD TEXT NOT NULL,
        ACTIVE INTEGER NOT NULL
    )
'''

CREATE_RESERVATION_TABLE = '''
    CREATE TABLE IF NOT EXISTS RESERVATION (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USER_ID INTEGER NOT NULL,
        PROJECTION_ID INTEGER NOT NULL,
        ROW INTEGER NOT NULL,
        COL INTEGER NOT NULL,
        FOREIGN KEY (USER_ID) REFERENCES USER(ID),
        FOREIGN KEY (PROJECTION_ID) REFERENCES PROJECTION(ID)
    )
'''


INSERT_MOVIE = '''
    INSERT INTO MOVIE (NAME, RATING)
    VALUES (?,?);
'''

INSERT_PROJECTION = '''
    INSERT INTO PROJECTION (MOVIE_ID, TYPE, DATE_, TIME_)
    VALUES (?, ?, ?, ?);
'''

INSERT_RESERVATION = '''
    INSERT INTO RESERVATION (USER_ID, PROJECTION_ID, ROW, COL)
    VALUES (?, ?, ?, ?);
'''

INSERT_USER = '''
    INSERT INTO USER(USERNAME, PASSWORD, ACTIVE)
    VALUES (?, ?, ?)
'''