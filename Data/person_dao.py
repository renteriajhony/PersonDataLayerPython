from Data.cursor_of_pool import CursorOfPool
from Data.person import Person
from logger_base import log


class PersonDAO:
    _SELECT = 'SELECT id_person, name, last_name, email FROM PUBLIC.PERSON ORDER BY id_person ASC'
    _INSERT = 'INSERT INTO PUBLIC.PERSON ( name, last_name, email) VALUES (%s, %s, %s)'
    _UPDATE = 'UPDATE PUBLIC.PERSON SET name = %s, last_name = %s, email = %s WHERE id_person = %s'
    _DELETE= 'DELETE FROM PUBLIC.PERSON WHERE id_person = %s'

    @classmethod
    def createPerson(cls, person: Person):
        with CursorOfPool() as cursor:
            values = (person.name, person.last_name, person.email)
            cursor.execute(cls._INSERT, values)
            log.debug(f'Persona insertada: {person}')
            return cursor.rowcount

    @classmethod
    def readPerson(cls):
        with CursorOfPool() as cursor:
            cursor.execute(cls._SELECT)
            records = cursor.fetchall()
            personList: [Person] = []
            for record in records:
                person = Person(record[0], record[1], record[2], record[3])
                personList.append(person)
            return personList

    @classmethod
    def updatePerson(cls, person: Person):
        with CursorOfPool() as cursor:
            values = (person.name, person.last_name, person.email, person.id_person)
            cursor.execute(cls._UPDATE, values)
            log.debug(f'Persona actualizada: {person}')
            return cursor.rowcount

    @classmethod
    def deletePerson(cls, person: Person):
        with CursorOfPool() as cursor:
            values = (person.id_person,)
            cursor.execute(cls._DELETE, values)
            log.debug(f'Persona eliminada: {person}')
            return cursor.rowcount


if __name__ == '__main__':

    person = Person(name='Manuel', last_name='Garcia', email='mgarcia@mail.com')
    registers = PersonDAO.createPerson(person)
    log.debug(f'Registros creados: {registers}')

    person = Person(name='Pablo', last_name='Prado', email='pprado@mail.com', id_person=2)
    registers = PersonDAO.updatePerson(person)
    log.debug(f'Registros actualizados: {registers}')

    person = Person(id_person=5)
    registers = PersonDAO.deletePerson(person)
    log.debug(f'Registros eliminados: {registers}')

    personList = PersonDAO.readPerson()
    for person in personList:
        log.debug(person)

