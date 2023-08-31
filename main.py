import csv
from 

class Node(object):

    def __init__(self, data):
        self.data = data

        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList(object):

    def __init__(self):

        # The first Node object in the list

        self.head_node = None

        self.num_of_nodes = 0

    def list_size(self):

        return self.num_of_nodes

    def insert_at_start(self, data):

        self.num_of_nodes += 1

        new_node = Node(data)

        if self.head_node is None:  # if the list is empty

            self.head_node = new_node

        else:

            # update the references to keep the order

            new_node.next = self.head_node

            self.head_node = new_node

    # https://www.geeksforgeeks.org/given-a-linked-list-which-is-sorted-how-will-you-insert-in-sorted-way/

    def add(self, data):

        self.num_of_nodes += 1

        new_node = Node(data)

        # Check if the linked list is empty

        # Runs in Linear time

        if self.head_node is None:  # if the list is empty

            self.head_node = new_node



        elif self.head_node.data.title.lower() >= new_node.data.title.lower():

            new_node.next = self.head_node

            self.head_node = new_node



        else:

            # We have to go through the list until we find the node with None as the reference

            temp_node = self.head_node

            previous_node = self.head_node

            while temp_node is not None and temp_node.data.title.lower() < new_node.data.title.lower():
                previous_node = temp_node

                temp_node = temp_node.next

            # Edit the next node pointer on the last node to be the newly added node

            previous_node.next = new_node

            new_node.next = temp_node

    def __iter__(self):

        node = self.head_node

        while node is not None:
            yield node

            node = node.next

    def __repr__(self):

        output = ""

        current_node = self.head_node

        while current_node is not None:
            output += current_node.__repr__() + "\n"

            current_node = current_node.next

        return output

    # https://www.geeksforgeeks.org/binary-search-on-singly-linked-list/

    def lookup(self, keyword):

        matches = []

        for node in self:

            if keyword in node.data.title or keyword in node.data.author:
                matches.append(node.data)

        # print("Matching Books:")

        # for i in range(1, len(matches)+1):

        #     print(f"{i}: {matches[i-1]}")

        # num = int(input("Enter number to select:"))

        return matches

        # value not present

        # return None

    def save_changes(self, filename):

        # field names

        fields = ['Publisher', 'Author', 'Primary ISBN10', 'Date', 'Title', 'Weeks on list', 'Status']

        # writing to csv file

        with open(filename, 'w') as csvfile:
            # creating a csv writer object

            csvwriter = csv.writer(csvfile)

            # writing the fields

            csvwriter.writerow(fields)

            for node in self:
                row = [node.data.publisher, node.data.author, node.data.ISBN, node.data.date, node.data.title,
                       node.data.weeks_on_list, node.data.status]

                # writing the data rows

                csvwriter.writerow(row)


class Book(object):
    book_list = LinkedList()

    def __init__(self, publisher, author, ISBN, date, title, weeks_on_list):
        self.publisher = publisher

        self.author = author

        self.ISBN = ISBN

        self.date = date

        self.title = title

        self.weeks_on_list = weeks_on_list

        self.status = "In stock"

        Book.book_list.add(self)

    def __repr__(self):
        return f"{self.title} by {self.author} - {self.status}"

    @classmethod
    def check_out_book(cls):
        keyword = input("Enter keyword")

        self.status = "Checked out"

    def return_(self):
        self.status = "In stock"

    @classmethod  # designates it as a class method
    def import_books(cls, filename: str):
        with open(filename, "r") as f:
            reader = csv.DictReader(f)

            items = list(reader)

        for item in items:
            Book(

                publisher=item.get('Publisher'),

                author=item.get('Author'),  # would by default read as a string

                ISBN=item.get('Primary ISBN10'),

                date=item.get('Date'),

                title=item.get('Title'),

                weeks_on_list=int(float(item.get('Weeks on list')))

            )


if __name__ == '__main__':

# book1 = Book("Harper", "Daniel Silva", "NA",  "9/7/14", "THE HEIST", 6)

# book2 = Book("St. Martin's", "Nora Roberts", "1250123100.0",   "7/16/17", "COME SUNDOWN", 5)

# book3 = Book("Harper/HarperCollins", "Mitch Albom" , "62294415.0",  "1/10/16", "THE MAGIC STRINGS OF FRANKIE PRESTO",  5.0)

# book4 = Book("Colleen Hoover", "Colleen Hoover",  "None",  "8/26/12",  "SLAMMED", 5.0)


# Book.import_books("New York Times Bestsellers.csv")

# print(Book.book_list)

# print(Book.book_list.num_of_nodes)

#

# print(Book.book_list.lookup("ZOO"))

# Book.book_list.get_book("ZOO 2").check_out()

# Book.book_list.save_changes("New York Times Bestsellers.csv")

