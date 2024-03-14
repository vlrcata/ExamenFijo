import random

bandas = []
opcion = 100

while opcion != 5:
    print("*** Festival Altavoz ***")
    print("------------------------")
    print("1. Registrar Banda")
    print("2. Ver el cartel del festival")
    print("3. Buscar Banda")
    print("4. Modificar Banda")
    print("5. Finalizar")

    try:
        opcion = int(input("Digita una opción: "))

        if opcion == 1: 
            banda = {}
            banda["idBanda"] = random.randint(10000, 99999)
            banda["nombreBanda"] = input("Digite el nombre de su banda: ")
            banda["generoBanda"] =input("Digite el genero de su banda: ")
            banda["clasificacionBanda"] =input("Digite la clasificacion de su banda: ")
            banda["costoBanda"]=int(input("Digite el costo de su banda: "))
            banda["tiempoBanda"]=int(input("Digite el tiempo que tocara su banda: "))
            print(banda)
            bandas.append(banda)
           

        elif opcion == 2:
           #print(bandas)
            print("*** Estas son las maravillosas bandas que asistiran ***")
              
            for bandaAuxiliar in bandas:
                print(f"{bandaAuxiliar["idBanda"]}---{bandaAuxiliar["nombreBanda"]}") 

        elif opcion == 3:
           #BUSCANDO UN ELEMENTO DENTRO DE UNA LISTA
            bandaBuscada = input("Digite la banda que quiere buscar")

            for bandaAuxiliar in bandas:
                if bandaAuxiliar["nombreBanda"]==bandaBuscada:
                   print("La banda buscada si va tocar en Altavoz, compra la boletaaa")
                else:
                   print("Esa banda no esta registrada aun")

        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        else: 
            print("Error: Concentradit@, opcion invalida")

    except ValueError:
        print("Error: Por favor, ingresa solo números.")
   
    