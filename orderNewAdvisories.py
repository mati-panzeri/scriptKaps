#Importar la libreria pandas
import pandas as pd
import cleanNewLine as cl
import append as append
from vendorModules import novell as novell
from vendorModules import rhel as rhel
from vendorModules import ubuntu as ubuntu


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
    cleanTitle = cl.cleanNewLine(queue[adv])
    #list(map(lambda l: l.rstrip('\n'), newAdvisories[adv]))
    cleanTitle = "".join(cleanTitle)
    #print(cleanTitle)
    cleanTitle = cleanTitle.split(':', 1)

    if cleanTitle[0] not in VENDORS:
        cleanTitle = cleanTitle[1].strip()
        boolean = df['title'].str.contains(cleanTitle, case=False, regex=False)
        append.append(boolean, cleanTitle, updates, newAdvisories)
    elif cleanTitle[0] == VENDORS[0]:
        cleanTitle = cleanTitle[1].strip()
        cleanTitle = novell.novell(cleanTitle)
        boolean = df['title'].str.contains(cleanTitle, case=False, regex=False)
        append.append(boolean, cleanTitle, updates, newAdvisories)
        print(cleanTitle)
    elif cleanTitle[0] == VENDORS[1]:
        cleanTitle = cleanTitle[1].strip()
        cleanTitle = rhel.rhel(cleanTitle)
        boolean = df['title'].str.contains(cleanTitle, case=False, regex=False)
        append.append(boolean, cleanTitle, updates, newAdvisories)
        print(cleanTitle)
    elif cleanTitle[0] == VENDORS[2]:
        print("Oracle")
    elif cleanTitle[0] == VENDORS[3]:
        cleanTitle = cleanTitle[1].strip()
        cleanTitle = ubuntu.ubuntu(cleanTitle)
        boolean = df['title'].str.contains(cleanTitle, case=False, regex=False)
        append.append(boolean, cleanTitle, updates, newAdvisories)
        print(cleanTitle)
        
    
    #print(boolean)

    #updates.append(boolean['title'])

    #buscar cleanTitle en df titulos
        # updates.append(cleanTitle)
    #else:
    #    newAdvisories.append(cleanTitle)
    #arrAdvisories.append(cleanTitle)

#print(df['title'])
print(len(updates))
print (len(newAdvisories))
