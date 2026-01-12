"""PROGRAMMAZIONE ORIENTATA AGLI OGGETTI (OOP)"""

#Esempio di classe e oggetto
""" class Persona:
  def __init__(self,nome,eta,sesso,qualita):
    self.nome = nome
    self.eta = eta
    self.sesso = sesso
    self.qualita = qualita

  def saluta(self):
    print(f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni e sono {self.sesso} e sono {self.qualita}")

#creazione di un oggetto
persona1 = Persona("Alice", 30, "Femmina", "intelligente")
persona1.saluta()
 """

""" ------------------------------------------------------------------------------ """

###Esercizio 1: Creazione di una classe
#### Crea una classe Animale con un costruttore (__init__) che accetti un nome e una specie.
#### Aggiungi un metodo descrivi che stampi il nome e la specie dell'animale.
#### Crea una istanza della classe Animale e chiama il metodo descrivi.

""" class Animale:
  def __init__(self, nome, specie):
    self.nome = nome
    self.specie = specie

  def descrivi(self):
    print(f"L'animale si chiama: {self.nome} ed è della specie {self.specie}")

animale = Animale("Lippo lappo", "cane oriundo")
animale.descrivi() """

""" ------------------------------------------------------------------------------ """
#Esercizio 2: Creazione di attributi e metodi
""" Crea una classe Libro con attributi titolo e autore.
Aggiungi un metodo descrizione che stampi il titolo e l'autore del libro.
Crea un'istanza della classe Libro e chiama il metodo descrizione. """
""" class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
    
    def descrizione(self):
        print(f"{self.titolo} scritto da {self.autore}")

libro = Libro("Il Signore degli Anelli", "J.R.R. Tolkien")
libro.descrizione() """

""" ------------------------------------------------------------------------------ """
#Esempio di attributo privato
"""Esercizio 3: Incapsulamento con attributi privati
Crea una classe ContoBancario con un attributo privato saldo.
Aggiungi metodi deposita e mostra_saldo.
Crea un'istanza della classe e verifica il funzionamento dei metodi"""

""" class ContoBancario:
  def __init__(self, saldo):
     self.__saldo = saldo
  
  def deposita(self, importo):
     self.__saldo += importo

  def mostra_saldo(self):
     print(f"saldo: {self.__saldo}")

conto = ContoBancario(1000)
conto.deposita(500)
conto.mostra_saldo()  # Output: saldo: 1500
 """
""" ------------------------------------------------------------------------------  """
#Esempio di ereditarietà

""" class Animale:
    def __init__(self, nome):
        self.nome = nome
    
    def parla(self):
        pass

class Cane(Animale):
    def parla(self):
        print("Bau Bau")

class Gatto(Animale):
    def parla(self):
        print("Miao Miao")

fido = Cane("Fido")
fido.parla()  # Output: Bau Bau

micio = Gatto("Micio")
micio.parla()  # Output: Miao Miao """

""" ------------------------------------------------------------------------------ """

""" Esercizio 4: Ereditarietà

Crea una classe Veicolo con un attributo marca e un metodo descrizione.

Crea una sottoclasse Auto che eredita da Veicolo e aggiunge un metodo tipo
   che stampa "Questa è un'auto".

   Crea un'istanza della classe Auto e chiama i metodi descrizione e tipo. """
""" class Veicolo:
    def __init__(self, marca):
        self.marca = marca
    def descrizione(self):
        pass

class Auto (Veicolo):
    def tipo(self):
        print("Questa è un'auto")

auto = Auto("Toyota")
auto.descrizione()
auto.tipo()  """ # Output: Questa è un'auto """

""" ------------------------------------------------------------------------------ """

""" Esempio di Polimorfismo"""
""" class Forma:
  def area(self):
    pass

class Rettangolo(Forma):
  def __init__(self, larghezza, altezza):
      self.larghezza = larghezza
      self.altezza = altezza
    
  def area(self):
      return self.larghezza * self.altezza
  
class Cerchio(Forma):
  def __init__(self, raggio):
      self.raggio = raggio

  def area(self):
      return 3.14 * (self.raggio ** 2)
  
forme = [Rettangolo(4, 5), Cerchio(3)]
for forma in forme:
  print(f"L'area è: {forma.area()}")
   """


""" ------------------------------------------------------------------------------ """

""" Esercizio 5: Polimorfismo con classi """
""" Crea una classe Animale con un metodo suono.
Crea due sottoclassi, Cane e Gatto, che ridefiniscono  il metodo suono per stampare 
          rispettivamente 'Woof' e ' Meow'.
Crea un'istanza  di entrambe le classi e chiama il metodo suono. """

""" class Animale:
    def suono(self):
        pass
    
class Cane(Animale):
        def suono(self):
            print("Woof")

class Gatto(Animale):
     def suono(self):
          print("Meow")

cane = Cane()
cane.suono()
gatto = Gatto()
gatto.suono()
 """
