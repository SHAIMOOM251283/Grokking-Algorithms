voted = {}

def check_voter(name):
    if voted.get(name):
        print("Kick them out!")
    else:
        voted[name] = True
        print("Let them vote!")

def main():
    while True:
        name = input("Enter a name (type 'quit' to exit): ")
        if name.lower() == 'quit':
            break
        check_voter(name)

if __name__ == "__main__":
    main()


# Hardcoded function calls with names
#check_voter("tom")
#check_voter("mike")
#check_voter("mike")
