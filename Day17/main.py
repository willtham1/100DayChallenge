from getpass import getpass as input


print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()
print("Select your move (R, P or S)")
print()
#hint: create these variables outside loop and then add += with correct player to keep score throughout
player1_score = 0
player2_score = 0
#hint: that the while loop needs to go around all code and then highlight the rest of the code and hit tab once. 
while True: 
  player1Move = input("Player 1 > ")
  print()
  player2Move = input("Player 2 > ")
  print()
  
  if(player1Move=="R"):
    if(player2Move=="R"):
      print("You both picked Rock, draw!")
    elif(player2Move=="S"):
      print("Player1 smashed Player2's Scissors into dust with their Rock!")
      player1_score += 1
    elif(player2Move=="P"):
      print("Player1's Rock is smothered by Player2's Paper!")
      player2_score += 1
  elif(player1Move=="P"):
    if(player2Move=="R"):
      print("Player2's Rock is smothered by Player1's Paper!")
      player1_score += 1
    elif(player2Move=="S"):
      print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
      player2_score += 1
    elif(player2Move=="P"):
      print("Two bits of paper flap at each other. Dissapointing. Draw.")
  elif(player1Move=="S"):
    if(player2Move=="R"):
      print("Player 2's Rock makes metal-dust out of Player1's Scissors")
      player2_score += 1
    elif(player2Move=="S"):
      print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
    elif(player2Move=="P"):
      print("Player1's Scissors make confetti out of Player2's paper!")
      player1_score += 1
  
# hint: make sure you add player scores at the end of all the options but still inside the while loop.
  print("Player 1 has", player1_score, "wins.")
  print("Player 2 has", player2_score, "wins.")

  if player1_score==3 or player2_score==3:
    print("Thanks for playing!")
    exit()
  else:
    continue
  
  ## Day17 improvements to day 14 rock paper scissors