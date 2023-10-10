#ALGORITMO PARA ESTUDIANTES
def create_students ():
    students_list=[]
    notes_list=[]
    ages_list=[]
    cant= int (input("Ingrese la cantidad de estudiantes: "))

    for x in range (cant):
        students_list.append(input("Digite el nombre del estudiante: "))
        name= students_list[x]

        note_1= float(input(f"Digite la nota 1 del estudiante {name} "))
        note_2= float(input(f"Digite la nota 2 del estudiante {name} "))
        note_3= float(input(f"Digite la nota 3 del estudiante {name} "))

        prom= (note_1+note_2+note_3)/3
     
        notes_list.append(prom)

        ages_list.append(int(input(f"Digite la edad del estudiante {name}: ")))
       
    return students_list, notes_list, ages_list


def show_students(st_ls):
    for x in range (len(st_ls)):
        print(f"ID {x+1}:",st_ls[x])


def show_notes(nt_ls):
    for x in range (len(nt_ls)):
        print(f"ID {x+1}:",nt_ls[x])

def show_ages(ages_ls):
    for x in range (len(ages_ls)):
        print(f"ID {x+1}:",ages_ls[x])

def add_info ():
    
    cant= int (input("Ingrese la cantidad de estudiantes que quiere agregar: "))

    for x in range (cant):
        st_ls.append(input("Digite el nombre del estudiante: "))
        name= st_ls[-1]

        note_1= float(input(f"Digite la nota 1 del estudiante {name} "))
        note_2= float(input(f"Digite la nota 2 del estudiante {name} "))
        note_3= float(input(f"Digite la nota 3 del estudiante {name} "))

        prom= (note_1+note_2+note_3)/3
     
        nt_ls.append(prom)

        ages_ls.append(int(input(f"Digite la edad del estudiante {name}: ")))
       


init=-1

while init!=0:
    
    print("--------MENU------")
    print("1. Crear la lista de estudiantes con sus edades y notas")
    print("2. Mostrar la lista de estudiantes")
    print("3. Mostrar la lista de notas")
    print("4. Mostrar la lista de edad ")
    print("5. Agregar información de un estudiante")
    # print("6. Eliminar el elemento deseado")
    # print("7. Organizar en orden ascendente")
    # print("8. Organizar en orden descendente")

    option= int(input("digite la opción deseada: "))

    if option==1:
        list_st_nt= create_students()
        
        st_ls= list_st_nt[0]
        nt_ls=list_st_nt[1]
        ages_ls=list_st_nt[2]

    elif option==2:
        show_students(st_ls)

    elif option ==3:
        show_notes(nt_ls)

    elif option ==4:
        show_ages(ages_ls)
    
    elif option ==5:
        add_info()
