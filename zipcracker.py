# Program: Zip Cracker
# Author: spencminfeb
# Date: 20181211
# Run with python3

# Calls the zipfile module for python
import zipfile


input("This program will use a Word List to perform a dictionary attack on a Zip File.\n"
      "The ZIP file will be extracted if a password is found.\n"
      "DO NOT USE THIS PROGRAM ON UNTRUSTED FILES!\n"
      "Files will be extracted to directory where script is stored.\n"
      "Press any key to continue...")




# Sets flags for validation of user input.
ValidWord = False
ValidZip = False
PassFound = False

zipfilename = ""

# Performs data validation on zip file input.
while ValidZip is False:
    zipfilename = input("Please enter path and name of Zip File: ")
    try:
        if zipfile.is_zipfile(zipfilename):
            print(zipfilename + " is a valid Zip File!")
            ValidZip = True

        elif ValidZip is False:
            print("Invalid Zip File or File Not Found!")

    except OSError:
        print("Invalid file path!")

# Performs data validation on word list provided.
while ValidWord is False:

    wordlistpath = input("Enter path and name of Word List File: ")
    try:
        with open(wordlistpath, 'r') as f:
            for line in f.readlines():
                ValidWord = True
    except FileNotFoundError:
        print("Word List file or path does not exist!.")
        continue

    except PermissionError:
        print("You do not have proper permissions to this directory!")
        continue

    except UnicodeDecodeError:
        print("Word List contains invalid characters, use a valid Word List!")
        continue

    except OSError:
        print("Invalid file path!")

# Sets a variable as the zip file
zip_file = zipfile.ZipFile(zipfilename)

# Opens the word list, looping through the lines one at a time to try and find a match.
# Loop continues until a match is found or EOF occurs.

with open(wordlistpath, 'r') as f:
    for line in f.readlines():
        password = line.strip('\n')
        try:
            zip_file.extractall(pwd=password.encode())

        except:
            print(password + " was not a match.")

        else:
            PassFound = True
            break

if PassFound is False:

    print("\nNo match was found!")

if PassFound is True:
    print("\nPassword found! Password is: " + password)
