# Contact Book Management System

import os
import csv

print("Welcome to Contact Book Management System\n")
contacts = []
properties = ["Name", "Email", "phone_num", "address", ]


def load_from_database():
    global contacts
    if os.path.exists("all_books.csv"):
        with open("all_books.csv", "r") as read_file:  
            content = csv.reader(read_file)
            contacts.clear()
            for row in content:
                contacts.append(row)

    else:
        print("all_books.csv file not found! try adding some book(s)\n")


def show_books():
    global contacts
    if len(contacts) < 2:
        print("list is empty, try adding some\n")
    else:
        for i in range(0, len(contacts)):
            if i == 0:
                print("  ", contacts[0])
            else:
                print(f"{i})", contacts[i])
        print()


book = {
    'Name': 'Name',
    'Email': 'Email',
    'phone_num': 'phone_num',
    'address': 'address'
}


def input_book():
    book["Name"] = input("Enter your name: ")
    book["Email"] = input("Enter your email: ")
    book["phone_num"] = int(input("Enter your phone number: "))
    book["address"] = input("Enter your address: ")  


def save_it():
    global contacts
    new_book = []
    input_book()
    if len(contacts) == 0:
        contacts.append(properties)
    for value in book.values():
        new_book.append(value)
    contacts.append(new_book)
    with open("all_books.csv", mode="w", newline='') as write_file:
        csv_writer = csv.writer(write_file)
        csv_writer.writerow(properties)
        for i in range(1, len(contacts)):
            csv_writer.writerow(contacts[i])

    load_from_database()
    print("Book added to database!\n")


def edit_it():
    global contacts
    new_book = []
    if len(contacts) < 2:
        print("Book list is empty so you cant edit any. add some book(s) first")
    else:
        print("The Book list is : ")
        show_books()
        select = int(input("Select the number from the above list, which you want to edit : "))
        if 1 <= select <= len(contacts):
            input_book()
            for value in book.values():
                new_book.append(value)
            books[select] = new_book
            with open("all_books.csv", mode="w", newline='') as write_file:
                csv_writer = csv.writer(write_file)
                csv_writer.writerow(properties)
                for i in range(1, len(contacts)):
                    csv_writer.writerow(contacts[i])

            print(f"Book {select} edited in database!\n")
        else:
            print("invalid choice, try again.\n")


def remove_it():
    global contacts
    if len(contacts) < 2:
        print("Book list is empty so you cant remove any. add some book(s) first")
    else:
        print("The Book list is : ")
        show_books()
        select = int(input("Select the number from the above list, which you want to delete : "))
        if 1 <= select <= len(contacts):
            # remove at index:
            contacts.pop(select)
            # remove from database:
            with open("all_books.csv", mode="w", newline='') as write_file:
                csv_writer = csv.writer(write_file)
                csv_writer.writerow(properties)
                for i in range(1, len(contacts)):
                    csv_writer.writerow(contacts[i])

            print(f"Book {select} removed from database!\n")
        else:
            print("invalid choice, try again.\n")


while True:
    print("Please select an option from below : ")
    print("0. close app")
    print("1. view all contacts")  
    print("2. add new contacts")
    print("3. edit your contacts")
    print("4. remove your contact")
    print()
    selected = input("please enter a choice : ")

    if selected == "0":
        print("Thank You for using our Contact Book Management System")
        break

    elif selected == "1":
        load_from_database()
        show_books()

    elif selected == "2":
        save_it()

    elif selected == "3":
        edit_it()

    elif selected == "4":
        remove_it()

    else:
        print("invalid choice, please try again\n")