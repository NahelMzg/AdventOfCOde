
# Ouvrir le fichier en mode lecture
with open("corruptedMemory.rtf", "r", encoding="utf-8") as fichier:
    chaine = fichier.read().strip()  # Lire le contenu et supprimer les espaces inutiles

# Afficher la chaîne extraite
#print("La chaîne extraite est :", chaine)


#==== Functions

def isInt(word : str) :
    try:
        int(word)
        return True
    except ValueError:
        return False
    
    


def findActions(word : str) :
    
    actionDictionnary = {}
    
    

def findUncorrupted(word : str) :
    
    uncorruptedMemory =[]
    
    
    for i in range(len(word)-3) :
        
        currentWord = ""
        
        isAccurate = False
        
       
        if word[i]+word[i+1]+word[i+2]+word[i+3] == 'mul(' :
                
            currentWord += word[i]+word[i+1]+word[i+2]+word[i+3]
            startIndex= i+3
            
        
       
            
            isAccurate = False
        
               
            number = ""
            whatNumber = "first"
                    
                
            for j in range(1,len(word)) :
                      
                if isInt(word[startIndex+j]) :
                            
                    number += word[startIndex+j]
                            
                elif j>1 and word[startIndex+j] == "," :
                            
                                
                    currentWord += number + ","
                           
                    number =""
                    whatNumber = "second"
                            
                            
                elif whatNumber =="second" and len(number)>0  and word[startIndex+j] == ")" :
                                
                    currentWord += number + ")"
                          
                    isAccurate = True
                            
                    break
                            
                else :
                    break
                
                
            if isAccurate :
                        
                uncorruptedMemory.append(currentWord)
        
       
    return uncorruptedMemory

def findUncorruptedV2(word : str) :
    
    uncorruptedMemory =[]
    
    action =""
    
    
    for i in range(len(word)-6) :
        
        currentWord = ""
        
        isAccurate = False
        
        if word[i]+word[i+1]+word[i+2]+word[i+3]+word[i+4]+word[i+5]+word[i+6] == "don't()" :
            
            action = "don't"
            
        if word[i]+word[i+1]+word[i+2]+word[i+3] == "do()" :
             
            action = "do"
            
        print("action :", action)
       
        if action != "don't" :
            
            if word[i]+word[i+1]+word[i+2]+word[i+3] == 'mul(' :
                    
                currentWord += word[i]+word[i+1]+word[i+2]+word[i+3]
                startIndex= i+3
                
            
           
                
                isAccurate = False
            
                   
                number = ""
                whatNumber = "first"
                        
                    
                for j in range(1,len(word)) :
                          
                    if isInt(word[startIndex+j]) :
                                
                        number += word[startIndex+j]
                                
                    elif j>1 and word[startIndex+j] == "," :
                                
                                    
                        currentWord += number + ","
                               
                        number =""
                        whatNumber = "second"
                                
                                
                    elif whatNumber =="second" and len(number)>0  and word[startIndex+j] == ")" :
                                    
                        currentWord += number + ")"
                              
                        isAccurate = True
                                
                        break
                                
                    else :
                        break
                    
                    
                if isAccurate :
                            
                    uncorruptedMemory.append(currentWord)
        
       
    return uncorruptedMemory

def mulToExpression(word : str) :
    
    start = 3
    expression =""
    for i in range(1,len(word)-4) :
        
        if isInt(word[start+i]) :
            
            expression += word[start+i]
       
        elif word[start+i] =="," :
            expression += "*"
            
        
    
    
    
    return expression



def productSum(ProductList : list) :
    
    s = 0
    for i in range(len(ProductList)):
        expression = mulToExpression(ProductList[i])
        s+=  eval(expression)
    return s


#=== Tests


motTest = "sqjnbchjhbqsjmul(3,4)slxknqx$$*€sjxqnijxmul(sqNXOSqnxmu(((3,4)lxqkn<cnxqmul(532,9920)qsCKNXPSnx"
L =findUncorrupted(motTest)

uncorrupted = findUncorrupted(chaine)
uncorrupted2 = findUncorruptedV2(chaine)
print(findUncorrupted(motTest))


print(mulToExpression(L[0]))


print("réponse 1: ", "183788984" )
print("réponse 1: ", productSum(uncorrupted))
print("réponse 2: ", productSum(uncorrupted2))