""" ----------------------------------------------------------------------------------- """    

#PROGETTO FINALE: GESTIONE DI UN SISTEMA DI BIBLIOTECA
""" Esercizio 6: Sistema di Biblioteca
Crea una classe Libro con attributi titolo, autore e disponibile.
Crea una classe Biblioteca con un attributo catalogo che è una lista di libri.
Aggiungi metodi aggiungi_libro, presta_libro e restituisci_libro per gestire il catalogo.
Crea un'istanza della biblioteca e aggiungi alcuni libri.
Presta e restituisci un libro, aggiornando la disponibilità."""

""" class Libro():
     def __init__ (self, titolo, autore):
          self.titolo = titolo
          self.autore = autore
          self.disponibile = True

class Biblioteca():
    def __init__(self):
         self.catalogo = []
    
    
    def aggiungi_libro(self, libro):
         self.catalogo.append(libro)
    
    
    def presta_libro(self, titolo):
         for libro in self.catalogo:
              if libro.titolo == titolo and libro.disponibile:
                   libro.disponibile = False
                   print(f"Hai prestato il libro: {titolo}")
                   return
         print(f"Il libro {titolo} non è disponibile.")
    
    
    def restituisci_libro(self, titolo):
         for libro in self.catalogo:
              if libro.titolo == titolo and not libro.disponibile:
                   libro.disponibile = True
                   print(f"Hai restituito il libro: {titolo}")
                   return
         print(f"Il libro {titolo} non è stato prestato.")


biblioteca = Biblioteca()
libro1 = Libro("1984", "George Orwell")
libro2 = Libro("Il Grande Gatsby", "F. Scott Fitzgerald")
libro3 = Libro("To Kill a Mockingbird", "Harper Lee")

biblioteca.aggiungi_libro(libro1)
biblioteca.aggiungi_libro(libro2)
biblioteca.aggiungi_libro(libro3)

biblioteca.presta_libro("1984")
biblioteca.restituisci_libro("1985")    #Libro non prestato
biblioteca.presta_libro("Il Grande Gatsby")
biblioteca.restituisci_libro("Il Grande Gatsby")
biblioteca.presta_libro("Moby Dick")  # Libro non disponibile
biblioteca.presta_libro("Orgoglio e pregiudizio") # Libro non disponibile """

""" <------------------------------------------------------------------------------------------------- """
# Esempio di letture di un file
""" with open("file_di_testo.txt", "r") as file:
    contenuto = file.read()
    print(contenuto) """
""" ------------------------------------------------------------------------------ """
# Esercizio 1: Lettura di un file di testo""" 
""" 
Crea un file di testo saluti.txt contenente alcuni saluti in diverse lingue.
Scrivi un programma che legge il contenuto del file e lo stampa a schermo. """

""" with open("saluti.txt", "r") as file:
    contenuto = file.read()
    print(contenuto)
 """
""" ------------------------------------------------------------------------------ """
#Esempio di scrittura file
""" with open("output.txt",  "w") as file:
    file.write("Ciao mondo\n")
    file.write("Questo è un file di testo") """

""" ------------------------------------------------------------------------------ """
#Esercizio 2: Scrittura di un file di testo
"""Scrivi un programma che chiede all'utente di inserire il proprio nome.
Il programma deve salvare il nome in un file nomi.txt.
Ogni nome deve essere aggiunto in una nuova riga, senza cancellare quelli esistenti."""

""" with open("nomi_utenti.txt", "a") as file:
    nome = input("Inserisci il tuo nome: ")
    file.write(nome + "\n") """

""" ------------------------------------------------------------------------------ """

#Esempio di lettura riga per riga
""" with open("file_di_testo.txt", "r") as file:
    for riga in file:
        print(riga.strip()) """
""" ------------------------------------------------------------------------------ """

#Esercizio 3: Contatore di Linee
"""Crea un file documento.txt con alcune righe di testo.
Scrivi un programma che legge il file e conta il numero di righe."""
""" with open("documento.txt", "r") as file:
    conta_righe = sum(1 for riga in file)
    print(f"Il numero di righe nel file è: ", conta_righe)
 """
""" ------------------------------------------------------------------------------ """
#Esempio di gestione delle eccezioni
""" try:
    with open("file_inesistente.txt", "r") as file:
        contenuto = file.read()
        print(contenuto)
except FileNotFoundError:
    print("Errore: Il file non esiste.")"""

""" ------------------------------------------------------------------------------ """
#Esercizio 4: Gestione degli errori durante la lettura
"""Scrivi un programma che tenta di aprire un file dati.txt.
Se il il file non esiste, il progranna deve stampare "Il file non è stato trovato." """
""" try:
    with open ("dati.txt", "r") as file:
        contenuto = file.read()
        print(contenuto)
except FileNotFoundError:
    print("Il file non è stato trovato.") """

