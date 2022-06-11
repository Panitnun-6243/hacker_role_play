print('''
#                      .........
#                    .'------.' |       Hack now!
#                   | .-----. | |
#                   | |     | | |
#                 __| |     | | |;. _______________
#                /  |*`-----'.|.' `;              //
#               /   `---------' .;'              //
#              /  /.////////; / /               //
#             /  / ######### //                //|
#            /  / ######### //                //||
#           /   `-----------'                // ||
#          /________________________________//| ||
#          `--------------------------------' | ||
#           : | ||      | || |__LL__|| ||     | ||
#           : | ||      | ||         | ||     `""'
#           n | ||      `""'         | ||
#           M | ||                   | ||
#             | ||                   | ||
#             `""'                   `""'

''')
print("Welcome to Hacker role play.\n")
print("Your mission is to hack this computer before cybersecurity team found you.") 

choice1 = input('You\'re in terminal. What choice you want to choose (hack in that dir or change to another directory)? Type "hack" or "cd" \n').lower()
if choice1 == "cd":
  choice2 = input('You\'ve come to the right directory. You need to choose 1 of 2 approach to hack. Type "virus" to spread instantly. Type "malware" to insert dangerous software. \n').lower()
  if choice2 == "malware":
    choice3 = input("Perfect choice! let finish by choose an appropriate malware. One spyware, one ransomware and one worms. Which type do you choose? \n").lower()
    if choice3 == "worms":
      print("Inappropriate malware, you got caught. Game Over.")
    elif choice3 == "ransomware":
      print("This computer is on your control! You Win!")
    elif choice3 == "spyware":
      print("Inappropriate malware, you got caught. Game Over.")
    else:
      print("You didn't choose any malware, out of time. Game Over.")
  else:
    print("Wrong approach! Game Over.")
else:
  print("You got caught by security team. Game Over.")