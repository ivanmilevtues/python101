# Use BFS
from collections import deque
import json
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
        return "Name: {0}\nEmail: {1}\nGender: {2}".format(self.name,
                                                           self.email,
                                                           self.gender)

    def __repr__(self):
        return str(self)

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

    def connection_level(self, panda1, panda2):
        if panda2 in self.connections[panda1]:
            return 1
        paths = {panda1: None}
        q = deque()
        visited = set()

        q.append(panda1)
        visited.add(panda1)

        while q:
            current = q.popleft()

            if current == panda2:
                path = []
                while panda2:
                    path.append(panda2)
                    panda2 = paths[panda2]
                return len(path) - 1

            for panda in self.connections[current]:
                if panda not in visited:
                    visited.add(panda)
                    q.append(panda)
                    paths[panda] = current
        return -1

    def how_many_gender_in_network(self, level, panda, gender):
        count = 0
        for user in self.connections.keys():
            if level == self.connection_level(panda, user) and \
               gender == user.gender:
                count += 1
        return count

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

    def save(self, filename):
        data = {}

        for key in self.connections.keys():
            if str(key) not in data.keys():
                data[str(key)] = []
            for nei in self.connections[key]:
                data[str(key)].append(str(nei))

        with open(filename, "w") as file_json:
            json.dump(data, file_json)

    def make_panda(self, info_list):
        name = info_list[0].split(': ')[1]
        email = info_list[1].split(': ')[1]
        gender = info_list[2].split(': ')[1]
        return Panda(name, email, gender)

    def load(self, filename):
        # self.connections = {}
        panda_list = []
        data = {}
        self.connections = {}
        print(self.connections)

        with open(filename, "r") as file_json:
            data = json.load(file_json)

        for key in data.keys():
            info_list = key.split("\n")
            cur_panda = self.make_panda(info_list)
            for fr in data[key]:
                info_list = fr.split("\n")
                fr_cur_panda = self.make_panda(info_list)
                self.make_friends(cur_panda, fr_cur_panda)
            if cur_panda not in self.connections:
                self.add_panda(cur_panda)


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
    print(a.connection_level(misho, ivo))
    # print(a.how_many_gender_in_network(1, kiko, 'male'))
    print(a.are_friends(ivo, chorbi))
    a.save("test_save.json")
    b = SocialNetowork()
    b.load("test_save.json")
    print(b.connections)
    print(b.are_connected(ivo, lonely))
    print(b.how_many_gender_in_network(2, kiko, "male"))
    # print(a.friends_of(i))
    # ivo = Panda("Ivo", "kkk", "panda")


if __name__ == '__main__':
    main()
