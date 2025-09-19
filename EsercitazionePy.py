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


""" STRUTTURE DI CONTROLLO """
""" ---------------------------------------------------- """
""" ESERCIZIO 1: Verifica della maggiore età
Chiedi all'utente di inserire la sua età.
Se l'età è inferiore a 18, stampa "Sei minorenne".
Se l'età è uguale a 18, stampa "Hai appena compiuto 18 anni!".
Altrimenti , stampa "Sei maggiorenne!" """

""" print("Verifichiamo se puoi bere alcolici!")
eta = int(input("Quanti anni hai? "))
if eta > 18 :
  print("Sei già maggiorenne da un po'")
elif eta == 18 :
  print("Ok.Sei appena diventato maggiorenne ")
else :
  print("Mi spiace, ma sei ancora minorenne")

print("avere", eta, "anni è un bel periodo della vita") """

""" --------------------------------------------------- """

""" Esercizio 2: Somma dei numeri da 1 a N
Chiedi all'utente di inserire un numero positivo N
Utilizza un ciclo for per calcolare la somma di tutti i numeri da 1 a N
Stampa il risultato """

""" print("CALCOLIAMO LA SOMMA DI UNA SEQUENZA")

N = int(input("Inserisci un numero positivo che vuoi: "))
while N <= 0 :
  print("Non fare il furbo!! Il numero deve essere positivo!")
  N = int(input("Inserisci un numero positivo che vuoi: "))

somma = 0  # Initializza la somma
for i in range(1, N + 1):  # Ripete 1 fino a N (compreso)
  somma = somma + i
print("La somma dei numeri da 1 a", N, "è:", somma) """

""" ------------------------------------------------- """

""" Esercizio 3: Indovina il numero
Genera un numero casuale tra 1 e 10 (usa la libreria random).
Chiedi all'utente di indovinare il numero.
Continua a chiedere finche l'utente non indovina il numero corretto.
Stampa il numero di tentativi. """

""" print("GIOCO DELL'INDOVINA IL NUMERO")
import random
tentativi = 1
numero = random.randint(1,10)
tentativo = int(input("Indovina il numero che ho in mente: "))
while tentativo != numero :
  tentativi = tentativi + 1
  print("Tentativo n. ", tentativo,"Hai sbagliato! Il numero non è questo! Riprova:")
  tentativo = int(input("Indovina il numero che ho in mente: "))

print("Complimenti hai indovinato in", + tentativi,  "tentativi!! Era proprio il numero:", numero)"""


""" ------------------------------------------------- """

""" Esercizio 4: Tavola Pitagorica
Utilizza un ciclo for nidificato per creare una tavola pitagorica (tabellina).
Stampa la moltiplicazione tra i numeri da 1 a 10 """

""" print("Tavola Pitagorica - Moltiplicazioni da 1 a 10")
print("-" * 40)

for i in range(1, 11):         # i va da 1 a 10
    for j in range(1, 11):     # j va da 1 a 10
        print(f"{i} x {j} = {i * j}")
    print("-" * 25)  # Separatore tra le tabelline (opzionale) """

""" ----------------------------------------------------------- """

""" Esercizio 5: Controllo Pari e Dispari
Chiedi all'utente di inserire un numero positivo N
Utilizza un ciclo for per stampare tutti i numeri da 1 a N, 
ma utilizza continue per saltare i numeri dispari """

""" print("Controllo numeri pari e dispari")

N = int(input("Inserisci un numero positivo: "))
for numero in range(1, N + 1):
  if numero == N +1 :
    break
  elif numero % 2 == 1:
    continue
  print(numero) """
  
""" -------------------------------------------------- """

""" Esercizio 6: Gioco del numero magico
Genera un numero casuale tra 1 e 100
Chiedi all'utente di indovinare il numero.
Dopo ogni tentativo, fornisci un feedback: se il numero è più alto o più basso.
Utilizza while per continuare fino a quando l'utente indovina.
Usa break per terminare il ciclo una volta che il numero è stato indovinato.
Stampa il numero di tentativi. """

""" print("GIOCO DEL NUMERO MAGICO tra 1 e 100")
import random
numero_magico = random.randint(1, 100)

tentativi = 1
n = int(input("Prova ad indovinare il numero magico: "))
if n <= 0 or n > 100:
  print("Non valido! Il numero deve essere compreso tra 1 e 100")
  n = int(input("Prova ad indovinare il numero magico: "))
while n == numero_magico:
  
  break
while n != numero_magico:
  if n < numero_magico:
    print("Sbagliato! Il numero è più alto")
  else:
    print("Sbagliato! Il numero è più basso")
     
  print("tentativo n° ", tentativi)
  n = int(input("Prova ad indovinare il numero magico: "))
  
  tentativi = tentativi + 1
  continue
print("Complimenti!! Bravo, ha indovinato in ", tentativi, "tentativi!!") """


""" ---------------------------------------------------------------------- """

""" ---------------------------------------------------------------------- """

""" FUNZIONI E MODULARITA' """
""" Esercizio 1: Funzione di benvenuto
Definisci una funzione chiamata benvenuto() che stampa il messaggio "Benvenuto al corso di Python"
Chiama la funzione per visualizzare il messaggio """

""" def benvenuto():
  print("Benvenuto al corso di Python")

benvenuto() """

""" --------------------------------------------------------------------- """
#test
""" totale = int(input("numero: "))

def saluta_utente(pollo):
  print("ciao ", pollo + 11)

saluta_utente(totale) """

""" --------------------------------------------------------------------- """

""" Esercizio 2: Somma di due numeri
Definisci una funzione chiamata Somma che accetta due parametri a e b
La funzione deve calcolare la somma di a e b e restituire il risultato.
Chiama la funzione con due numeri a tua scelta e stampa il risultato. """

