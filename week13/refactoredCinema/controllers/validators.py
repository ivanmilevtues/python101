from settings import SharedValues
from controllers.sign import log_in


def logged(func):
    def decorated(*args, **kwargs):
        if not SharedValues.user_logged:
            log_in()
        func()
    decorated(func)
