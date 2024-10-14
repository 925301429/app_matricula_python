"""
- registrar alos alumnos.
- generar fichaa de matricula
- mostrar las listas de todoslos matriculados
- filtrar matriculados por programa de estudio
"""
lista_alumnos=[]
#inicio del ptoblema
#necesito ´poder ageregar mas alumnos sin necesidad de crear tantas variables
#posible solucion cree o encerrar el codigoen un ciclo while

nombre=input("Ingrese el nombre del alumno: ")
apellido=input("Ingrese el apellido del alumno: ")
nombre2=input("Ingrese el nombre del alumno: ")
apellido2=input("Ingrese el apellido del alumno: ")
alumnos={
    "nombre" :nombre,
    "apellido" :apellido
}
alumnos2={
    "nombre" :nombre2,
    "apellido" :apellido2
}
lista_alumnos.append(nombre)
lista_alumnos.append(apellido2)
# fin delproblema
# deceo mostrar un menu con las opciones de agregar un menu alumno y salir del programa                                 
print(lista_alumnos)
