<<<<<<< HEAD
def leertxt():
    archi=open('leer.txt','r')
    linea=archi.readline()
    palabra=''
    contador=0
    while linea!="":
        print (linea)
        contador=contador+1
        for i in range (len(linea)):
        	if(linea[i]==' '):
        		contador = contador + 1	
        print(contador)		
        linea=archi.readline()
    archi.close()
    return contador	
palabra=leertxt()

print('encontro: '+str(palabra)+' palabras')
=======
file=open('hola.txt','r')
data=file.readlines()
file.close()
contador=0

for renglon in data:
    for palabra in renglon.split(' '):
        contador+=1
        print ('%s) %s'%(str(contador),palabra))
>>>>>>> origin/master
