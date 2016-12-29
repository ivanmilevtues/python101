import base64
import hashlib
import re


def encode_password(password):
	t_sha = hashlib.sha512()
	password = base64.b64encode(t_sha.digest())
	return password


def validate_password(password):
	if len(password) < 8 or (not re.search('\d', password)) or \
		(not re.search('[A-Z]', password)) or \
		(not re.search('[a-z]', password)):
		return False
	return True
