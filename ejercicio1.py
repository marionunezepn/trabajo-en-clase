frases=str(input('ingrese frase'))
frase=frases.split(" ")
for i in range(1,len(frase)+1):
	palabra=len(frase[i].split(" "))
	print ("frase",i,":",palabra)