import os


# Specify the parent directory where you want to create the new folder
parent_directory = r"C:\Users\anders.hoelstad\Documents\GitHub\GuessingGame-FileMakerPY"

# Specify the name of the new folder you want to create
new_folder_name = "mappeMedVeldigViktigeFiler;)"
new_file_name = "veldigViktigFil;).txt"

# Combine the parent directory and new folder name to create the full path
new_folder_path = os.path.join(parent_directory, new_folder_name)
new_file_path = os.path.join(new_folder_name, new_file_name)

# Check if the directory already exists

def makeFile():
    if not os.path.exists(new_folder_path):  # Corrected this line
        os.makedirs(new_folder_path)
        print(f"Directory {new_folder_path} er på plass !")
    else:
        print(f"Directory {new_folder_path} er allerede på plass !")

    if not os.path.exists(new_file_name):
        with open(new_file_path, "w") as file:
            file.write("Veldig viktig fil, kan ikke slettes.\n")
        print(f"{new_file_name} er på plass !")
    else:
        print(f"{new_file_name} er allerede å plass")
        
    print("alt på plass sjef")
makeFile()