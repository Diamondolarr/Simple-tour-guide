import time
import sys

def guides():
    print("WELCOME TO THE APOSTASYS ADVENTURE")
    time.sleep(1)
    print("The beginning is always the hardest")
    time.sleep(1)
    return

def welcome():
    name = input("enter your name: ")
    print(name)
    age = int(input(f"Dear {name}, enter your age:" ))
    print(age)
    if not age >= 18:
        print(f"Dear {name}, you are not eligible to use this software. Exiting....")
        sys.exit()
        print("exiting program")
    else:
        print(f"Welcome {name}, we will start the journey to the ultimate adventure in a moment")
        time.sleep(2)
        return name, age
    
def ask_guide(name):
    guide = input(f"Would you like to get the guide {name} (yes/no): ")
    if guide == "yes":
        print("Staring the beginner's guide")
        time.sleep(2)
        guides()
    elif guide =="no":
        print("Skipping the guide")
    else:
        print(f"{guide} is not a valid response")
        ask_guide(name)

def knowledge(name, age):
    first_time = input("Is your first time here?(yes/no): ")
    if first_time == "yes":
       ask_guide(name)
    elif first_time == "no":
        print(f"Welcome Back {name}")
        return
    else:
        print("invalid response")
        knowledge(name, age)
def fun():
    print(f"\n What would you like to do")
    print("1. Climb mountains")
    print("2. Ride a bicycle")
    print("3. Visit the temples")
    print("4. Play golf")

    choice = input("Enter your preferred choice: ")
    if choice == "1":
        print("You choose to climb mountains")
        time.sleep(1)
        print(f"\n What mountain are you visiting(select from the options below)")
        print("1. Himallayas mountain")
        print("2. Everest Mountain")
        print("3. Olumo Rock")
        print("4. Fiji Mountain")
        
    elif choice == "2":
        print("You choose to ride bicycle")
    elif choice == "3":
        print("You choose to visit the temples")
    elif choice == "4":
        print("You choose to play golf")
    else:
        print(f"{choice} is an invalid choice. Kindly select a valid option from the listed options 1-4.....")
        fun()


def main():
    name, age = welcome()
    knowledge(name, age)
    fun()
    
main()