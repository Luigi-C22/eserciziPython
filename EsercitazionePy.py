""" Le VARIABILI """
""" Esercizio 1: Assegnazione di variabili
Crea tre variabili per rappresentare il nome, l'età e la città di una persona.
Stampa ciascuna variabile separatamente.
Cambia il valore di una variabile e ristampala """

""" nome = "Luigi"
eta = 54
citta = "Roma"

print(nome)
print(eta)
print(citta)

nome = "Giorgio"
eta = 51
citta = "Milano"

print(nome)
print(eta)
print(citta) """

""" ---------------------------------------------- """
""" Esercizio 2: Calcolatrice Base
Chiedi all'utente di inserire due numeri.
Utilizza gli operatori aritmetici per sommare, sottrarre, moltiplicare e dividere i numeri.
Stampa i risultati di ciascuna operazione. """

""" print("Inserisci dei numeri per ottenere: somma, sottrazione, moltiplicazione e divisione")
primo_numero = int(input("Inserisci il primo numero: "))
secondo_numero = int(input("inserisci il secondo numero: "))

somma = primo_numero + secondo_numero
sottrazione = primo_numero - secondo_numero
moltiplicazione = primo_numero * secondo_numero
divisione = primo_numero / secondo_numero

print("La somma di ", primo_numero, " + ",secondo_numero, "è:", somma)
print("La sottrazione di", primo_numero, " - ", secondo_numero, "è:", sottrazione)
print("La moltiplicazione di ", primo_numero, " x ", secondo_numero,  "è:", moltiplicazione)
print("La divisione di ", primo_numero, " / ", secondo_numero, "è:", divisione) """


""" -------------------------------------------------------- """
""" Esercizio 3: Saluto perosnalizzato
Chiedi all'utente di inserire il proprio nome.
Utilizza print() per creare un saluto personalizzato.
Esempio di output: "Ciao alice! Benvenuto/a!"  """

""" print("Dimmi come ti chiami....")
nome = input("Inserisci il tuo nome: ")
print("Ciao", nome, "! Benvenuto/a nell'esercizio 3!") """

""" -------------------------------------------------------- """
""" Esercizio 4: Formattazione di una stringa
Chiedi all'utente di inserire il proprio nome e cognome.
Concatenali e stampa il nome completo in maiuscolo.
Utilizza il metodo .lower() per stampare il nome completo in minuscolo. """

""" print("Per favore segui le istruzioni:")
nome = input("Inserisci il tuo nome:")
cognome = input("Inserisci il tuo cognome: ")
nome_completo = nome + " " + cognome
print("Ti chiami: ", nome_completo.upper())
print("Il tuo nome in minuscolo è: ", nome_completo.lower()) """

""" ----------------------------------------------------- """

""" Esercizio 5: Creazione di una mini calcolatrice
Chiedi all'utente di inserire due numeri.
Fornisci un menù per scegliere un'operazione: somma, sottrazione, moltiplicazione o divisione.
Esegui l'operazione selezionata e mostra il risultato.
Gestisci eventuali errori, come la divisione per zero. """

""" print("CALCOLATRICE")
print("Devi inserire i numeri e poi scegliere l'operazione da eseguire")
operatore = input("Scegli quale operazione eseguire tra: +, -, *, / : ")


if operatore != "+" and operatore != "-" and operatore != "*" and operatore != "/":
    print("Scegli un operatore valido!!")
    operatore = input("Scegli quale operazione eseguire tra: +, -, *, / :")
if operatore == "+":
        print("hai scelto ", operatore)
elif operatore == "-":
        print("hai scelto ", operatore)
elif operatore == "*":
        print("hai scelto ", operatore)
elif operatore == "/":
        print("hai scelto ", operatore)

primo_numero = int(input("Primo numero: "))
secondo_numero = int(input("Secondo numero: "))


if secondo_numero == 0 and operatore == "/":
    print("Non puoi dividere per zero")
else:
    if operatore == "+":
        print("La somma di", primo_numero, "+", secondo_numero, "è:", primo_numero + secondo_numero)
    elif operatore == "-":
        print("La sottrazione di", primo_numero, "-", secondo_numero, "è:", primo_numero - secondo_numero)
    elif operatore == "*":
        print("La moltiplicazione di", primo_numero, "x", secondo_numero, "è:", primo_numero * secondo_numero)
    elif operatore == "/":
        print("La divisione di", primo_numero, "/", secondo_numero, "è:", primo_numero / secondo_numero)
    else:
        print("Operazione non valida") """

""" ---------------------------------------------------- """
""" ---------------------------------------------------- """