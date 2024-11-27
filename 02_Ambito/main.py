import suma


# Variable Local
def funcion_local():
    variable_local = "Variable local en funcion_local"
    print(variable_local)

# Variable Enclosing
def funcion_externa():
    variable_enclosing = "Variable enclosing en funcion_externa"
    
    def funcion_interna():
        print(variable_enclosing)
    
    funcion_interna()

# Variable No Local
def funcion_no_local():
    variable_no_local = "Variable no local en funcion_no_local"
    
    def funcion_interna_no_local():
        nonlocal variable_no_local
        variable_no_local = "Variable no local modificada en funcion_interna_no_local"
    
    funcion_interna_no_local()
    print(variable_no_local)

# Variable Built-in
def funcion_built_in():
    print(len("Variable built-in"))



if __name__ == "__main__":
    
    funcion_local()
    funcion_externa()
    funcion_no_local()
    funcion_built_in()


    mensaje = "Adiós"  # ✅ Podemos modificar con nonlocal


class Persona:
    # Atributo de clase
    especie = "Humano"
    
    def __init__(self, nombre, edad):
        # Atributos de instancia
        self.nombre = nombre
        self.edad = edad
    
    # Método de instancia
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
    
    # Método de clase
    @classmethod
    def obtener_especie(cls):
        return cls.especie
    
    # Método estático
    @staticmethod
    def es_mayor_de_edad(edad):
        return edad >= 18

# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 30)

# Acceder a los atributos y métodos
print(persona1.nombre)  # Juan
print(persona1.edad)    # 30
persona1.saludar()      # Hola, mi nombre es Juan y tengo 30 años.
print(Persona.obtener_especie())  # Humano
print(Persona.es_mayor_de_edad(20))  # True


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Punto(3, 4)
p.z = "mundo"  # Agregar un nuevo atributo dinámicamente
print(p.z)  # mundo

# Ejemplo de intento de añadir atributos a tipos integrados
x = 10
try:
    x.new_attr = "nuevo atributo"
except AttributeError as e:
    print(f"Error: {e}")  # Error: 'int' object has no attribute 'new_attr'

y = [1, 2, 3]
try:
    y.new_attr = "nuevo atributo"
except AttributeError as e:
    print(f"Error: {e}")  # Error: 'list' object has no attribute 'new_attr'

z = 3.14
try:
    z.new_attr = "nuevo atributo"
except AttributeError as e:
    print(f"Error: {e}")  # Error: 'float' object has no attribute 'new_attr'

s = "cadena"
try:
    s.new_attr = "nuevo atributo"
except AttributeError as e:
    print(f"Error: {e}")  # Error: 'str' object has no attribute 'new_attr'


class Padre:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Hijo(Padre):
    def __init__(self, nombre, edad, escuela):
        super().__init__(nombre, edad)  # Llamar al constructor de la clase padre
        self.escuela = escuela

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Escuela: {self.escuela}")

# Crear una instancia de la clase Hijo
hijo1 = Hijo("Carlos", 15, "Escuela Secundaria")
hijo1.mostrar_informacion()  # Nombre: Carlos, Edad: 15, Escuela: Escuela Secundaria
