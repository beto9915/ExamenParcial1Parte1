from contextlib import nullcontext


class Program:
    @staticmethod
    def main():
        opcion=0
        empleados={}
        while opcion!=5:
            print("""1. Ingresar empleado
            2. Buscar empleado por codigo
            3. Mostrar cuantos empleados tienen evaluacion satisfactoria
            4. Empleado con mejor promedio general""")
            opcion=int(input("Seleccione opcion: "))
            if opcion==1:
                print("\n===INGRESAR EMPLEADO===")
                codigo=input("\nIngrese codigo de empleado: ")
                nombre=input("Ingrese nombre completo: ")
                departamento=input("Ingrese el departamento en el que trabaja: ")
                antiguedad=int(input("Ingrese los años de antiguedad que tiene en la empresa: "))
                ##empleado=Empleado(codigo,nombre, departamento, antiguedad)
                puntualidad=int(input("Ingrese la nota por puntualidad (1-10): "))
                trabajo_equipo=int(input("Ingrese la nota por trabajo en equipo (1-10): "))
                productividad=int(input("Ingrese la nota por productividad (1-10): "))
                ##evaluacion=Evaluacion(puntualidad, trabajo_equipo, productividad)
                numero_telefono=int(input("Ingrese el numero de telefono: "))
                correo=input("Ingrese correo electronico: ")
                ##contacto=Contacto(numero_telefono, correo)
                empleados[codigo]={"nombre":nombre, "departamento":departamento, "antiguedad":antiguedad, "evaluacion": {}, "contacto":{}}

                empleados[codigo]["contacto"]={"numero_telefono":numero_telefono, "correo":correo}
                promedio=(puntualidad+trabajo_equipo+productividad)/3
                satisfactorio=0
                if promedio<=7:
                    print(f"El promedio es:{promedio}, Mejorar")

                else:
                    print(f"El promedio es:{promedio}, Satisfactorio")
                    satisfactorio+=1
                empleados[codigo]["evaluacion"] = {"puntualidad": puntualidad, "trabajo_equipo": trabajo_equipo,"productividad": productividad, "promedio":promedio
                                                   }
                print("\nEmpleado ingresado satisfactoriamente...")
                print("\npresione ENTER para continuar...")
                input()
            elif opcion==2:
                if len(empleados)==0:
                    print("No hay empleados registrados...")
                    print("\npresione ENTER para continuar...")
                    input()
                else:
                    codigo = input("Ingrese codigo empleado...")
                    for codigo, datos in empleados.items():
                        if codigo is empleados[codigo]:
                            print(f"Codigo de empleado: {codigo}")
                            print(f"Nombre: {datos["nombre"]}")
                            print(f"Departamento: {datos["departamento"]}")
                            print(f"Años de antiguedad: {datos["antiguedad"]}")
                            print(f"Puntualidad: {datos["evaluacion"]["puntualidad"]}")
                            print(f":Trabajo en equipo: {datos["evaluacion"]["trabajo_equipo"]}")
                            print(f"Promedio: {promedio}")
                            print(f"Numero de telefono: {datos["contacto"]["numero_telefono"]}")
                            print(f"Correo electronico: {datos["contacto"]["correo"]}")
                        else:
                            print("Empleado no encontrado, intente de nuevo...")
                print("\npresione ENTER para continuar...")
                input()
            elif opcion==3:
                if satisfactorio==0:
                    print("No hay empleados con evaluacion satisfactoria")
                else:
                    print(f"Cantidad de empleados con puntuacion satisfactoria: {satisfactorio}")
            elif opcion==4:
                mejor=-1
                ganador=""
                for promedio in empleados.items():
                    if promedio[codigo]["contacto"]["promedio"]>mejor:
                        mejor=promedio
                        ganador=promedio[codigo]["nombre"]

                print(f"El mejor promedio es: {mejor} de: {ganador}")
            elif opcion==5:
                print("Gracias por usar sistema de empleados...")
            else:
                print("Opcion no valida, intente de nuevo...")


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
    def promedio():
        promedio=(Evaluacion.__init__().puntualidad+Evaluacion.__init__().trabajo_equipo+Evaluacion.__init__().productividad)/3
        print(f"El promedio es: {promedio}")
        if promedio <=7:
            estado="Mejorar"
        else:
            estado="Satisfactorio"
        print(estado)


class Contacto:
    @staticmethod
    def __init__(self, telefono, correo):
        self.telefono=telefono
        self.correo=correo
Program.main()