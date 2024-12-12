from logger_base import log


class Person:
    def __init__(self, id_person=None, name=None, last_name=None, email=None):
        self._id_person = id_person
        self._name = name
        self._last_name = last_name
        self._email = email

    def __str__(self):
        return (f'''Person:
                Id person: {self._id_person},
                Name: {self._name},
                Last name: {self._last_name},
                Email: {self._email}''')

    @property
    def id_person(self):
        return self._id_person

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email


if __name__ == '__main__':
    person = Person(1, 'Jhony', 'Mande', 'jr@mail.com')
    log.debug(person)
    # Simular insert
    person1 = Person(name='Jhony2', last_name='Mande', email='jr@mail.com')
    log.debug(person1)
    # Simular delete
    person1 = Person(1)
    log.debug(person1)
