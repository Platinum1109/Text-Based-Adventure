import time
from time import sleep

def print_output(decision):
  choice = "i"
  while (choice == "i"):
    choice = input(decision)
    if (choice in ['y', 'Y', 'Yes', 'yes', 'YES']):
      print("You go into the woods. \n")
      time.sleep(0.5)
      print("The thick foilage blocks out most of the sunlight, leaving a thin ray of light being the only thing illuminating the path.\n")
      time.sleep(0.5)
      print("Suddenly a lion appears in your path.\n")
      time.sleep(0.5)
      print("Its eyes staring into your soul, it slowly creeps towards you.")
      q1 = input("Do you run back out of the forest(a), slowly creep into the nearby bushes (b), or attack the lion(c)?\n")
      if q1 == 'a':
        print("Running as fast as you can, you dash down the path leading out of the forest.\n")
        time.sleep(0.5)
        print("Unfortunetly, the lion, being an agile animal, is faster than you.\n")
        time.sleep(0.5)
        print("It quickly chases you down and rips your head off.\n")
        time.sleep(0.5)
        print('''
     _____ _  _ ___   ___ _  _ ___  
    |_   _| || | __| | __| \| |   \ 
      | | | __ | _|  | _||    | |) |
      |_| |_||_|___| |___|_|\_|___/ 
           
        ''')

      return True
    elif (choice in ['n', 'N', 'No', 'no', 'NO']):
      print("You leave. \n")
      return False
    else:
      print("I don't understand. Please respond with 'yes' or 'no' \n")

def choice_r_l(decision):
  while True:
    pass


def main():
  print_output("Do you want to take the path to the woods? \n")



if __name__ == "__main__":
  main()