from src.mouseinput import MouseInput
from src.bot import Bot


def main():

    print("Welcome to Autoclicker v.1")
    train_or_deploy = input("What are we doing today? (train) (deploy): ")

    # Split form train or deploy option
    if train_or_deploy == "train":
        # Initializing Variables
        file_name_train = input("File name: ")
        number_of_clicks = input("Number of clicks (type -1 for continuous clicking): ")
        # If statement for number of clicks

        print("Begin clicking! (Scroll the mouse-wheel when complete)")
        mouse_train = MouseInput(file_name_train, number_of_clicks)
        print("Stopped")
    elif train_or_deploy == "deploy" or "2":

        file_name_deploy = input("Please input file name (add .json please): ")
        number_of_loops = int(input("Number of loops (type -1 for infinite loop): "))

        print(f"Using {file_name_deploy} as file input with {number_of_loops} number of loops.")
        print("Beginning clicking.")

        mouse_clicker = Bot(file_name_deploy, number_of_loops)

        mouse_clicker.loop()
        print(f"Finished {number_of_loops} loops")
    else:
        print("Please select option (train or 1) (deploy or 2): ")