import re
import hashlib
import base64

def hash_password(passw):
    t_sha = hashlib.sha512()
    passw = base64.b64encode(t_sha.digest())
    return passw


def validate_password(passw):
    if len(passw) < 8:
        print("Password too short")
        return False
    if not re.search(r"\d", passw):
        print("No digits in the password!")
        return False
    if not re.search(r"[a-z][A-Z]", passw):
        print("Upper or lower case letters missing!")
        return False
    return True


def generate_new_pass():
	new_pass = ''
	ch_pool = string.ascii_uppercase + string.ascii_lowercase + string.digits
	while not validate_password(new_pass):
		new_pass = ''.joing(random.choive(chars) for _ in range(8))

	return password