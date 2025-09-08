""" x = tuple(("milano","roma", "napoli"))
print(type(x)) """

""" x ={"milano", "roma", "napoli"}
for citta in x:
    print(citta)
     """

""" persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 35,
    "indirizzo": {
        "citta": "milano",
        "cap": "00000",
        "civico": 45
    }
}

print(persona["indirizzo"]["citta"]) """

""" def fai_la_pasta(tipo_pasta):
    print("metti l'acqua")
    print("fai bollire")
    print("metti " + tipo_pasta)

fai_la_pasta("spaghetti")
     """

""" import datetime
x = datetime.datetime.now()
print(x.strftime("%W %d %Y"))
 """

""" import camelcase
c = camelcase.CamelCase()
frase = "ciao sono una frase in camelcase"
print(c.hump(frase)) """

""" x = 5
t = "cucù"
try:
    print(x + "Ciao")
except NameError:
    print("era sbagliato")
 """
""" persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 25
}

operazioni = ("aggiungere", "modificare", "eliminare")

def start():
    operazione = input("Cosa vuoi fare? ")
    if operazione == operazioni[0]:
        x = input("Aggiungi chiave:valore separati da una virgola aggiungi")
        aggiungi(x.split(","))
    elif operazione == operazioni[1]:
        pass
    elif operazione == operazioni[2]:
        pass

def aggiungi(param):
    chiave = param[0]
    valore = param[1]
    persona[chiave] = valore
    print(persona)

while True:
    start() """

""" peso = 65
altezza = 176
eta = 25
frase = "Ciao sono io ed ho {eta} anni, peso {peso} kg e sono alto {altezza} cm"

print(frase.format(eta=eta, peso=peso, altezza=altezza)) """

""" f = open("nuovotesto.txt", "x")

f.write("dentro scriviamo quel che vogliamo")
f.close()
f = open("testo.txt", "r")
print(f.read()) """
""" import os

if os.path.exists("nuovotesto.txt"):
    os.remove("nuovotesto.txt")
else:
    print("non esiste un file con questo nome") """

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pysql"
)

cursor = db.cursor()

""" sql ="INSERT INTO clienti (nome, cognome) VALUES (%s, %s)" 
values = ("Giorgio", "Strunz")
cursor.execute(sql, values)

db.commit()
print("id riga inserita: ", cursor.lastrowid) """

""" sql = "SELECT * FROM clienti WHERE nome = 'giorgio' OR cognome = 'qualunque'"

cursor.execute(sql)
result = cursor.fetchall()

for riga in result:
    print(riga) """

""" sql = "SELECT * FROM clienti ORDER BY nome LIMIT 4"

cursor.execute(sql)
result = cursor.fetchall()

for riga in result:
    print(riga) """

""" sql = "DELETE FROM clienti WHERE nome = %s AND cognome = %s"

valore = ("Giorgio", "Frego")
cursor.execute(sql, valore)
db.commit()

print("numero di righe cancellate: ", cursor.rowcount)
 """

""" sql = "UPDATE clienti SET nome = %s WHERE ID = %s"
valori = ("Gigio", 11)

cursor.execute(sql, valori)
db.commit()
print("Righe modificate: ", cursor.rowcount) """

