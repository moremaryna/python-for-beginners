#To create our application, we want to read the distance from the sun for two planets, and then display the distance between the planets. We'll do this by using input to read the values, int to convert to integer, and then abs to convert the result into its absolute value.

#Start by adding the code to prompt the user for the distance between the sun and the first planet, and then the second. Store each result in variables named first_planet_input and second_planet_input.

first_planet_input = input("What's the distance to the first planet in km?")
second_planet_input = input('What\'s the distance to the second planet in km?')

# Because input returns string values, we need to convert them to numbers. Add the code to convert each input into an integer using int. Store the values in first_planet and second_planet respectively.

first_planet = int(first_planet_input)
second_planet = int(second_planet_input)

# With your values stored as numbers, you can now add the code to perform the calculation, subtracting the first planet from the second. Because the second planet might be a greater number, you'll use abs to convert it to an absolute value.

# Subtract first_planet from second_planet and convert the result to its absolute value by using abs. Store the result in a variable named distance_km. Then display the result on the screen.

distance_km = abs(second_planet - first_planet)
print (distance_km)