import datetime

flights = [
    [
        'vno',
        'kns',
         datetime.datetime(2024, 10, 15, 14, 30, 0),
         datetime.datetime(2024, 10, 15, 16, 30, 0)
     ],
    [
        'vno',
        'tln',
         datetime.datetime(2024, 10, 15, 14, 30, 0),
         datetime.datetime(2024, 10, 15, 20, 30, 0)
     ],
    [
        'vno',
        'chr',
         datetime.datetime(2024, 10, 15, 14, 30, 0),
         datetime.datetime(2024, 10, 15, 15, 00, 0)
     ]
]

def printInfo():
    print("---------------------------------------------")
    print("1. sarasas 2. ideti 3. redaguoti 4. trinti 5. baigti programa")
    print("1. Skrydžių atvaizdavimas")
    print("2. Naujo skrydžio įkėlimas")
    print("3. Skrydžio redagavimas")
    print("4. Skrydžio šalinimas")
    print("5. Išeiti iš programos")
    print("---------------------------------------------")

def printFlight(fl, num = 1):
    print(f'{num}. Skrydis iš {fl[0]} į {fl[1]}. Pakyla {fl[2]}, nusileidžia {fl[3]}. Skrydžio trukmė - '
          f'{fl[3] - fl[2]} ')

def printFlights():
    num = 1
    for fl in flights:
        printFlight(fl, num)
        num += 1

def addFlight():
    print("Iš kur skrenda?")
    flFrom = input()
    print("Į kur skrenda?")
    flTo = input()
    print("Kada kyla? (yyyy-mm-dd hh:mm:ss)")
    flLeave = datetime.datetime.strptime(input(), "%Y-%m-%d %H:%M:%S")
    print("Kada leidžiasi? (yyyy-mm-dd hh:mm:ss)")
    flArrive = datetime.datetime.strptime(input(), "%Y-%m-%d %H:%M:%S")
    flights.append([flFrom, flTo, flLeave, flArrive])

def editFlight():
    print("Įveskite skrydžio numerį kurį norite redaguoti")
    ed = int(input())
    printFlight(flights[ed - 1])
    print("suvekite naujas reišmes:")
    print("Iš kur skrenda?")
    flFrom = input()
    print("Į kur skrenda?")
    flTo = input()
    print("Kada kyla? (yyyy-mm-dd hh:mm:ss)")
    flLeave = datetime.datetime.strptime(input(), "%Y-%m-%d %H:%M:%S")
    print("Kada leidžiasi? (yyyy-mm-dd hh:mm:ss)")
    flArrive = datetime.datetime.strptime(input(), "%Y-%m-%d %H:%M:%S")
    flights[ed - 1] = [flFrom, flTo, flLeave, flArrive]

def removeFlight():
    print("Įveskite skrydžio numerį kurį norite pašalinti")
    rem = int(input())
    flights.pop(rem - 1)

print("---SKRYDŽIŲ VALDYMO SISTEMA---")

while True:
    printInfo()
    opt = int(input())
    match opt:
        case 1:
            printFlights()
        case 2:
            addFlight()
            printFlights()
        case 3:
            editFlight()
            printFlights()
        case 4:
            removeFlight()
            printFlights()
        case 5:
                exit(1)