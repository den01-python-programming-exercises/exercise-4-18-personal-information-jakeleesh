from personal_information import PersonalInformation

def main():
    #write your code below this line
    people = []
    while True:
        first = input("First Name:")
        if not first:
            break
        last = input("Last Name:")
        id = input("Identification Number:")
        person = PersonalInformation(first, last, id)
        people.append(person)
    

if __name__ == '__main__':
    main()
