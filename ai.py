# Generated using microsoft copilot
#Great! You can replace `"data.csv"` in the previous Python program with the path to your actual CSV file. Here's the updated code:



class Node:
    def __init__(self, country=None, currency=None, next=None):
        self.country = country
        self.currency = currency
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, country, currency):
        if not self.head:
            self.head = Node(country, currency)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(country, currency)

    def display(self, country):
        current = self.head
        while current:
            if current.country == country:
                return current.currency
            current = current.next
        return "Country not found"

import csv

def create_linked_list(file_name):
    linked_list = LinkedList()
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            linked_list.insert(row[0], row[1])
    return linked_list

file_name = r"data.csv"
linked_list = create_linked_list(file_name)

country = input("Enter a country: ")
print("The local currency of", country, "is", linked_list.display(country))

# This program will read data from the CSV file at the location you provided and create a linked list of countries and their local currencies. It will then ask you to input a country and display that country's local currency. Please note that this program doesn't handle exceptions. You might want to add error handling code for a robust solution. Also, make sure the CSV file at the location you provided has two columns: the first one for the country and the second one for the local currency. If the file is not in this format, the program might not work as expected. If you have any other questions or need further assistance, feel free to ask!