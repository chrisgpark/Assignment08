# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# CPark,3.2.2022,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
file_name = 'products.txt'
lstOfProductObjects = []
strChoice = ""

class Product:
    """Stores data about a product:
    properties:
        product_name: (string) with the products's name
        product_price: (float) with the products's standard price
    methods:
        to_string() returns comma separated product data (alias for __str__())
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
    """

    def __init__(self, prod_name, prod_price):
        try:
            self.__prod_name = str(prod_name)
            self.__prod_price = float(prod_price)
        except Exception as e:
            raise Exception("Error setting initial values:\n" + str(e))

    @property
    def prod_name(self):
        return str(self.__prod_name)

    @prod_name.setter
    def prod_name(self, value: str):
        if str(value).isnumeric():
            self.__prod_name = value
        else:
            raise Exception("Names cannot be integers")

    @property
    def prod_price(self):
        return float(self.__prod_price)

    @prod_price.setter
    def prod_price(self, value: float):
        if str(value).isnumeric():
            self.__prod_price = float(value)
        else:
            raise Exception("Price must be in float")

    def to_string(self):
        """ alias of __str__(), converts product data to string """
        return self.__str__()

    def __str__(self):
        """ Converts product data to string """
        return self.prod_name + "," + str(self.prod_price)


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):

        """ Write data to a file from a list of product rows
        :param file_name: (string) with name of file
        :param list_of_product_objects: (list) of product objects data saved to file
        :return: (bool) with status of success status
        """

        objFile = open(file_name, "w")
        for row in list_of_product_objects:
            objFile.write(str(row.prod_name) + "," + str(row.prod_price) + "\n")
        objFile.close()

    @staticmethod
    def read_data_from_file(file_name):

        try:
            objFile= open(file_name,"r")
            for line in objFile:
                product, price=line.split(",")
                lstOfProductObjects.append(Product(product.strip(),float(price.strip())))
            return lstOfProductObjects

        except:
            print("You do not have a file, please create one.")
            return lstOfProductObjects

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
    # TODO: Add docstring
    # TODO: Add code to show menu to user
    # TODO: Add code to get user's choice
    # TODO: Add code to show the current data from the file to user
    # TODO: Add code to get product data from user
class IO:

    """ A class for performing Input and Output
    methods: print_menu_items():

    print_current_list_items(list_of_rows):

    input_product_data():

    changelog: (When,Who,What) RRoot,1.1.2030,Created Class:
    """
    @staticmethod
    def menu_option():
        print('''
        Menu of Options
        1) View products
        2) Add a product
        3) Save File
        4) Exit
        ''')
        print()

    @staticmethod
    def input_menu_choice():
        choice = str(input("Choose an option:")).strip()
        return choice

    @staticmethod
    def print_current_list_items(list_of_products):
        print("Existing products and prices are:")
        for item in list_of_products:
            print(item)

    @staticmethod
    def input_new_product():
        newProduct=input("Product name: ")
        newPrice=float(input("Product price: "))
        return Product(newProduct,newPrice)

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #

lstOfProductObjects = FileProcessor.read_data_from_file(file_name)

while True:
    IO.menu_option()
    strChoice= IO.input_menu_choice()

    if strChoice.strip() == '1':
       IO.print_current_list_items(lstOfProductObjects)
       continue

    elif strChoice.strip() == '2':
        lstOfProductObjects.append(IO.input_new_product())
        continue

    elif strChoice.strip() == '3':
        FileProcessor.save_data_to_file(file_name, lstOfProductObjects)
        continue

    elif strChoice.strip() == '4':

        break

