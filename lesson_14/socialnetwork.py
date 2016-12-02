# Use BFS
import re


class Panda:
    @staticmethod
    def __email_validation(email):
        return True if re.match("\w+@\w+.\w+", email) else False

    def __init__(self, name, email, gender):
        self.name = name
        # print(Panda.__email_validation(email))
        if Panda.__email_validation(email):
            self.email = email
        else:
            raise ValueError
        self.email = email
        self.gender = gender

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_gender(self):
        return self.gender

    def isMale(self):
        return True if self.gender == 'Male' else False

    def isFemale(self):
        return True if self.gender == 'Female' else False

    def __str__(self):
        return "Name: {0}\nEmail - {1}\nGender: {2}".format(self.name,
                                                            self.email,
                                                            self.gender)

    def __eq__(self, other):
        return self.name == other.name and self.email == other.email and \
               self.gender == other.gender

    def __hash__(self):
        return hash(self.name) * hash(self.gender) * hash(self.email)


class SocialNetowork:
    def __init__(self):
        self.connections = {}

    def add_panda(self, panda):
        if self.has_panda(panda):
            raise "PandaAlreadyThere"
        self.connections[panda] = []

    def has_panda(self, panda):
        return True if panda in self.connections else False

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)
        elif not self.has_panda(panda2):
            self.add_panda(panda2)
        self.connections[panda1].append(panda2)
        self.connections[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        return True if panda2 in self.connections[panda1] else False

    def friends_of(self, panda):
        return False if panda not in self.connections else self.connections[panda]

    def connection_level(self,)

def main():
    k = Panda("K", "k@k.com", "d")
    i = Panda("sadsdK", "k@k.com", "dasdda")
    kiko = Panda("Kiko", "kir4o@robopartans.com", "male")
    print(k.get_name())
    print(k.get_email())
    print(k.get_gender())
    a = SocialNetowork()
    a.add_panda(k)
    a.add_panda(i)
    print(a.connections)
    a.make_friends(i, kiko)
    print(a.connections)
    print(a.are_friends(i, k))
    print(a.friends_of(i))
    # ivo = Panda("Ivo", "kkk", "panda")


if __name__ == '__main__':
    main()
