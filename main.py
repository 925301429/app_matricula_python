"""
- registrar alos alumnos.
- generar fichaa de matricula
- mostrar las listas de todoslos matriculados
- filtrar matriculados por programa de estudio

"""
lista_alumnos=[]
def mensaje_menu():
    menu_opciones="""
        --------bienvenidos al sistema-------
            ----Registra tu alumno-----
    1.Escribe (s) si deceas agregar un nuevo alumno
    2.Escribe (n) si deceas salir del sistema
    Escribe la accion que decea realiza:"""      
    return menu_opciones 

def ingresar_datos_alumnos()
    id=len(lista_alumnos)+1
    cui=int(input("ingrese el numero de su dni:")) 
    nombre=input("ingrese elnombre delalumno:")
    apellido=input("ingrese el apellido del alumno:")
    numero_celular=int(input("ingrese su numero de celular:"))
    programa_estudio=imput("ingrese su ciclo academico:")
    ciclo_academico=input("ingrese su ciclo academico:")
    email=input("ingrese su correo electronico:")
def guarda_datos_alumno(id,cui,nombre,apellido,numero_celular,programa_estudio,ciclo_academico,email):
    alumnos={
        "id":id,
        "cui":cui,
        "nombre":nombre,
        "apellido":apellido,
        "numero_celular":numero_celular,
        "programa_estudio":programa_estudio,
        "ciclo_academico":ciclo_academico,
        "email":email
    }
while True:
    menu_opciones=input(mensaje_menu())
    if menu_opciones.lower() == "n":
        print("saliendo del sistema  ")
        break
    elif menu_opciones.lower() == "s":
        ingresar_datos_alumnos()
    else:
        print("opciones erroneas")
print (lista_alumnos)


