import sys

import pyodbc as bd


class Conexion:
    _SERVIDOR = '192.168.195.251'
    # _SERVIDOR = 'localhost'
    # _SERVIDOR = '127.0.0.1'
    _BBDD = 'APP_MAT'
    _USUARIO = 'app_mat_user'
    _PASSWORD = '12345678'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                           cls._SERVIDOR + ';DATABASE=' + cls._BBDD + ';UID=' + cls._USUARIO + ';PWD=' + cls._PASSWORD)
                # log.debug(f'Conexión exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                # log.error(f'Ocurrió una excepción al obtener la conexión: {e}')
                print(e)
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                # log.debug(f'Se abrió correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                # log.error(f'Ocurrió una excepción al obtener el cursor: {e}')
                sys.exit()
        else:
            return cls._cursor

if __name__ == '__main__':
    print(Conexion.obtenerConexion())
    print(Conexion.obtenerCursor())