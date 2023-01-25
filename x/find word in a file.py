
with open("testofile.txt", "r") as f:
    lines = f.readlines()

while True:
    word = input("Inserisci una parola da cercare, premere 'q' per uscire: ")

    if word == 'q':
        print('hai selezionato \'q\', programma terminato')
        break

    found = False
    
    for i, linea in enumerate(lines):
        if word in linea:
            colonna = linea.index(word)
            print(f"parola trovata alla linea {i+1} e colonna {colonna+1}")
            found = True
            break

    if not found:
        print("Parola non presente")
    
