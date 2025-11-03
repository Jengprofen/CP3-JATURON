Dist = int(input("Enter the distance in kilometers: "))
Time = int(input("Enter the time in hours: "))
#Velocity = Distance/Time
if Dist >= 1 and Time >= 1:
    print("Velocity =",Dist/Time,"km/hr")
else:
    print("Please identify distance and/or time more than 1")
