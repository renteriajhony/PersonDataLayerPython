from Data.conexion import Connection
from logger_base import log


class CursorOfPool:
    def __init__(self):
        self._connetion = None
        self._cursor = None

    def __enter__(self):
        log.debug("Inicio del metodo with __enter__")
        self._connetion = Connection().getConnection()
        self._cursor = self._connetion.cursor()
        return self._cursor

    # renombramos prefijo exc por excepcion, para recordar a que hace referencia
    def __exit__(self, excepcion_type, excepcion_val, excepcion_tb):
        log.debug(f'Se ejecuta metodo __exit__')
        if excepcion_val:
            self._connetion.rollback()
            log(f'Ocurrió una exepcion, se hace rollBack:\n Type: {excepcion_type} \n Value: {excepcion_val} \n Detail: {excepcion_tb} ')
        else:
            self._connetion.commit()
            log.debug(f'Commit de la transaction')
        self._cursor.close()
        Connection.freeConnectionPool(self._connetion)

if __name__ == '__main__':
    with CursorOfPool() as cursor:
        cursor.execute('SELECT * FROM PUBLIC.PERSON')
        print(cursor.fetchall())