"""print("Stampa di due numeri")

a = int(input("Inserisci un numero: "))
b = int(input("Inserisci un altro numero:"))

def somma(a,b):
  somma = a + b
  
  print("hai inserito i numeri", a, " e ", b)
  return somma

print("La somma dei tuoi numeri è: ", somma(a,b)) """

""" -------------------------------------------------------------------- """

""" Esercizio 3: Calcolo dell'area di un rettangolo
Definisci una funzione area_rettangolo che accetta la base e l'altezza come parametri.
La funzione deve calcolare e restituire l'area del rettangolo.
Chiedi all'utente di inserire i valori di base e altezza, calcola l'area e stampa il risultato. """

""" print("Calcoliamo l'area di un rettangolo")

base = int(input("Inserisci la misura della base: "))
altezza = int(input("inserisci la misura dell'altezza: "))

def area_rettangolo(base,altezza):
  area = base * altezza
  print("La base è: ", base, "e l'altezza è: ", altezza)
   
  return area

print("L'area del rettangolo, data la base ", base, "e l'altezza ", altezza, "è: ", area_rettangolo(base,altezza)) 

 """

""" -------------------------------------------------------------------------- """
""" Esercizio 4: Differenza tra scope locale e globale
Crea una variabile numero globale
Crea una funzione modifica_numero che modifica numero all'interno della funzione
Stampa il valore di numero prima e dopo la chiamata alla funzione per vedere come cambia """

""" print("Differenze tra scope locale e scope globale.")

numero = 15
def modifica_numero():
   global numero
   numero = numero + 54
  

print(f"La variabile 'numero' globale è: {numero}")
modifica_numero()
print(f"la variabile 'numero' modificata nella funzione, quindi locale è: {numero}") """

""" ------------------------------------------------------------------------------ """
""" Esercizio 5: Funzione lambda per il calcolo del prodotto
Definisci una funzione lambda per calcolare il prodotto di sue numeri.
Chiedi all'utente di inserire due numeri e utilizza la funzione lambda per calcolare il prodotto
Stampa il risultato """

""" print("Utilizzo della funzione LAMBDA")

prodotto = lambda x,y : x * y

numero_a = float(input("inserisci un il primo numero: "))
numero_b = float(input("inserisci il secondo numero: "))
print(f"Hai scelto i numeri {numero_a} e {numero_b}")

print(f"Il prodotto è: {prodotto(numero_a, numero_b)}") """

""" -------------------------------------------------------------------------- """

""" Esercizio 6: Calcolatrice con funzioni modulari
Crea funzioni per eseguire le operazioni di base: somma, sottrazione, moltiplicazione e divisione.
Crea una funzione principale calcolatrice che chiede all'utente di scegliere un'operazione e di inserire due numeri.
Usa le funzioni per calcolare e stampare il risultato in base alla scelta dell'utente. """

""" print("CALCOLATRICE CON FUNZIONI MODULARI")

def somma(a,b):
  somma = a + b
  return somma

def sottrazione(a,b):
  sottrazione = a - b
  return sottrazione

def moltiplicazione(a,b):
  moltiplicazione = a * b
  return moltiplicazione

def divisione(a,b):
  if b == 0:
    print("Non puoi dividere per zero")
    return None
  divisione = a / b
  return divisione

def calcolatrice():
  operazione = input("Scegli l'operazione tra: +, -, *, /: ")
  numero_a = float(input("Inserisci il primo numero: "))
  numero_b = float(input("Inserisci il secondo numero: "))

  if operazione == "+":
    risultato = somma(numero_a, numero_b)
    print(f"Il risultato dell'addizione è: {risultato}")
    return somma(numero_a, numero_b)

  elif operazione == "-":
    risultato = sottrazione(numero_a, numero_b)
    print(f"Il risultato della sottrazione è: {risultato}")
    return sottrazione(numero_a, numero_b)
    
  elif operazione == "*":
    risultato = moltiplicazione(numero_a, numero_b)
    print(f"Il risultato della moltiplicazione è: {risultato}")
    return moltiplicazione(numero_a, numero_b)
    

  elif operazione == "/":
    risultato = divisione(numero_a, numero_b)
    print(f"Il risultato della divisione è: {risultato}")
    return divisione(numero_a, numero_b)
    
  else:
    print("Operazione non valida")

(calcolatrice()) """

""" ----------------------------------------------------------------------- """
""" ----------------------------------------------------------------------- """

""" STRUTTURE DATI (LISTE, TUPLE, DIZIONARI E SET) """
""" ----------------------------------------------------------------------- """
""" Le Liste """
""" Esercizio 1: Creazione e Modifica di una lista
Crea una lista di tre elementi rappresentanti nomi di animali.
Aggiungi un altro animale alla lista.
Rimuovi il primo animale dalla lista.
Stampa la lista aggiornata """

""" print("Creo un LISTA di animali")

animali = ["zebra", "cavallo", "leone", "gallina", "echidna"]
print("lista di animali originale: ", animali)

animali.append("giraffa")
print("Lista di animali dopo aver usato  append", animali)

animali.pop(0)
print("Lista di animali dopo aver usato pop", animali) """

""" ------------------------------------------------------------ """

""" Esercizio 2: Lavorare con le Tuple
Crea una Tupla con tre colori.
Stampa il secondo colore nella Tupla
Tenta di aggiungere un nuovo colore e nota l'errore per capire l'immutabilità delle Tuple """

print("creo una Tupla con 3 colori")

colori = ("rosso", "verde", "marrone")
print(colori[1])

# colori.append("giallo") # Questo causerà un errore perché le tuple sono immutabili
print("Le tuple sono immutabili, non è possibile aggiungere elementi dopo la creazione.")