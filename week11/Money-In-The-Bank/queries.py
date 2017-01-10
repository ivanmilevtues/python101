DROP_DB = """
    DROP TABLE if exists clients
"""

CREATE_QUERY = """
    CREATE TABLE IF NOT EXISTS
    clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    email TEXT,
    balance REAL DEFAULT 0,
    message TEXT,
    login_attempts INT DEFAULT 0,
    timeout REAL DEFAULT 0)
"""


UPDATE_SQL = """
    UPDATE clients 
    SET message = ?
    WHERE id = ?
"""


INSERT_SQL = """
    INSERT INTO clients (username, password)
    VALUES (?, ?)
"""


SELECT_USER = """
    SELECT *
    FROM clients
    WHERE USERNAME = ?
"""


SELECT_USERNAME = """
    SELECT id, username, balance, message, login_attempts
    FROM clients
    WHERE username = ? AND password = ? LIMIT 1
"""

UPDATE_ATTEMPTS = """
    UPDATE clients
    SET login_attempts = ?
    WHERE username = ?
"""

BAN_FOR_5min = """
    UPDATE clients
    SET timeout = ?
    WHERE username = ?
"""

TAKE_EMAIL = """
    SELECT  email
    FROM clients
    WHERE username = ?
"""