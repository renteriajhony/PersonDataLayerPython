import sys

from psycopg2 import pool

from logger_base import log


class Connection:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'postgres'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def getConnectionPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CON,
                    cls._MAX_CON,
                    host=cls._HOST,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    port=cls._DB_PORT,
                    database=cls._DATABASE
                )
                log.debug(f'Creacion del pool  exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el pool: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def getConnection(cls):
        connetion = cls.getConnectionPool().getconn()
        log.debug(f'Connection obtenida del pool: {connetion}')
        return connetion

    @classmethod
    def freeConnectionPool(cls, connection):
        cls.getConnectionPool().putconn(connection)
        log.debug(f'Regresamos la conexion al pool: {connection}')

    @classmethod
    def closeConnectionPool(cls):
        cls.getConnectionPool().closeall()

if __name__ == '__main__':
    connetion1 = Connection.getConnection()
    Connection.freeConnectionPool(connetion1)
    connetion2 = Connection.getConnection()
    connetion3 = Connection.getConnection()
    connetion4 = Connection.getConnection()
    connetion5 = Connection.getConnection()
    connetion6 = Connection.getConnection() # Falla porque supera el maximo de connetiones especificados
