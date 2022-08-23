

class Persona:
    contador_persona = 0
    def __init__(self, nombre=None, apellido=None, cedula=None, email=None, sexo=None):
        Persona.contador_persona += 1
        self._id = Persona.contador_persona
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._email = email

    def __str__(self):
        return f'Persona [id: {self._id}, nombre: {self._nombre}, apellido: {self._apellido}, ' \
               f'cedula: {self._cedula}, email: {self._email}]'

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, sexo):
        self._sexo = sexo

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

if __name__ == '__main__':
    p1 = Persona(nombre='Luis', apellido='Perez', cedula='0123456789', sexo='Masculinio', email='luis@mail.com')
    p2 = Persona(nombre='Maria', apellido='Paz', cedula='9876543210', sexo='Femenino')
    print(p1.__str__())
    print(p2)