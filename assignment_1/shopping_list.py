# Name:Kunam Vijay Saradhi
# Reading a csv file with books and display the completed books
import csv
import operator
import os
import sys

# function to print the menu
def print_menu():#creating a function of menu
    print("Menu:")
    print("R - List required items")
    print("C - List completed items")
    print("A - Add new item")
    print("M - Mark an item as completed")
    print("Q - Quit")


def load_data_from_csv(csvfile):
    # function to print the load the data
    shopping_list = list()
    count = 0

    if os.path.exists(csvfile):
        with open(csvfile, "r") as data:
            load_items = csv.reader(data, delimiter=",") #The method reader() reads until EOF using reader() and returns a list containing lines
            for row in load_items:
                count += 1
                row[1] = round(float(row[1]), 2)
                row[2] = int(row[2])
                shopping_list.append(row)

    print("{0} items loaded from {1}".format(count, csvfile))#print the total number of loaded items in .format
    return shopping_list


def show_items(_items):#craeting the function to show items
    for idx, each in enumerate(_items):
        print("{0}. {1: <20}$  {2:.2f} ({3})".format(idx, each[0], each[1], each[2]))#print the total number of loaded items in .format
    total = sum([item[1] for item in _items])
    print("Total expected price for {0} items: ${1:.2f}".format(len(_items), total))#print the total price of loaded items in .format


def main():#craeting the main function
    csv_file_path = "sample_input.csv"
    print("Shopping List 1.0 - by YOUR NAME WRITE HERE")#print the Shopping list

    shopping_list = load_data_from_csv(csv_file_path) #loading the data from the shopping_list
    completed_list = list() #initialising the list

    while True:
        print_menu()
        user_input = input(">>> ").upper() #initilaising the input

        if user_input == "C":
            if not completed_list:
                print("No completed items") #print the no completed items
                continue
            else:
                print("Completed items:")
                completed_list = sorted(completed_list, key=lambda x: x[2]) #sorting the initialised list
                show_items(completed_list)

        elif user_input == "R":
            if not shopping_list:
                print("No required items") #print the no required items
                continue
            else:
                print("Required items:") #print the required items
                shopping_list = sorted(shopping_list, key=lambda x: x[2]) #sorting the initialised list
                show_items(shopping_list)

        elif user_input == "M":
            if not shopping_list:
                print("No required items") #printing the no required items
                continue
            show_items(shopping_list) #declaring the show_items
            print("Enter the number of item to mark as completed") #printing the statement

            while True:
                user_selection = input(">>> ")

                if user_selection.isdigit() and int(user_selection) < len(shopping_list):
                    user_selection = int(user_selection)
                    print("{0} marked as completed".format(shopping_list[user_selection][0]))
                    #printing the "marked as complete" in .format
                    shopping_list[user_selection][3] = "c"
                    completed_list.append(shopping_list[user_selection])
                    #adding the completed_list to the shopping_list
                    del shopping_list[user_selection]
                    break
                elif not user_selection.isdigit():
                    print("Invalid input; enter a number")
                    #printing the invalid input
                elif user_selection.isdigit() and int(user_selection) >= len(shopping_list):
                    print("Invalid item number")
                    #print invalid item number

        elif user_input == "A":
            while True:
                item_name = input("Item name: ") #initilaising the input
                if not item_name.strip():
                    print("Input can not be blank") #printing the statement
                else:
                    item_name = item_name.strip() #declaring the input name
                    break

            while True:
                item_price = input("Price: $") #initilaising the input
                if not item_price.strip():
                    print("Input can not be blank") #printing the statement
                elif not item_price.isdigit() and item_price[0] == "-":
                    print("Price must be >= $0")
                elif item_price.isdigit():
                    item_price = int(item_price.strip()) #declaring the item_price
                    break

            while True:
                item_priority = input("Priority : ") #initilaising the input
                if not item_priority.strip():
                    print("Input can not be blank") #printing the statement
                elif not item_priority.isdigit():
                    print("Invalid input; enter a valid number") #printing the statement
                elif item_priority.isdigit() and (int(item_priority) == 0 or int(item_priority) >= 4): #declaring the item_priority
                    print("Priority must be 1, 2 or 3") #printing the statement
                else:
                    item_priority = int(item_priority.strip()) #declaring the item_priority to integer
                    break

            print("{0}, ${1:.2f}, (priority {2}) added to shopping list".format(item_name, item_price, item_priority))
            ##printing the items to shopping list in .format
            shopping_list.append([item_name, item_price, item_priority, "r"]) #adding in to the shopping list
            shopping_list = sorted(shopping_list, key=lambda x: x[2]) #sorting the shopping the shopping_list

        elif user_input == "Q":
            with open("items.csv", "w") as outputcsv:
                writer = csv.writer(outputcsv, delimiter=",") ##The method writer() reads until EOF using reader() and returns a list containing lines
                for item in completed_list:
                    writer.writerow(item)
            print("{0} items saved to items.csv".format(len(completed_list)))
            #printing the completed_list in .format
            print("Have a nice day :)")
            #printing the statement
            break

        else:
            print("Invalid menu choice")
            #printing the statement
            continue


if __name__ == "__main__":
    main()