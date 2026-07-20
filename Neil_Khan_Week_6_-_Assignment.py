# Student Name - Neil Khan
# Date - 17 July 2026
# Program Description - Library Book Management System (Week 6 Assignment)
# Tier Level - Base Level


# Book class representing a library book
class Book:

    # Initialize new Book object
    def __init__(self, title, author, isbn, year, genre):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.genre = genre
        self.available = True
        self.borrower = None

    # Return formatted string describing the book
    def __str__(self):
        return (f"{self.isbn:<18} "
                f"{self.title:<25} "
                f"{self.author:<22} "
                f"{self.year:<6} "
                f"{self.genre:<18} "
                f"{self.get_status()}")

    # Check out the book to a patron if it is available
    def check_out(self, patron_name):
        if self.available:
            self.available = False
            self.borrower = patron_name
            return True
        return False

    # Return the book to the library
    def return_book(self):
        self.available = True
        self.borrower = None
        return f"'{self.title}' has been returned and is now available."

    # Return current availability status of the book
    def get_status(self):
        if self.available:
            return "Available"
        return f"Checked out to {self.borrower}"


# ---------------- Main Program ----------------

# Create library collection
collection = [
    Book("The 48 Laws of Power", "Robert Greene", "978-0140280197", 2000, "Self-Improvement"),
    Book("Steve Jobs", "Walter Isaacson", "978-1451648539", 2011, "Biography"),
    Book("The Sign of the Four", "Arthur Conan Doyle", "978-0441013593", 1890, "Classic Fiction"),
    Book("Mere Christianity", "C.S. Lewis", "978-0060652920", 1952, "Theology"),
    Book("Everyday Woodworking", "Rex Krueger", "978-1510760165", 2021, "Woodworking"),
    Book("A Game of Thrones", "George R.R. Martin", "978-0553386790", 1996, "Fantasy")
]

# Display all books
print("=" * 23)
print("=== Full Collection ===")
print("=" * 23)
print()

print(f"{'ISBN':<18} {'Title':<25} {'Author':<22} {'Year':<6} {'Genre':<18} Status")
print("-" * 115)

for book in collection:
    print(book)
print()

# Activity log
print()
print("=" * 20)
print("=== Activity Log ===")
print("=" * 20)

# Check out the first two books
print()

if collection[0].check_out("Neil"):
    print(f"'{collection[0].title}' checked out to Neil.")
else:
    print(f"'{collection[0].title}' is already checked out.")

if collection[1].check_out("Ray"):
    print(f"'{collection[1].title}' checked out to Ray.")
else:
    print(f"'{collection[1].title}' is already checked out.")

# Attempt to check out the first book again
if collection[0].check_out("Alicia"):
    print(f"'{collection[0].title}' checked out to Alicia.")
else:
    print(f"'{collection[0].title}' is already checked out.")

# Return the second checked-out book
print()
print(collection[1].return_book())
print()

# Display books sorted by title
print()
print("=" * 34)
print("=== Collection Sorted by Title ===")
print("=" * 34)
print()

print(f"{'ISBN':<18} {'Title':<25} {'Author':<22} {'Year':<6} {'Genre':<18} Status")
print("-" * 115)

sorted_books = sorted(collection, key=lambda b: b.title)

for book in sorted_books:
    print(book)
print()

# Display only available books
print()
print("=" * 23)
print("=== Available Books ===")
print("=" * 23)
print()

print(f"{'ISBN':<18} {'Title':<25} {'Author':<22} {'Year':<6} {'Genre':<18} Status")
print("-" * 115)

available_books = [book for book in collection if book.available]

for book in available_books:
    print(book)