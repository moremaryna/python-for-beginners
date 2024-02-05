# You will finish your program by adding the code to find any sentences which mention temperature. Add code to loop through the sentences variable. For each sentence, search for the word temperature. If the word is found, print the sentence.
name = "Ganymede"
planet = "Mars"
gravity = 1.43

#Now you will create the template to display the information about the moon. You want the output to look like the following:

# Gravity Facts about {name}
# --------------------------
# Planet Name: {planet}
# Gravity on {name}: {gravity} m/s2

template = """Now you will create the template to display the information about the moon. You want the output to look like the following:

Gravity Facts about {name}
--------------------------
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2"""

# With the template created, it's time to use it to display information about the moon! Use the format function on template to use the template and print the information. Set name, planet, and gravity to the appropriate values.

print(template.format(name=name, planet=planet, gravity=gravity))