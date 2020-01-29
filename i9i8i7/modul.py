import csv
import json

def introduction():
    print("Välkommen till programmet.")
    choice = ""
    epiclist = startup()

    while choice != 6:
        print("\n[1] - Läs in csv-fil")
        print("[2] - Visa json-data")
        print("[3] - Lägg till person")
        print("[4] - Ta bort person")
        print("[5] - Spara fil")
        print("[6] - Avsluta")

        try:
            choice = int(input("Vilket alternativ vill du välja? "))
        except ValueError:
            print("Oops! That's not a number!")

        if choice == 1:
            epiclist = readfromfile()
        elif choice == 2:
            viewjson(epiclist)
            print("JSON-data has been shown")
        elif choice == 3:
            addperson(epiclist)
            print("Personen har blivit tillagd!")
        elif choice == 4:
            delperson(epiclist)
            print("Personen har tagits bort!")
        elif choice == 5:
            saveasjson(epiclist)
            print("Filen har sparats!")
        elif choice == 6:
            print("You have chosen to exit the program.")
        else:
            print("Please choose a number 1-6!")

def startup():
    epiclist = []
    try:
        with open('data.json', 'r', encoding='UTF-8') as File:
            print("Json filen finns! wow")
            epiclist = json.load(File)
    except Exception as p:
        print(p)
        epiclist = readfromfile(False)
        #testa om csv filen finns
    return epiclist

def readfromfile(afterstartup = True):
    randomlist = []
    try:
        with open('personer.csv', newline='', encoding='UTF-8') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            for row in spamreader:
                #print(', '.join(row))
                d = {}
                d["fnamn"] = row[0]
                d["enamn"] = row[1]
                d["email"] = row[3]
                randomlist.append(d)
            if (afterstartup):
                for line in randomlist:
                    print(line)
        print("CSV-file has now been loaded.")
        return randomlist
    except FileNotFoundError:
        print("File Not Found")

def viewjson(epiclist):
    print(epiclist)
    # try:
    #     with open('data.json') as data_file:
    #         print("Successful")
    # except:
    #     saveasjson(epiclist)
    # with open('data.json') as data_file:
    #     data_loaded = json.load(data_file)
    #     for lines in data_loaded:
    #         print(lines)

def addperson(epiclista):
    addstuff = {}
    addstuff["fnamn"] = input("Skriv in namn: ")
    addstuff["enamn"] = input("Skriv in efternamn: ")
    addstuff["email"] = input("Skriv in email: ")
    print(addstuff)
    epiclista.append(addstuff)
    return epiclista

def delperson(epiclist):
    try:
        deleteperson = int(input("Vem vill du ta bort? Nummer: "))
        epiclist.pop(deleteperson)
        print(f'Removed person number: {deleteperson}!')
    except ValueError:
        print("Deletion of person has failed.")
    return epiclist

def saveasjson(epiclist):
    with open('data.json', 'w', encoding='UTF-8') as outfile:
        json.dump(epiclist, outfile, ensure_ascii=False, indent=2)