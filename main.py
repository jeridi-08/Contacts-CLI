from os import system, name
import os
import pickle

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def seperators(length):
    if length > 0:
        seperator = "_"
        for i in range(length - 1):
            seperator = seperator + "_"
        return seperator
    else:
        return ""


def center(string, length):
    newstring = string
    if int((length - len(string)) / 2) <= 0:
        return string
    else:
        newstring = string
        for i in range(int((length - len(string)) / 2)):
            newstring = " " + newstring + " "
        return newstring


def validity(phonenumber):
    phonenumber = phonenumber + "i"
    validityscore = 0
    while ord(phonenumber[validityscore]) >= 48 and ord(phonenumber[validityscore]) <= 57:
        validityscore += 1
    if validityscore == 4 or validityscore == 5:
        if phonenumber[validityscore] == " ":
            validityscore += 1
            while ord(phonenumber[validityscore]) >= 48 and ord(phonenumber[validityscore]) <= 57:
                validityscore += 1
            if validityscore == 11 or validityscore == 12:
                return True
            else:
                return False
    return validityscore


def createContact(contacts,contact_name,contact_number,contact_favourites):
    class Contacts:
        def __init__(self, name, number, favourites):
            self.name = name
            self.number = number
            self.favourites = favourites
    contact = Contacts(contact_name,contact_number,contact_favourites)
    contacts.append(contact)
    return contacts

allContacts = []
seperatorLength = 50
def mainPage():
    inputValue = 0
    repeatedTimes = 0
    while inputValue != "c" and inputValue != "v" and inputValue != "f" and inputValue != "r" and inputValue != "s" and inputValue != "q":
        clear()
        if repeatedTimes > 0:
            print("not a valid option, try again\n\n")
        print(seperators(seperatorLength) + "\n")
        print(center("Contacts", seperatorLength) + "\n")
        print("create new contact (c)\nview contacts (v)\ncreate save file (f)\nrestore save file (r)\nsettings (s)\nquit (q)\n")
        inputValue = input()
        repeatedTimes += 1
    return inputValue
inputValue = 0
while inputValue != "q":
    inputValue = mainPage()
    if inputValue == "c":
        clear()
        print(seperators(seperatorLength) + "\n")
        print(center("Name your contact", seperatorLength) + "\n")
        contactName = input()
        clear()
        print(seperators(seperatorLength) + "\n")
        print(center("What is " + contactName + "'s phone number?", seperatorLength) + "\n")
        contactNumber = input()
        if not validity(contactNumber):
            while not validity(contactNumber):
                clear()
                print("invalid phone number\n")
                print(seperators(seperatorLength) + "\n")
                print(center("Name your contact", seperatorLength) + "\n")
                contactName = input()
                clear()
                print(seperators(seperatorLength) + "\n")
                print(center("What is " + contactName + "'s phone number?", seperatorLength) + "\n")
                contactNumber = input()
        contactFavourites = 0
        if contactFavourites != "y" and contactFavourites != "n":
            clear()
            print(seperators(seperatorLength) + "\n")
            print(center("Is this contact one of your favourites?", seperatorLength) + "\n")
            print(center("(y/n)", seperatorLength) + "\n")
            contactFavourites = input()
        allContacts = createContact(allContacts,contactName,contactNumber,contactFavourites)

    if inputValue == "v":
        clear()
        print(seperators(seperatorLength) + "\n")
        print(center("Favourites", seperatorLength) + "\n")
        for i in range(len(allContacts)):
            if allContacts[i].favourites == "y":
                print(center(allContacts[i].name + " ("+str(i)+")", seperatorLength) + "\n")
        print(center("All other contacts", seperatorLength) + "\n")
        for i in range(len(allContacts)):
            if allContacts[i].favourites == "n":
                print(center(allContacts[i].name + " ("+str(i)+")", seperatorLength) + "\n")
        contactInput = int(input())
        clear()
        print(seperators(seperatorLength) + "\n")
        print(center(allContacts[contactInput].name+":", seperatorLength) + "\n")
        print(center("Number: " + allContacts[contactInput].number, seperatorLength) + "\n")
        input()
    if inputValue == "s":
        clear()
        print(seperators(seperatorLength) + "\n")
        print(center("Settings", seperatorLength) + "\n")
        print("change seperator length (c)")
        if input() == "c":
            clear()
            print(seperators(seperatorLength) + "\n")
            print(center("Input new seperator length", seperatorLength) + "\n")
            seperatorLength = int(input())
    if inputValue == "f":
        print("Saving...")
        with open('save.txt', 'wb') as saveFile:
            for i in range(len(allContacts)):
                pickle.dump([allContacts[i].name,allContacts[i].number,allContacts[i].favourites], saveFile, protocol=2)
    if inputValue == "r":
        print("Loading...")
        with open('save.txt', 'rb') as saveFile:
            contactDetails = (pickle.load(saveFile))
        for i in range(0,len(contactDetails),3):
            createContact(allContacts, contactDetails[i], contactDetails[i+1], contactDetails[i+2])

quit()