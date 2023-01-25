


file=open("proverbio.txt", 'w')


file.write('''Botte piccola fa buon vino.
Brutta di viso, sotto il paradiso.
Brutto in fasce bello in piazza.
Buon sangue non mente.
Buon seme dà buoni frutti.
Buon vino fa buon sangue.
Buon tempo e mal tempo non dura tutto il tempo.
''')

file=open("proverbio.txt", 'r')
filepari=open("file_proverbio_pari.txt", 'w')
filedispari=open("file_proverbio_dispari.txt",'w')

for i, item in enumerate(file):
    if i%2==0:
        
        filepari.write(str(i)+" "+item)
    else:
        
        filedispari.write(str(i)+" "+item)

        
# print(f"file originale\n{i} {item}\nfile pari")

file.close()
filepari.close()
filedispari.close()
