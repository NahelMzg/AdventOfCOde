import numpy as np
import copy


# Ouvrir le fichier en mode lecture
with open("xmasInput.txt", "r", encoding="utf-8") as fichier:
    # Lire chaque ligne, en supprimant les caractères inutiles
    lignes = [ligne.strip().split() for ligne in fichier]  # Découper chaque ligne en une liste de valeurs

# Convertir la liste de listes en un tableau NumPy 2D
xmasArray = np.array(lignes)  # Convertir en float si les valeurs sont numériques

# Afficher le tableau NumPy
# print("Tableau NumPy 2D contenant les données du fichier :")
# print(xmasArray)

# Transformation de chaque ligne en une liste de caractères
matrice = np.array([list(ligne) for ligne in xmasArray])

#==== Functions



def wordToList(wordList : list) :
    '''
    

    La liste wordList est composé d'un seul mot à ce stade
    
    Cette fonction transforme un liste contenant un seul mot en une liste 
    contenant chaque lettre contenue par le mot

    '''
    mot = wordList[0]
    
    newList =[]
    
    for i in range(len(mot)) :
        
        newList.append(mot[i])
        
    return newList

def transformNumpy(array) :
    '''
    Transforme un array numpy contenant plusieurs listes contenant chacune
    un seul mot en un array numpy contenant plusieurs listes contenant chacune 
    les lettres qui composent les mots d'origine
    
    '''
    lenMot = len(xmasArray[0][0])
    
    newArray = np.array([[wordToList(xmasArray[i])[j] for j in range(lenMot)] for i in range(len(xmasArray))])
        
    return newArray
    

def lookForXmas(array) :
    
    count = 0
    
    #en lignes
    for i in range(len(array)) :
       
        for j in range(len(array[0])-3) :
            
            if array[i,j] + array[i,j+1] + array[i,j+2] + array[i,j+3] == "XMAS" :
                
                count += 1
            if array[i,j] + array[i,j+1] + array[i,j+2] + array[i,j+3] == "SAMX" :
                count += 1
    
    #diagonales
    for i in range(len(array)-3) :
        
        for j in range(len(array[0])-3) :
             
            if array[i,j] + array[i+1,j+1] + array[i+2,j+2] + array[i+3,j+3] == "XMAS" :
                 
                count += 1
            
            if array[i,j] + array[i+1,j+1] + array[i+2,j+2] + array[i+3,j+3] == "SAMX" :
                  
                count += 1
                
    #anti diagonale           
    for i in range(3,len(array)) :
         
        for j in range(len(array[0])-3) :
            
            if array[i,j] + array[i-1,j+1] + array[i-2,j+2] + array[i-3,j+3] == "XMAS" :
                  
                 count += 1
            
            if array[i,j] + array[i-1,j+1] + array[i-2,j+2] + array[i-3,j+3] == "SAMX" :
                   
                 count += 1
    
    #en colonne
    
    for i in range(len(array)-3) :
         
        for j in range(len(array[0])) :
            
            if array[i,j] + array[i+1,j] + array[i+2,j] + array[i+3,j] == "XMAS" :
                  
                 count += 1
                 
            if array[i,j] + array[i+1,j] + array[i+2,j] + array[i+3,j] == "SAMX" :
                   
                  count += 1
        
    return count


def lookForXdashMas(array) :
    
    count = 0
    
    for i in range(len(array)-2) :
         
        for j in range(len(array[0])-2) :
            
            if array[i,j] + array[i+1,j+1] + array[i+2, j+2] +array[i+2,j] + array[i, j+2] == "MASMS" :
                count +=1
                
            
            if array[i,j] + array[i+1,j+1] + array[i+2, j+2] +array[i+2,j] + array[i, j+2] == "MASSM" :
                count +=1
             
            
            if array[i,j] + array[i+1,j+1] + array[i+2, j+2] +array[i+2,j] + array[i, j+2] == "SAMMS" :
                count +=1
            
           
            if array[i,j] + array[i+1,j+1] + array[i+2, j+2] +array[i+2,j] + array[i, j+2] == "SAMSM" :
                count +=1
            
    return count
    
#==== Test



mot = xmasArray[3]

print("mot : ",mot)

print(wordToList(mot))

print('checkpoint')

readyForSearchArray = transformNumpy(xmasArray)

print("newArray : ",transformNumpy(xmasArray))

print("lookForXmas", lookForXmas(readyForSearchArray))

print("lookForX-mas", lookForXdashMas(readyForSearchArray))