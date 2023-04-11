class Book:

    # Attributes
    brand = ""
    title = ""
    price = 0

    # Constructor
    def __init__(self, brand, title, price):
        self.brand = brand
        self.title = title
        self.price = price

    # Methods
    def getDetails(self):
        print("Book Brand: ", self.brand)
        print("Book Title: ", self.title)
        print("Book Price: ", self.price)

    # Destructor
    def __del__(self):
        return None
