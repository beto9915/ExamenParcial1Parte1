class Program:
    @staticmethod
    def main():
        opcion=0
        empleados={}
        while opcion!=5:
            print("""1. Ingresar empleado
            2. Buscar empleado por codigo
            3. Mostrar empleados con evaluacion satisfactoria
            4. Empleado con mejor promedio general""")
            opcion=int(input("Seleccione opcion: "))
            if opcion==1:
                print("\n===INGRESAR EMPLEADO===")
                codigo=input("\nIngrese codigo de empleado: ")
                nombre=input("Ingrese nombre completo: ")
                departamento=input("Ingrese el departamento en el que trabaja: ")
                antiguedad=input("Ingrese los años de antiguedad que tiene en la empresa: ")
                empleado=Empleado(codigo, nombre, departamento, antiguedad)
                puntualidad=int(input("Ingrese la nota por puntualidad (1-10): "))
                trabajo_equipo=int(input("Ingrese la nota por trabajo en equipo (1-10): "))
                productividad=int(input("Ingrese la nota por productividad (1-10): "))
                evaluacion=Evaluacion(puntualidad, trabajo_equipo, productividad)
                numero_telefono=int(input("Ingrese el numero de telefono: "))
                correo=input("Ingrese correo electronico: ")
                contacto=Contacto(numero_telefono, correo)
                empleados[codigo]={empleado, evaluacion, contacto}

class Empleado:
    @staticmethod
    def __init__(self,codigo, nombre, departamento, antiguedad):
        self.codigo=codigo
        self.nombre=nombre
        self.departamento=departamento
        self.antiguedad=antiguedad
class Evaluacion:
    @staticmethod
    def __init__(self, puntualidad, trabajo_equipo, productividad):
        self.puntualidad=puntualidad
        self.trabajo_equipo=trabajo_equipo
        self.productividad=productividad
    @staticmethod
    def promedio(nota1, nota2, nota3):
        promedio=(nota1+nota2+nota3)/3


class Contacto:
    @staticmethod
    def __init__(self, telefono, correo):
        self.telefono=telefono
        self.correo=correo
