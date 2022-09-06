import pyodbc as bd

from Aplicacion.Datos.conexion import Conexion


class PersonaDAO:
    _INSERTAR = "INSERT INTO Personas (nombre,apellido,cedula,email,sexo) VALUES (?,?,?,?,?)"
    _SELECCIONAR_X_CED = "SELECT id, nombre, apellido, cedula, email, sexo FROM Personas WHERE cedula = ?"
    _ACTUALIZAR_X_CED = "UPDATE Personas SET nombre=? , apellido=?, email=?, sexo=? WHERE cedula=?"
    _ELIMINAR_X_CED = "DELETE FROM Personas WHERE cedula = ?"

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
        except bd.IntegrityError as e:
            exito = False
            print(e.__str__())
            if e.__str__().find('Cedula')>0:
                mensaje = 'Cédula ya ingresada.'
            elif e.__str__().find('Email')>0:
                mensaje = 'Email ya ingresado.'
            else:
                mensaje = 'Error de integridad'
        except Exception as e:
            exito = False
            mensaje = e
            print(e)
            print(type(e))
        finally:
            return {'exito':exito, 'mensaje':mensaje}

    @classmethod
    def seleccionar_por_cedula(cls, persona):
        persona_consultada = None
        try:
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.cedula)
                registro = cursor.execute(cls._SELECCIONAR_X_CED, valores)
                persona_consultada = registro.fetchone()
        except Exception as e:
            print(e)
            persona_consultada = None
        finally:
            return persona_consultada

    @classmethod
    def actualizar_por_cedula(cls, persona):
        exito = False
        mensaje = ''
        try:
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email, persona.sexo, persona.cedula)
                registros_modificados = cursor.execute(cls._ACTUALIZAR_X_CED, valores)
                if registros_modificados.rowcount > 0:
                    exito = True
                    mensaje = 'Actualización exitosa'
                else:
                    exito = False
                    mensaje = 'No se pudo actualizar el registro porque la cedula no existe.'
                print(valores)
        except Exception as e:
            print(e)
            exito = False
            mensaje = 'No se pudo actualizar el registro.'
        finally:
            return {'exito':exito, 'mensaje':mensaje}

    @classmethod
    def eliminar_por_cedula(cls, persona):
        exito = False
        mensaje = ''
        try:
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.cedula)
                registros_modificados = cursor.execute(cls._ELIMINAR_X_CED, valores)
                if registros_modificados.rowcount > 0:
                    exito = True
                    mensaje = 'Eliminación exitosa'
                else:
                    exito = False
                    mensaje = 'No se pudo eliminar el registro porque la cedula no existe.'
        except Exception as e:
            print(e)
            exito = False
            mensaje = 'No se pudo actualizar el registro.'
        finally:
            return {'exito': exito, 'mensaje': mensaje}


if __name__ == '__main__':
    # PersonaDAO.insertar()
    pass