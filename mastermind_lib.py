import random

def fields(field, large,small):
    #Pole do gry z czterema dużymi otworami, a także czterema małymi otworami
    #5 kolorów pionków
    field0 = [[0,0,0,0], [0,0,0,0]]
    field1 = [[1,0,0,0], [0,0,0,0]]
    field2 = [[2,0,0,0], [0,0,0,0]]
    field3 = [[3,0,0,0], [0,0,0,0]]
    field4 = [[4,0,0,0], [0,0,0,0]]
    field5 = [[5,0,0,0], [0,0,0,0]]
    field6 = [[6,0,0,0], [0,0,0,0]]
    field7 = [[7,0,0,0], [0,0,0,0]]
    field8 = [[8,0,0,0], [0,0,0,0]]
    match field:
        case "0":
            field0 = large, small
            print("Pole do gry",field, field0)
        case "1":
            field1 = large, small
            print("Pole do gry",field, field1)
        case "2":
            field2 = large, small
            print("Pole do gry",field, field2)
        case "3":
            field3 = large, small
            print("Pole do gry",field, field3)
        case "4":
            field4 = large, small
            print("Pole do gry",field, field4)
        case "5":
            field5 = large, small
            print("Pole do gry",field, field5)
        case "6":
            field6 = large, small
            print("Pole do gry",field, field6)
        case "7":
            field7 = large, small
            print("Pole do gry",field, field7)
        case "8":
            field8 = large, small
            print("Pole do gry",field, field8)                     
#Dynamiczne pole
def code():
    #5 kolorów pionków do ustalania kodu
    pin = ["A","B","C","D","E","F"]
    #Losowanie elementu z tablicy
    a = random.choice(pin)
    b = random.choice(pin)
    c = random.choice(pin)
    d = random.choice(pin)
    secret = [a,b,c,d]
    return secret


def check_code(code, entered_code):
    male = []
    print("\"X\" oznacza trafienie litery na prawidłowej pozycji")
    print("\"O\" oznacza trafienie litery znajdującej się na liście ale na nieodpowiedniej pozycji ")
    print("\"-\" oznacza brak litery na liście ")

    for i in range(4):
        if entered_code[i] == code[i]:
            male.append("X")
        elif entered_code[i] in code:
            male.append("O")
        else:
            male.append("-")
    return male

def game():
    #Funkcja do gry w Mastermind
    print("Gra Mastermind")
    start = input("Żeby rozpocząć nową grę wprowadź \"N\" Żeby zakończyć wprowadź \"Q\"")
    if start == "N":
        kod = code()
        for i in range(9):
            runda = i
            if runda == 8:
                print("Przegrałeś")
                print("Kod Mastermind", kod)
                break
            print("Runda ", runda)
            x = input("Wprowadź 4 litery od A do F:")
            x_list = [*x]
            #print("Wprowadzony kod:", x_list)
            check = check_code(kod, x_list)
            #print("Wynik:", check)
            fields(str(i),x_list, check)
            if check == ["X","X","X","X"]:
                print("Wygrałeś")
                print("Wygrana w", runda, "rundach")
                print("Kod Mastermind: ", kod)
                break
    else:
        quit()
    quit()
#fields("3",0,1)
#game()
#