
def inputInRange(minNumber, maxNumber):
    countErrors=0
    while True:
        number = int(input("Введите число: "))
        if(number<=maxNumber and number>=minNumber):
            return number
            break
        else:
            countErrors = countErrors+1
        if(countErrors>3):
            return minNumber-1
            break

def getNumberPiramidus(number):
    # for i in range(1, n+1):
    #     print(str(i)*i)



    piramida = [1]
    hashNuber = 11
    for i in range(2, number+1):
        piramida.append(hashNuber*i)
        hashNuber = hashNuber*10+1
    return(piramida)

def getNumberKvadratus(number):
    kvadratus = []
    hashNuber = 11
    for i in range(2, number+1):
        hashNuber = hashNuber*10+1
    for i in range(1, number+1):
        kvadratus.append(number*hashNuber)
    return kvadratus

        

def isOverVeryNiceNumber(number):
    dels = []
    for i in range(1, number):
        if(number%i==0):
            dels.append(i)

    return sum(dels)==number

class program1(object):
    def __init__(self):
        print("Programm created")
    def script(self):
        
        maxNumber = 100
        minNumber = -100

        firstNumber = inputInRange(minNumber, maxNumber)
        secondNumber = inputInRange(minNumber, maxNumber)

        if(firstNumber == minNumber-1) or (secondNumber == minNumber-1):
            return

        if(firstNumber>secondNumber):
            hashNumber = secondNumber
            secondNumber = firstNumber+1
            firstNumber = hashNumber
        
        print("Начинаю печатать ...")

        for i in range(firstNumber, secondNumber):
            if(i%2==1):
                print(i)

class program2(object):
    def __init__(self):
        print("Programm created")
    def script(self):
        minNumber = 1
        maxNumber = 1000

        nuber = inputInRange(minNumber, maxNumber)

        if(nuber==minNumber-1):
            return
        if(nuber%2==0):
            print("Это число четное")
        else:
            print("Это число нечетное")
        
class program3(object):
    def __init__(self):
        print("Programm created")
    def script(self):
        minNumber = 1
        maxNumber = 1000

        number = inputInRange(minNumber, maxNumber)

        if(number==minNumber-1):
            return

        if isOverVeryNiceNumber(number):
            print("Это число супер-супер")
        else:
            print("Это число не супер-супер")

class program4(object):
    def __init__(self):
        print("Programm created")
    def script(self):
        minNumber = 1
        maxNumber = 9

        number = inputInRange(minNumber, maxNumber)

        if(number==minNumber-1):
            return

        piramida = getNumberPiramidus(number)
        for i in piramida:
            print(i)

class program5(object):
    def __init__(self):
        print("Programm created")
    def script(self):
        minNumber = 1
        maxNumber = 9

        number = inputInRange(minNumber, maxNumber)

        if(number==minNumber-1):
            return    
        kvadratuus = getNumberKvadratus(number)
        for i in kvadratuus:
            print(i)


def Main():
    p = program5()
    p.script()

if __name__ == "__main__":
    Main()
