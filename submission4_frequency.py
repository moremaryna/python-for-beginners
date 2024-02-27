phrase = "You can have data without information, but you cannot have information without data" # Initial phrase for analysis
phrase = phrase.lower() # Make phrase in lower case

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] # Provide alphabet

# make a loop to count presence of letters and print this number
for letter in alphabet:
    frequency = phrase.count(letter) 
    
    if frequency > 0 :
      print(letter + " : " + str(frequency))
    
