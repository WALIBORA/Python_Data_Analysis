class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def describe(self):
        return f"'{self.title}' by {self.author},is Ksh. {self.price} "

    def read(self):
        return f"You start reading '{self.title}'."

# Child Class (Inheritance)
class Biology(Book):
    def __init__(self, title, author, price, edition):
        # Call parent constructor
        super().__init__(title, author, price)
        self.edition = edition

    # Method overriding (Polymorphism)
    def read(self):
        return f"Thank you for purchasing '{self.title}' and it is: {self.edition}. edition"

# Another Child Class
class OnlineBook(Book):
    def __init__(self, title, author, price, duration):
        super().__init__(title, author, price)
        self.duration = duration

    # Method overriding (Polymorphism)
    def read(self):
        return f"You are about to read '{self.title}' which will take a total readtime of {self.duration} hours."

# --- Usage ---
book1 = Book("The River And The Source", "Magret Ogola", 1000)
biology = Biology("Made Familiar", "Gideon Wafula", 700, 5)
online = OnlineBook("c++", "Benjamin Kalume", 400, 2)

# Show polymorphism in action
books = [book1, biology, online]

for b in books:
    print(b.describe())
    print(b.read())
    print()
