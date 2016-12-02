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
        if not self.has_panda(panda2):
            self.add_panda(panda2)
        self.connections[panda1].append(panda2)
        self.connections[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        return True if panda2 in self.connections[panda1] else False

    def friends_of(self, panda):
        return False if panda not in self.connections \
            else self.connections[panda]

    def take_paths(self, panda1, panda2, path=[]):
        path.append(panda1)
        if panda1 == panda2:
            return [path]
        if panda1 not in self.connections:
            return []
        paths = []
        for friend in self.connections[panda1]:
            if friend not in path:
                newpaths = self.take_paths(friend, panda2, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def connection_level(self, panda1, panda2):
        if not self.has_panda(panda1) or not self.has_panda(panda2):
            return False
        paths = self.take_paths(panda1, panda2)
        if paths:
            return len(sorted(paths)[0]) - 1
        return -1

    def are_connected(self, panda1, panda2):
        is_path = self.connection_level(panda1, panda2)
        if is_path != -1 and is_path:
            return True
        return False

    def how_many_gender_in_network(self, level, panda, gender):
        gender_num = 0
        for user in self.connections:
            print(user)
            # print(self.are_connected(panda, user))
            if self.connection_level(panda, user) == level:
                if user.gender == gender:
                    gender_num += 1
        return gender_num


def main():
    ivo = Panda("Ivo", "Ivo@k.com", "male")
    valio = Panda("Valio", "k@k.com", "male")
    kiko = Panda("Kiko", "kir4o@robopartans.com", "male")
    chorbi = Panda("Lubo", "l@chr.com", "male")
    dudev = Panda("Dudevian", "Dudevian@emo.com", "male")
    misho = Panda("Misho", "misho@hidr0.com", "male")
    lonely = Panda("4EverAlone", "nofrs@sad.com", "female")
    # print(k.get_name())
    # print(k.get_email())
    # print(k.get_gender())
    a = SocialNetowork()
    a.add_panda(ivo)
    a.add_panda(valio)
    a.add_panda(lonely)
    # print(a.connections)
    a.add_panda(dudev)
    a.make_friends(misho, kiko)
    a.make_friends(valio, kiko)
    a.make_friends(kiko, ivo)
    a.make_friends(ivo, chorbi)
    print(a.connection_level(ivo, kiko))
    print(a.are_connected(chorbi, lonely))
    print(a.how_many_gender_in_network(1, kiko, 'male'))
    # print(a.are_friends(i, k))
    # print(a.connections)
    # print(a.friends_of(i))
    # ivo = Panda("Ivo", "kkk", "panda")


if __name__ == '__main__':
    main()
