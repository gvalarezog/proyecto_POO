from Aplicacion.Datos.conexion import Conexion


class PersonaDAO:
    _INSERTAR = "INSERT INTO Personas (nombre,apellido,cedula,email,sexo) VALUES (?,?,?,?,?)"

    @classmethod
    def insertar(cls, persona):
        exito = False
        mensaje = ''
        try:
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.cedula, persona.email, persona.sexo)
                cursor.execute(cls._INSERTAR, valores)
                mensaje = 'Ingreso exitoso'
                exito = True
        except Exception as e:
            exito = False
            mensaje = e
            print(e)
            print(type(e))
        finally:
            return {'exito':exito, 'mensaje':mensaje}


if __name__ == '__main__':
    # PersonaDAO.insertar()
    pass