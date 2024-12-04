
import copy
 

path = "Distances"

# Charger le contenu du fichier RTF
with open("votre_fichier.rtf", "r", encoding="utf-8") as file:
    rtf_content = file.read()

# Convertir le contenu RTF en texte brut
plain_text = rtf_to_text(rtf_content)

# Afficher le texte brut
print(plain_text)

# Supposons que les données soient sous forme de listes séparées par des lignes vides ou des délimiteurs
# Vous pouvez les extraire avec des séparateurs spécifiques, comme "\n" :
listes = [ligne.split("") for ligne in plain_text.split("\n") if ligne.strip()]
print(listes)

#==== Initialisation


L = [2, 3, 1, 2, 93, 5]

L2= [3, 3, 42, 34, 53, 5]


def read_file(f):
    # charge les données de path dans une liste et retourne la liste
    L = []
    f = open('frenchssaccent.dic','r' ) 
    for ligne in f:
    #éliminer les mots de taille <= len(tirage)
        mot= ligne[0:len(ligne)-1]
       
        L.append(mot) #on prend tout sauf le backslash n 
    f.close()
    return L




#==== Functions

def findMax(L : list) :

    n = len(L)
    max = L[0] 
    for i in range(1, n) :
        if L[i] > max :
            max = L[i]
          
    return min

def findMin(L : list) :

    n = len(L)
    min = L[0] 
    minIndex = 0
    for i in range(1, n) :
        if L[i] < min :
            min = L[i]
            minIndex = i
    return min, minIndex

def orderList(L : list) :
    orderedList = []
    max = findMax(L)
    copyL = copy.deepcopy(L)
    for i in range(0, len(L)) :
        minAndMinIndex = findMin(copyL)
        
        orderedList.append(minAndMinIndex[0])
        
        copyL[ minAndMinIndex[1]] =  10000
    return orderedList

def distanceBetweenLists(L1, L2) :
    distances = []
    orderedL1 = orderList(L1)
    orderedL2 = orderList(L2)

    for i in range(len(L1)):
        distance = abs(orderedL1[i]- orderedL2[i])
        distances.append(distance)
    
    return distances

def sumList(L : list) :
    s = 0
    for i in range(0, len(L)) :
        s = s + L[i]

    return s



#==== Tests

print(findMin(L))
print(orderList(L))
print(orderList(L2))
print(distanceBetweenLists(L, L2 ))
print(sumList(distanceBetweenLists(L,L2)))

