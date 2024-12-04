
import copy


import pandas as pd

excel_file_path = "newReports.xlsx"
df = pd.read_excel(excel_file_path)

i = 0

i = 999

# Vérification que l'indice existe dans les données
if i < len(df):
    # Extraction de la ligne et suppression des NaN
    ligne_i = df.iloc[i].tolist()  # Conversion en liste
    ligne_sans_nan = [valeur for valeur in ligne_i if pd.notna(valeur)]  # Supprimer les NaN
    print("Ligne sans NaN :", ligne_sans_nan)
   
else:
    print(f"Ligne {i} hors des limites du fichier (taille max: {len(df)-1}).")
    


#==== Initialisation

Liste = [1,2,5,34]

ListeDec = [7,3,3,1]



#==== Functions

def isSafeIncreasingly(L):
    for i in range(1, len(L)):
        if L[i] <= L[i-1] or not (1 <= abs(L[i] - L[i-1]) <= 3):
            return False
    return True


def isSafeDecreasingly(L):
    for i in range(1, len(L)):
        if L[i] >= L[i-1] or not (1 <= abs(L[i] - L[i-1]) <= 3):
            return False
    return True

def isSafe(L):
    if isSafeDecreasingly(L) or isSafeIncreasingly(L):
        return True
    
    for i in range(len(L)):
        copyL = L[:i] + L[i+1:]  # Supprime l'élément à l'indice i
        if isSafeDecreasingly(copyL) or isSafeIncreasingly(copyL):
            return True
    
    return False



# def isSafeable(L : list) :
    
#     trueIterations = 0
    
#     if isSafe(L) :
       
#         return False
    
   
    
#     for i in range(0,len(L)) :
       
#         copyL = copy.deepcopy(L)
#         del copyL[i]
#         print(copyL)
        
    
#         if isSafe(copyL) :
        
#             trueIterations +=1
    
   
#     if trueIterations == 1 :
#         return True
#     else :
#         return False
        

    
    
def findSafeNumber(df) :
    safeNumber = 0 
    
    for i in range(0,len(df)) :
    
       
        
        ligne_i = df.iloc[i].tolist()  # Conversion en liste
        ligne_i_sans_nan = [valeur for valeur in ligne_i if pd.notna(valeur)]    
      

        
       
        if isSafe(ligne_i_sans_nan) :
            safeNumber +=1
            
          
        
            
            
      
            
            
    return safeNumber


        

#==== Tests
LSafeable=[6.0, 8.0, 9.0, 11.0, 10.0]



print("isSafe: ",isSafe(LSafeable))


# print(isSafeIncreasingly(Liste))
# print(isSafeDecreasingly(ListeDec))
# print(isSafe(ListeDec))
print(findSafeNumber(df))
