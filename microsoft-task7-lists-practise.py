# First, create a variable named planets. Add the eight planets (without Pluto) to the list. The planets are:

# Mercury
# Venus
# Earth
# Mars
# Jupiter
# Saturn
# Uranus
# Neptune
# Finish by using print to display the list of planets.
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print(planets)
# Next, display the total number of planets by using len and print.

print(len(planets))

# Finally, add Pluto to the list that you created. Then display both the number of planets and the last planet in the list.
planets.append("Pluto")
print(len(planets), "this is total number of planets")
print(planets[-1], "this is the last planet")

