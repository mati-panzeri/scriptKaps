#Importar la libreria pandas
import pandas as pd
import cleanNewLine as cl
import append as append
from vendorModules import novell as novell
from vendorModules import rhel as rhel
from vendorModules import ubuntu as ubuntu
from vendorModules import oracle as oracle


#Importamos archivo csv y txt
df = pd.read_csv("filesToEdit/Kaps_adv_published.csv", sep=',')
archivoTxt = open('filesToEdit/advisories.txt')


#array de advisories
queue = archivoTxt.readlines()
updates = []
newAdvisories = []

#Declaramos constante con vendors especiales
VENDORS = ['Novell', 'Red Hat', 'Oracle', 'Ubuntu']


for adv in range(len(queue)):
    title = cl.cleanNewLine(queue[adv])
    #list(map(lambda l: l.rstrip('\n'), newAdvisories[adv]))
    title = "".join(title)
    #print(cleanTitle)
    cleanTitle = title.split(':', 1)

    if cleanTitle[0] not in VENDORS:
        cleanTitle = cleanTitle[1].strip()
        boolean = df['title'].str.contains(cleanTitle, case=False, regex=False)
        append.append(boolean, title, updates, newAdvisories)
    elif cleanTitle[0] == VENDORS[0]:
        cleanTitle = cleanTitle[1].strip()
        cleanTitle = novell.novell(cleanTitle)
        boolean = df['title'].str.contains(cleanTitle, case=False, regex=False)
        append.append(boolean, title, updates, newAdvisories)
        print(cleanTitle)
    elif cleanTitle[0] == VENDORS[1]:
        cleanTitle = cleanTitle[1].strip()
        cleanTitle = rhel.rhel(cleanTitle)
        boolean = df['title'].str.contains(cleanTitle, case=False, regex=False)
        append.append(boolean, title, updates, newAdvisories)
        print(cleanTitle)
    elif cleanTitle[0] == VENDORS[2]:
        cleanTitle = cleanTitle[1].strip()
        cleanTitle = oracle.oracle(cleanTitle)
        boolean = df['title'].str.contains(cleanTitle, case=False, regex=False)
        append.append(boolean, title, updates, newAdvisories)
        print(cleanTitle)
    elif cleanTitle[0] == VENDORS[3]:
        cleanTitle = cleanTitle[1].strip()
        cleanTitle = ubuntu.ubuntu(cleanTitle)
        boolean = df['title'].str.contains(cleanTitle, case=False, regex=False)
        append.append(boolean, title, updates, newAdvisories)
        print(cleanTitle)

#Creamos archivo nuevo con los adv ordenados
nuevoTxt = 'filesToEdit/advisoriesOrdenados.txt'
with open(nuevoTxt, 'a') as file:
    file.write('UPDATES\n')
    for update in updates:
        file.write(update + '\n')
    file.write('-------------------\n')
    file.write('NUEVOS:\n')
    for new in newAdvisories:
        file.write(new + '\n')

print("Se generó el archivo!")