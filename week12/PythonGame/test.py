class DeathError(Exception):
    pass


try:
    raise DeathError
except DeathError:
    print("?")
