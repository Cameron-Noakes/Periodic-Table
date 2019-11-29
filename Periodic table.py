##You only need to get this working for 6 elements from two different groups.

elements = [
    ["Lithium","3","1"],["Sodium","11","1"],["Potassium","19","1"],
    ["Magnesium","12","2"],["Calcium","20","2"],["Barium","56","2"]
    ]

print("1 is the Element, 2 is the Atomic Weight, 3 is the Group\n(Must have Element with capital)")

for item in elements:
    user = input("Enter name of element: ")
    
    if user == elements[0][0] or user == "Li" or user == "1":
        print (elements[0])

    if user == elements[1][0] or user == "Na" or user == "1":
        print (elements[1])
    
    if user == elements[2][0] or user == "K" or user == "1":
        print (elements[2])

    if user == elements[3][0] or user == "Mg" or user == "2":
        print (elements[3])

    if user == elements[4][0] or user == "Ca" or user == "2":
        print (elements[4])

    if user == elements[5][0] or user == "Ba" or user == "2":
        print (elements[5])
