#KeyError
#IndexError
#TypeError

try:
    # Code and logic goes here
    file = open("a_file.txt")

    a_dictionary={"key":"Value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    # Handle exception here
    # print("There was an error")
    file = open("a_file.txt","w")
    file.write(("Something"))
except KeyError as error_message:
    print(f"the Key {error_message} does not exist")
except:
    print("Unknown error")
else:
    # If there is no exception, after try it comes here comes here
    print("File exist and operate on it")
finally:
    # If exception or not code here
    # print("If error or not code here")
    file.close()
    #custom exceptions

try:
    height = float(input("Height:"))
    weight = float(input("Weight"))

    if height>3:
        raise ValueError("Unrealistic height")
except ValueError as message:
    print(message)
else:
    bmi = weight / height ** 2
    print(f"Your BMI is {bmi}")
finally:
    pass