""" ------------------------------------------------------------------------------ """

#File CSV
"""Esempio di lettura di un file CSV"""
""" import csv
with open("dati.csv", "r") as file:
    lettore_csv =csv.reader(file)
    for riga in lettore_csv:
        print(riga)
 """
""" ------------------------------------------------------------------------------ """
#Esercizio 5: Lettura di un file CSV
"""Crea un file studenti.csv contenente i nomi e le età di alcuni studenti.
Scrivi un programma che legge il file e stampa i dati di ogni studente."""

""" import csv
with open("studenti.csv", "r") as file:
    contenuto_csv = csv.reader(file)
    for riga in contenuto_csv:
        print(f"Nome: {riga[0]}  Età: {riga[1]}") """
        
""" ------------------------------------------------------------------------------ """
#Esempio di scrittura di un file CSV
""" import csv
dati = [["Nome", "Età"], ["Alice", 22], ["Bob", 25]]

with open("output.csv", "w", newline="")as file:
    scrittore_csv = csv.writer(file)
    scrittore_csv.writerows(dati)
 """
""" ------------------------------------------------------------------------------ """
#Esercizio 6: Scrittura di dati in unn file CSV
"""Crea una lista di dizionari, dove ogni dizionario 
           rappresenta uno studente con "nome" e "età".
Scrivi un programma che salva questi dati in un file studenti.csv, 
           dove ogni riga rappresenta uno studente."""

""" import csv
studenti = [["nome", "età"], ["Carletta", 23], ["Davidino", 24], ["Elenuccia", 21]]
with open("studenti.csv", "w", newline="") as file:
    scrittore_csv = csv.writer(file)
    scrittore_csv.writerows(studenti) """

""" ------------------------------------------------------------------------------ """
#Progetto finale: Sistema di Registrazione delle Vendite
#Esercizio 7: Sistema di Registrazione delle Vendite
""".Crea un programma che chiede all'utente di inserire prodotto, quantità e prezzo.

   .Salva ogni registrazione nel file vendite.csv, con una riga per ogni vendita.

   .Aggiungi un'opzione per visualizzare tutte le vendite presenti nel file."""

""" import csv
def registra_vendita():
    prodotto = input("Inserisci il nome del prodotto: ")
    quantita = input("Inserisci la quantità venduta: ")
    prezzo = input("Inserisci il prezzo del prodotto: ")
    
    with open("vendite.csv", "a", newline="") as file:
        scrittore_csv = csv.writer(file)
        scrittore_csv.writerow([prodotto, quantita, prezzo])
    print("Vendita registrata con successo.")

def visualizza_vendite():
    try:
        with open("vendite.csv", "r") as file:
            lettore_csv = csv.reader(file)
            print("Prodotto | Quantità | Prezzo")
            for riga in lettore_csv:
                print(f"{riga[0]} | {riga[1]} | {riga[2]}")
    except FileNotFoundError:
        print("Nessuna vendita registrata.")
while True:
    print("1. Registra una vendita")
    print("2. Visualizza tutte le vendite")
    print("3. Esci")
    scelta = input("Scegli un'opzione (1-3): ")
    
    if scelta == "1":
        registra_vendita()
    elif scelta == "2":
        visualizza_vendite()
    elif scelta == "3":
        print("Uscita dal programma.")
        break
    else:
        print("Opzione non valida. Riprova.") """

""" ------------------------------------------------------------------------------ """
# La libreria Math
""" Esempio di utilizzo della libreria math """
""" import math

raggio = float(input("Inserisci la misura del raggio: " ))
area_cerchio = math.pi * raggio ** 2
print (f"Area del cerchio: {area_cerchio:.3f}")  # Output: Area del cerchio: 78.539
 """

""" ------------------------------------------------------------------------------ """
#Esercizio 1: Calcolo dell'ipotenusa
""" Crea una funzione che calcola l'ipotenusa di un triangolo rettangolo dati i cateti A e B
    Usa math.sqrt() per il calcolo della radice quadrata."""

""" import math
def calcola_ipotenusa(catetoA, catetoB):
    ipotenusa = math.sqrt(catetoA **2 + catetoB ** 2)
    return ipotenusa
print(f"L'ipotenusa è: {calcola_ipotenusa(30,40)}") """  # Output: L'ipotenusa è: 5.0

""" ------------------------------------------------------------------------------ """
#La libreria Random
""" Esempio di utilizzo della libreria random """
import random
numero_casuale = random.randint(1,100)
print("Il numero casuale è:", numero_casuale)

#Esercizio 2: Simulazione del lancio di un dado
"""Crea una funzione lancia_dado che simula il lancio di un dado a 6 facce,
 restituendo un numero tra 1 e 6.
 Esegui la funzione 10 volte e stampa i risultati."""
import random
def lancia_dado():
    return random.randint(1, 6)
for _ in range(10):
    print(f"Lancio del dado: {lancia_dado()}")
