# Exercises
# 1) Build a Shopping Cart
# You can use either lists or dictionaries. The program should have the following capabilities:

# 1) Takes in input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list



# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?

def my_func():
    shopping_cart = []

    while True:
        print("\nWhat would you like to do: \n1 - Show Cart\n2 - Add Item\n3 - Delete Item\n4 - Quit and Checkout")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Here is your current shopping cart:\n\n", shopping_cart)
        elif choice == "2":
            item = input("Enter item to add to your cart: ")
            shopping_cart.append(item)
            print(f"{item.title()} added to your cart.")

        elif choice == "3":
            item = input("Enter item to remove from your cart: ")
            if item in shopping_cart:
                shopping_cart.remove(item)
                print(f"{item.title()} removed from your cart.")

        elif choice == "4":
            print("Proceed to Checkout:", shopping_cart)
            break
        else:
            print("I'm sorry. Please type: 1, 2, 3, or 4 to continue.")

my_func()
        


# 2) Set Practice
# Remove all duplicates from the following list

nums_list = [1, 1, 1, 2, 2, 3, 5, 6, 4, 12, 11, 12, 12, 14, 16, 16, 16, 1, 1, 1, 2, 2]

my_set = set(nums_list)
print(my_set)


# Output the intersection of the following the following sets.

set1 = {20, 24, 26, 27}
set2 = {26, 35, 63, 27}

set3 = set1 & set2
print(set3)


# Output the difference between the following sets


set3 = {100, 65, 89, 200}
set4 = {65, 103, 54, 200}

set6 = set3 - set4
set7 = set4 - set3

set8 = set6 | set7

print(set8)