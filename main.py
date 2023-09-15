def fields(field, large,small):
    #Pole do gry z czterema dużymi otworami, a także czterema małymi otworami
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
            print("Pole do gry",field0)
        case "1":
            print("Pole do gry",field1)
        case "2":
            print("Pole do gry",field2)
        case "3":
            print("Pole do gry",field3)
        case "4":
            print("Pole do gry",field4)
        case "5":
            print("Pole do gry",field5)
        case "6":
            print("Pole do gry",field6)
        case "7":
            print("Pole do gry",field7)
                        

def test(field_dyn):
    # Dynamic_Variable_Name can be
# anything the user wants
# The value 2020 is assigned
# to "geek" variable
    globals()[field_dyn] = ["X","Y"]
# Display variable
    print("Dynamiczne pole",fieldX)


fields(3,0,1)
test("fieldX")