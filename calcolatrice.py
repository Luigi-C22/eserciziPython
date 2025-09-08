hello_message = """
Benvenuti al programma calcolatrice!

Di seguito un elenco delle varie funzioni disponibili:

- Per effettuare un'Addizione  seleziona 1;
- per effettuare una Sottrazione seleziona 2;
- per effettuare una Moltiplicazione seleziona 3;
- per effettuare una Divisione seleziona 4;
- per effettuare un Calcolo Esponenziale seleziona 5;
- per effetuare una Radice Quadrata seleziona 6;

- per uscire dal programma digitare ESC;
"""


while True:
    print(hello_message)

    action = input("Inserisci il numero corrispondente all'operazione da effettuare: ")

    if action == "1":
        print("\nHai scelto: Addizione\n")
        a = float(input("Inserisci il primo numero -> "))
        b = float(input("inserisci il secondo numero -> "))
        print("Il risultato dell'addizione è:", str(a+b))
    elif action =="2":
        print("\nHai scelto: Sottrazione\n")
        a = float(input("Inserisci il primo numero -> "))
        b = float(input("inserisci il secondo numero -> "))
        print("Il risultato della sottrazione è:", str(a-b))
    elif action == "ESC" or action =="esc":
        print("\nL'applicazione verrà chiusa!\n")
        break

    new_action = input("\nDesideri continuare ad utilizzare l'Applicazione? S/N ")
    if new_action == "S" or new_action == "s":
        print("Sto tornando al menù principale!\n")
        continue
    else:
        print("A presto!\n")
        break