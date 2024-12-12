import sys

import psycopg2 as db

from logger_base import log


class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'postgres'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conexion = None
    _cursor = None

    @classmethod
    def getConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = db.connect(host=cls._HOST, user=cls._USERNAME, password=cls._PASSWORD,
                                           port=cls._DB_PORT, database=cls._DATABASE)
                log.debug(f'Conexion a base de datos exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.error(f'Ocurrio un error al conectar a la base de datos: {e}')
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def getCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.getConexion().cursor()
                log.debug(f'Se abrió correctamente el cursor: {cls._conexion}')
                return cls._cursor
            except Exception as e:
                log.error(f'Ocurrio un error al optener cursor: {e}')
                sys.exit()
        else:
            return cls._cursor


if __name__ == '__main__':
    Conexion.getCursor()
