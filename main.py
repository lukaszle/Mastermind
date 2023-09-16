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
def code(a,b,c,d):
    #5 kolorów pionków do ustalania kodu
    pin = ["A","B","C","D","E","F"]
    #Losowanie elementu z tablicy
    a = random.randint(41,46)
    secret = [a,b,c,d]
    print("Kod Mastermind: ", secret)
def test(field_dyn):
    globals()[field_dyn] = ["X","Y"]
    print("Dynamiczne pole", globals()[field_dyn])
#Wrpwoadzanie wartości do pola grye
def points():
    player1 = 0
    #Obliczanie punktów
    return player1
def set_mark(field,a,b,c,d):
    duze = [a,b,c,d]
    male = [1,1,1,1]
    set = fields(field, duze, male)
x = set_mark("5","X","Y","A","B")
#fields("3",0,1)
test("fieldX")
code("X","V","F","P")