class Patient():
	def __init__(self, username, id_):
		self.name = username
		self.id = id_

	def get_username(self):
		return self.name

	def get_id(self):
		return self.id