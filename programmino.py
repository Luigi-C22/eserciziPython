# il primo programma con python

robot_name = "Chappie"
robot_age = 1
print("Ciao! il mio nome è " + robot_name + " e ho " + str(robot_age) + " anno")

user_name = input("Tu come ti chiami? ")
print("ciao " + user_name + "!")

user_age = int(input("Quanti anni hai? "))
age_difference = user_age - robot_age # Differenza di eta

print(str(user_age) + " anni!? Sono " + str(age_difference) + " più di me!")
print("A presto")