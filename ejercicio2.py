file=open('hola.txt','r')
data=file.readlines()
file.close()
contador=0

for renglon in data:
    for palabra in renglon.split(' '):
        contador+=1
        print ('%s) %s'%(str(contador),palabra))