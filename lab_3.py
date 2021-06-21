groceries_list = {"chicken":1.59, "beef": 1.99, "cheese": 1.00, "milk" : 2.50}
NBA_players = {"Lebron James": 23, "Kevin Durrant":35, "Stephen Curry": 30, "Damian Lillard" :0  }
phone_numbers = {"friend1" : 1234567, "friend2": 2942784, "friend3": 2849472, "friend4": 23927429}
shoe_inventory={"jordan13": 1,"yeezy" :8, "foamposite": 10, "airmax": 5, "sbdunk": 20}


NBA_players["Lebron James"] = 6 
jersey_number=NBA_players ["Lebron James"]
print(jersey_number)

NBA_players["Lebron James"] -= 17
jersey_number=NBA_players ["Lebron James"]
print (jersey_number)

chicken_price = groceries_list ["chicken"]
print (chicken_price)

beef_price = groceries_list ["beef"]
print (beef_price)

cheese_price = groceries_list ["cheese"]
print (cheese_price)

milk_price = groceries_list ["milk"]
print (milk_price)

friend1_number = phone_numbers[friend1]
print (friend1_number)
friend2_number = phone_numbers[friend2]
print (friend2_number)
friend3_number = phone_numbers[friend3]
print (friend3_number)
friend4_number = phone_numbers[friend4]
print (friend4_number)

shoe_inventory["Jordan_13"] = 5
Jordan_13_amount = shoe_inventory["Jordan_13"]
print(Jordan_13_amount)
shoe_inventory["Yeezy"] = 13
Yeezy_amount = shoe_inventory["Yeezy"]
print(Yeezy_amount)
shoe_inventory["Foamposite"] = 14
Foamposite_amount = shoe_inventory["Foamposite"]
print(Foamposite_amount)
shoe_inventory["Air_Max"] = 9
Air_Max_amount = shoe_inventory["Air_Max"]
print(Air_Max_amount)
shoe_inventory["SB_Dunk"] = 22
SB_Dunk_amount = shoe_inventory["SB_Dunk"]
print(SB_Dunk_amount)
#Slide 11
Food_price1 = {"pasta": 2.53, "juice": 3.54, "tea": 1.09}
groceries_list.update(Food_price1)
print(groceries_list)


NBA_players1 = {"player1": 5, "player2": 12, "player3": 35}
NBA_players.update(NBA_players1)
print(NBA_players)
People_PhoneNumber1 = {"friend5": 3245498883, "friend6": 4133285489, "friend7": 4135482390}
phone_numbers.update(People_PhoneNumber1)
print(phone_numbers)
Shoe_amount1 = {"Nikes": 20, "Jordans": 10, "Flip_Flops": 35}
shoe_inventory.update(Shoe_amount1)
print(shoe_inventory)



del groceries_list["Bean"]
del groceries_list["Beef"]
print(groceries_list)
del NBA_players["Dude"]
del NBA_players["Cool"]
print(NBA_players)
del phone_numbers["Sam"]
del phone_numbers["Bob"]
print(phone_numbers)
del shoe_inventory["Nikes"]
del shoe_inventory["Yeezy"
print(shoe_inventory)
