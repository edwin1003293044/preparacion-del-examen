bandas=[]


#construyendo la interfaz
print("****ALTA ES TU VOZ***")
print("*********************")

opcion=100
while(opcion!=5):

    print("1.Registrar banda")
    print("2.Buscar informacion de una banda")
    print("3.Agenda del evento")
    print("4.Modeficar una banda")
    print("5.SALIR")

    opcion=int(input("digita una opcion"))
     
    if opcion==1:
       banda={}
       #creando los datos del diccionario
       banda["id"]=int(input("digite el id:"))
       banda["nombre"]=input("nombre de la banda:")
       banda["genero"]=input("Genero:")
       banda["clasificacion"]=input("clasificacion:")
       banda["tiempo"]=int(input=("Tiempo:"))
       banda["costo"]=int(input("costo: $"))

       #agregando un diccionario a una lista 
       bandas.append(banda)


    elif opcion==2:
       bandaBuscada=input("digita el  nombre de la banda que estas buscando:")
       for bandaAuxiliar in bandas:
          if bandaAuxiliar["nombre"]==bandaBuscada:
             #como lo encontre muestro los datos debandaAuxiliar
             print(f"id:{bandaAuxiliar["id"]}---nombre:{bandaAuxiliar["nombre"]}")
          else:
           print("parce siga buscando...")



    elif opcion==3:
       print(bandas)
    elif opcion==4:
      pass
    elif opcion==5:
       pass
    else:
        pass