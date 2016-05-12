def leertxt():
    archi=open('leer.txt','r')
    linea=archi.readline()
    while linea!="":
        print (linea)
        linea=archi.readline()
    archi.close()
leertxt()
		
