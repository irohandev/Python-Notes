# 6. Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance 
# (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

dist = int(input("Enter the distance in KM = "))

if dist < 3:
    print("You should travel by walking.")

elif dist <= 15:
    print("You should travel by bike.")
    
else:
    print("You should travel by car.")