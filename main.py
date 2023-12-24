# This function returns the key for the matching organ description
def get_key_by_value(organ_description):
  for organkey, organvalue in organs.items():
    if organvalue == organ_description:
      return organkey


# This function retuns the organ description based on the choosen difficulty
def o_description(difficulty):
  if difficulty == "EASY":
    print()
    print(
      "You have chosen the EASY level. Each question will be multiple choice. Please choose the correct answer from the ones presented! "
    )
    print("""
        Choose from the possible answers: 

        Pancreas, Liver, Diaphragm, Cerebellum, Kidney
        """)
    # Returns first organ descriptoion from the organ dictionary
    for key, value in organs.items():
      return value
  elif difficulty == "HARD":
    print("You have chosen the HARD level. Each question will be open-ended.")
    for key, value in organs.items():
      return value
      print()


# Provides the first letter of oragan name as the hint based the matching organ description
def hint_system(guess, organ_description):
  # get the organ name by matching organ description from the organ dictionary
  key = get_key_by_value(organ_description)
  print("The first letter of the organ starts with " + key[0])


# Checking whether the guess matches organ name
def validating_key(guess):
  for key in organs:
    if key == guess:
      return True
    else:
      return False


#validate the guess and return true or false
def validate_guess(guess, organ_description, attempts):
  validate = False
  #loop untill attempts is less than three
  while attempts < 3 and validate == False:
    if guess == get_key_by_value(organ_description):
      print("Your guess is correct! Good Job!")
      validate = True
    else:
      hint_choice = input("Need a hint? Yes or No?: ")
      print()
      if hint_choice.lower() == "yes":
        # generate hint
        hint_system(guess, organ_description)
        print()
        guess = input("Please try again! What is the NAME of this ORGAN? ")
        attempts += 1

      elif hint_choice.lower() == "no":
        # ask user to guess again
        guess = input(
          "Your guess is INCORRECT! Please try again! What is the NAME of this ORGAN? "
        )
        attempts += 1


# 'Name that organ' game instructions.
print("""
Hello Player! Welcome to 'Name that Organ'!

In this game, the description of an organ is displayed. GUESS the organ to win! 
Good luck Player!

First, you must choose the difficulty level to proceed. 
""")

organs = {
  # Taken from WebMd website
  "Pancreas":
  "This organ synthesizes enzymes that breaks down sugar, fats and starches.",
  # Taken from Stanford Medicine
  "Liver":
  "This organ makes bile, which carries away waste and break down fats in the small intestine during digestion.",
  # Taken from Cleveland Clinic
  "Diaphragm":
  "This organ is a thin, dome-shaped muscle that sits below your lungs and heart to help you inhale and exhale.",
  # Taken from Medical News Today
  "Cerebellum":
  "This organ is particularly responsible for muscle control, including balance, coordination, and movement.",
  # Taken from NHS
  "Kidney":
  "This organ cleanses the toxins in the blood and transforms the waste into urine."
}

# Asking user for preferred difficulty level
difficulty = str(
  input("What level of difficulty do you prefer, EASY or HARD: "))

# The difficulty options provided are "EASY" or "HARD"
while difficulty != "EASY" and difficulty != "HARD":
  difficulty = str(
    input("""
INVALID RESPONSE!
What level of difficulty do you prefer, EASY or HARD: """))

# If difficulty is EASY, then the multiple choice answers are also displayed
if difficulty == "EASY":
  organ_description = o_description(difficulty)
  print()
  print("Function: \n" + str(organ_description))
  print()
  # ask user to guess the organ name
  guess = input("Name that organ!: ")
  attempts = 1
  # validate guess
  checker = validate_guess(guess, organ_description, attempts)
  print()
  #game over

elif difficulty == "HARD":
  organ_description = o_description(difficulty)
  print()
  print("Function: \n" + str(organ_description))
  print()
  guess = input("Name that organ!: ")
  attempts = 1
  checker = validate_guess(guess, organ_description, attempts)

# replay the game
play_again = input("Do you want to play again? Yes or No? ")
print()
if play_again.lower() == "no":
  print("Thank you for playing!")


#play the second round
def re_play(play_again):
  if play_again.lower() == "yes":
    for key, value in organs.items():
      #print(key)
      if key == "Liver":
        return value

#replay
replay = re_play(play_again)
print("Function: \n" + str(replay))
print()
guess = input("Name that organ!: ")
print()
checker = validate_guess(guess, replay, attempts)
'''
Citing Sources for organs Dictionary:
1. https://www.webmd.com/digestive-disorders/what-is-pancreas#:~:text=This%206%2D%20to%2010%2Dinch,when%20to%20empty%2C%20and%20more.
2. https://columbiasurgery.org/liver/liver-and-its-functions#:~:text=The%20liver%20filters%20all%20of,lobules%20(or%20small%20lobes).
3. https://my.clevelandclinic.org/health/body/21578-diaphragm#:~:text=The%20diaphragm%20is%20a%20muscle%20that%20helps%20you%20inhale%20and,below%20your%20lungs%20and%20heart.
4.https://www.medicalnewstoday.com/articles/313265#summary
5.https://www.nhs.uk/Livewell/Kidneyhealth/Documents/kidney%20guide.pdf
'''