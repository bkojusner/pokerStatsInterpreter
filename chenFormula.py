import sys
import math

while True:
  print("~~~~~~~~~~~~~~~~~~~~~~~~")
  print("~~Chen~Poker~Calculator~")
  print("~~~~~~~~~~~~~~~~~~~~~~~~")
  #Get our input values stored into txt
  txt = input("Hand: ")
  if txt.lower() == "exit":
    sys.exit("Successfully Exited")
  x = txt.split()
  value = 0
  string = ""

  #Loop to convert letters to numbers
  for j in x:
    if j.lower() == "a":
      string = string + "14 "
    elif j.lower() == "k":
      string = string + "13 "
    elif j.lower() == "q":
      string = string + "12 "
    elif j.lower() == "j":
      string = string + "11 "
    else:
      string = string + j + " "

  #Formatting string for next loop
  y = string.split()

  #Check that the first card is greater than
  if int(y[0]) < int(y[1]):
    temp = y[0]
    y[0] = y[1]
    y[1] = temp

  #Deficiency points for space between cards
  minus = 0

  #Ensures our number will be negative
  minus = int(y[0]) - int(y[1]) - 1
  if minus == -1:
    minus = minus + 1
  firstMinusCheck = int(y[0])
  secondMinusCheck = int(y[1])

  #If 14 then give it a value 10
  if int(y[0]) == 14:
    value = value + 10
  #If in range 11 thru 13 subtract 5
  elif int(y[0]) >= 11 and int(y[0]) <= 13:
    value = value + int(y[0]) - 5
  elif int(y[0]) <= 10:
    value = value + int(y[0]) * 0.5
  if y[0] == y[1]:
    value = value * 2
    if value < 5:
      value = 5

  #If suited letter appears then add 2
  if len(y) == 3:
    value = value + 2

  #Last special case included
  if minus < 2 and int(y[0]) < 12 and int(y[1]) < 12:
    if int(y[0]) != int(y[1]):
      value = value + 1

  if minus >= 4:
    minus = 5 * -1
  else:
    minus = minus * -1

  #Only calculate deficiency if number card
  if firstMinusCheck < 11 or secondMinusCheck < 11 and minus != 0:
    value = value + minus

  #Give us our value
  print("Rating: " + str(math.ceil(value)))

  size = input("[F]ull ring (10) or [S]hort handed (6): ")
  position = input("[E]arly, [M]id, or [L]ate position: ")

  if position.lower() == "e":
    pos = 0
  elif position.lower() == "m":
    pos = 1
  elif position.lower() == "l":
    pos = 3

  if size.lower() == "f":
    if value < 10 - pos:
      verdict = "fold"
    elif value >= 10 - pos and value < 12 - pos:
      verdict = "consider calling a raise"
    elif value >= 12 - pos:
      verdict = "raise or reraise"

  if size.lower() == "s":
    if pos == 3: 
      pos = pos - 1
    if value < 9 - pos:
      verdict = "fold"
    elif value >= 9 - pos and value < 11 - pos:
      verdict = "consider calling a raise"
    elif value >= 11 - pos:
      verdict = "raise or reraise"

  print("verdict: " + verdict)
