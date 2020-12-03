import os
import hashlib
from hashlib import sha256
import random
import csv

files_path = input( "Introduceti locatia fisierelor ce vor fi verificate: " ) 

# Deschidem toate fisierele de la locatia introdusa si le punem in lista "files"

filepaths  = [os.path.join(files_path, name) for name in os.listdir(files_path)]
files = []

for path in filepaths:
    with open(path, 'rb') as f:
        file = f.read()
        files.append(file)

# Calculez rezultatele dupa aplicarea SHA-256 

codes = []

for file in files:
    tmp = hashlib.sha512(file)
    codes.append( tmp.hexdigest() )

output_path = os.path.join(files_path, "output.txt" )
g = open( output_path, "w" )

for c in codes:
    g.write( c + "\n" )

# vom introduce rezultatele intr-un csv in directorul unde se afla si fisierele

output_csv = os.path.join(files_path, "checksum_codes.csv" )

with open( output_csv, "w" ) as file:
    writer = csv.writer(file)
    for c in codes:
        writer.writerow([c])

# Acum programul va citi de la user un string pe care il va adauga la urma unui fiser aleatoriu
# dupa care va verifica cheile sha256 existente si va afisa pe ecran la care din fiser s-a 
# produs o eroare

modifier = input( "Introduceti un string: ")

R = random.randint(0, len(files) - 1)
files[R] = files[R] + modifier.encode()

for i in range(len(files)):
    tmp = hashlib.sha512(files[i])
    tmp = tmp.hexdigest()
    if tmp != codes[i]: 
        print( "Fisier corupt cu indexul: " + str(i) )





