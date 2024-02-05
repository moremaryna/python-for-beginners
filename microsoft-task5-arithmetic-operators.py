# Start by creating two variables named first_planet and second_planet. Set first_planet to the distance from the sun to Earth, and second_planet for the distance from the sun to Jupiter.
first_planet = 149597870
second_planet = 778547200


#You have two variables which store the distance between each planet and a common point: the sun. You can subtract these two values to determine the distance between the planets.

# Start by adding the code to subtract first_planet from second_planet and store the result in a variable named distance_km. Display the value to the screen.

# Then add the code to convert distance_km to miles by dividing it by 1.609344 (the rough difference between miles and kilometers) and store the result in a variable named distance_mi. Display the value to the screen.

distance_km = second_planet - first_planet
distance_mi = distance_km / 1.609344
print(distance_km)
print(distance_mi)