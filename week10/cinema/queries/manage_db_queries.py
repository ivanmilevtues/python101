SELECT_MOVIES = """
    SELECT *
    FROM movie
    ORDER BY RATING
"""

SELECT_PROJECTIONS_FOR_DATE = """
    SELECT p.ID, p.DATE_, p.TIME_, p.TYPE
    FROM movie as m, projection as p
    WHERE p.DATE_ = ? and p.movie_id = m.id and m.id = ?
    ORDER BY TIME_;
"""


SELECT_PROJECTIONS = """
    SELECT p.ID, p.DATE_, p.TIME_, p.TYPE
    FROM movie as m, projection as p
    WHERE p.movie_id = m.id and m.id = ?
    ORDER BY TIME_;
"""

SELECT_USERS = """
    SELECT *
    FROM user
"""

UPDATE_ACTIVE = """
    UPDATE user
    SET ACTIVE = ?
    WHERE USERNAME = ?
"""
