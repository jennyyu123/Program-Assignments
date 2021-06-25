empty_list=[]
#               0         1          2            3             4         5         6              7            8      
city_list=["Oakland", "Atlanta", "New York City", "Seattle", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]


#changing the cities
city_list[0]= "San Francisco"
city_list[2]="Brooklyn"
city_list[6]="Hollywood"
city_list[4]= "Tampa"

city_list.append ("New Jersey")
city_list.extend (["Santa Cruz", "Selma", "Chicago"])
city_list.insert( 7, "Washington, D.C.")
print (city_list
       
City_list.append("Oakland")
City_list.extend(["New York City", "Los Angeles"])
City_list.insert(0, "Miami")
print(City_list)


City_list.pop(4)
City_list.remove("Miami")
print(City_list)


#                0    1    2    3    4    5    6   7    8    9    10
alphabet_list= ["a", "b", "c", "d", "e", "f", "g", "h", "i","j", "k"]
print (alphabet_list)

#lab4

def cities():
    longest_city = "a"
    i = 0 
    while i < len(city_list):
        print(city_list[i])
        x = city_list[i]
        if len(city_list[i]) > len(longest_city):
            longest_city = x 
        i += 1
    return((longest_city))
cities()

def cities_organized():
    for i in range(0, 16):
        b = city_list[i]
        a = city_list[i + 1]
        if len(b) >= len(a):
            i += 1
        else:
            city_list.remove(b)
            city_list.append(b)
    return city_list
cities_organized()

def four_letter_animals():
    i = 0
    while i < len(animal_list):
        if len(animal_list[i]) == 4:
            print(animal_list[i])
        i = i + 1
four_letter_animals()
