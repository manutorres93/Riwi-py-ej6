#ALGORITMO PARA ESTUDIANTES
def create ():
    students_list=[]
    notes_list=[]
    cant= int (input("Ingrese la cantidad de estudiantes: "))

    for x in range (cant):
        students_list.append(input("Digite el nombre del estudiante: "))
        notes_list.append(float(input("Digite la nota del estudiante ingresado: ")))
    
    return students_list, notes_list

def show_students(st_ls):
    for x in range (len(st_ls)):
        print(f"ID {x+1}:",st_ls[x])

def show_notes(nt_ls):
    for x in range (len(nt_ls)):
        print(f"ID {x+1}:",nt_ls[x])


init=-1

while init!=0:
    
    print("--------MENU------")
    print("1. Crear la lista de estudiantes con sus notas")
    print("2. Mostrar la lista de estudiantes")
    print("3. Mostrar la lista de notas")
    # print("4. Agregar un elemento en el final ")
    # print("5. Eliminar el último elemento")
    # print("6. Eliminar el elemento deseado")
    # print("7. Organizar en orden ascendente")
    # print("8. Organizar en orden descendente")

    option= int(input("digite la opción deseada: "))

    if option==1:
        list_st_nt= create()
        
        st_ls= list_st_nt[0]
        nt_ls=list_st_nt[1]

    if option==2:
        show_students(st_ls)
    
    if option ==3:
        show_notes(nt_ls)
