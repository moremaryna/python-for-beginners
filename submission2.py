hour = int(input("Enter the time you have arrived: ")) # User enters hour as a number
guard = False; # Guard is not here today

if hour >= 7 and hour <= 17: #Check the condition if the arrival is between 7.00AM and 5.00PM
  print("You're in!")
  
else: #Cover any other hours of arrival
  print("Wait for guard to ask permission to enter")
