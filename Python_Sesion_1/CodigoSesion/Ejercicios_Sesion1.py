#Python script
from click._compat import raw_input 


#Problem 1

def maximo(number1, number2):
    if number1>number2:
        print(str(number1) + " es mayor")
    elif number2 > number1:
        print(str(number2) + " es mayor")
    else:
        print("son iguales")


print("Problema 1 ");

try:
    
    number1 = int(raw_input("Introduce primer número: "));
    number2 = int(raw_input("Introduce segundo número: "));
    
    maximo(number1, number2)
    
except ValueError:
    
    print ("Problem line 27: Not a number")
    

#Problem 2

def numCadena(strCadena):
    i = 0
    for charLetter in strCadena:
        if charLetter!=' ':
            i += 1
    
    return i

print("\nProblema 2 ");

strCadena = raw_input("Introduzca cadena de texto ");

print("La cadena que ha introducido tiene "+str(numCadena(strCadena))+" caracteres");

#Problem 3

def validLetter(charLetter):
    letters = ['a', 'e', 'i', 'o', 'u', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    
    for letter in letters:
        if charLetter.lower() == letter:
            return True;
    return False;
    
def isVocal(charLetter):
    vocals = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    
    if(validLetter(charLetter)):
        for vocal in vocals:
            if charLetter.lower()==vocal:
                return True;
        
        for consonant in consonants:
            if charLetter.lower() == consonant:
                return False;
    else:
        print("Tipo de caracter no válido");
            
def typeLetter(charLetter):
    aux = isVocal(charLetter);
    if aux == True:
        print("La letra "+charLetter+" es una vocal");
    elif aux == False:
        print("La letra "+charLetter+" es una consonante");

print("\nProblema 3");

charLetter = raw_input("Introduzca una letra: ");

typeLetter(charLetter[0]);


#Problem 4

def conversor(strBinario):
    pot = len(strBinario)-1
    aux = 0
    
    for binario in strBinario:
        try:
            if(int(binario)==1):
                aux += pow(2, pot)
                pot -= 1
            elif(int(binario)==0):
                pot -= 1
            else:
                print("No es un número binario!")
                aux = 0;
                break;
        except ValueError:
            print("No es posible la conversión!!")
            aux = 0;
            break; 

    return aux

print("\nProblema 4");

strBinario = raw_input("Introduzca binario: ");

aux =  conversor(strBinario)

if(aux != 0):
    print("El número en decimal es: "+str(aux));   
    