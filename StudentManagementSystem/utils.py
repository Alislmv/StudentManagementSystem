def getInt(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Error, please enter int value.")


def getFloat(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Error, please enter float value.")

def getText(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("Field cannot be empty!")