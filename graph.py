x = [34, 54, 11, 22, 42, 20, 79, 55, 65, 57]

### schaalt de array naar een getal tussen 0 en 10
def scalar(array):
    p = max(array)/10
    x_augmented = []
    for value in array:
        scaledelement= ((value / p)+0.5)
        x_augmented.append(scaledelement)
    return(x_augmented)

## definieerd welke varabelen in de grafiek een sterretje moeten bevatten
def graphdefine(t):
    col= ["A","B","C","D","E","F","G", "H", "I", "J"]
    for value in t:
        counter = 0
        while counter <= value:
            p = col[t.index(value)] + str(counter)

            exec("global "+ p +"; " + p + " = '*'")
            counter += 1

## definieerd alle variablen van de grafiek naar een spatie zodat er geen errors voorkomen
def set_init_var():
    col = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    for element in col:
         counter=1
         while counter <= 10:
             g = col[col.index(element)] + str(counter)
             exec("global " + g + "; " + g + " = ' '")
             counter += 1


set_init_var()


if x != [0,0,0,0,0,0,0,0,0,0,]:

    graphdefine(scalar(x))

    print( max(x), "\n"
    "|", A10 ,B10 , C10, D10, E10, F10, G10, H10, I10, J10, "\n"
    "|", A9 ,B9, C9, D9, E9, F9, G9, H9, I9, J9, "\n"
    "|", A8 ,B8, C8, D8, E8, F8, G8, H8, I8, J8, "\n"
    "|", A7 ,B7, C7, D7, E7, F7, G7, H7, I7, J7, "\n"
    "|", A6 ,B6, C6, D6, E6, F6, G6, H6, I6, J6, "\n"
    "|", A5 ,B5, C5, D5, E5, F5, G5, H5, I5, J5, "\n"
    "|", A4 ,B4, C4, D4, E4, F4, G4, H4, I4, J4, "\n"
    "|", A3 ,B3, C3, D3, E3, F3, G3, H3, I3, J3, "\n"
    "|", A2 ,B2, C2, D2, E2, F2, G2, H2, I2, J2, "\n"
    "|", A1 ,B1, C1, D1, E1, F1, G1, H1, I1, J1, "\n"
    "+--------------------", "9999" , "\n"
    "1")

