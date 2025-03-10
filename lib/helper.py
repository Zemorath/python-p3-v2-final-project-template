from models.books import Book
from models.owners import Owner


def exit_program():
    print("See ya!")
    exit()

# Book model helper methods

def list_books():
    books = Book.get_all()
    for book in books:
        print(f"Title: {book.title} || Author: {book.author} || ISBN: {book.isbn}")

def create_book(_id):
    title = input("Enter the book's title: ")
    author = input("Enter the book's author: ")
    isbn = input("Enter the book's ISBN: ")
    try:
        book = Book.create(title, author, int(isbn), int(_id))
        print(f'Succes: {book.title} || Author: {book.author} || ISBN: {book.isbn}')
    except Exception as exc:
        print("Error creating book: ", exc)

def update_book(book_id):
    if book := Book.find_by_id(book_id):
        try:
            title = input("Enter the new title: ")
            book.title = title

            author = input("Enter the new author: ")
            book.author = author

            isbn = input("Enter the new ISBN: ")
            book.isbn = int(isbn)

            book.update()
            print(f'Success: {book.title} || Author: {book.author} || ISBN: {book.isbn}')
        except Exception as exc:
            print("Error updating book: ", exc)
    else:
        print(f'Book {title} not found')

def delete_book(_id, title):
    if book := Book.find_by_id(_id):
        book.delete()
        print(f'Book {title} deleted')
    else:
        print(f'Book {title} not found')


# Owner model helper methods
    
def list_owners():
    owners = Owner.get_all()
    return owners

def list_owners_by_age():
    age = input("Enter the age to filter by: ")
    owners = Owner.get_all_by_age(age)
    return owners

def list_owners_by_fav_genre():
    fav_genre = input("Enter the genre to filter by: ")
    owners = Owner.get_all_by_fav_genre(fav_genre)
    return owners

def create_owner():
    name = input("Enter the owner's name: ")
    age = input("Enter the owner's age: ")
    fav_genre = input("Enter the owner's favorite genre: ")
    try:
        owner = Owner.create(name, int(age), fav_genre)
        print(f"Success: Name: {owner.name} || Age: {owner.age} || Favorite Genre: {owner.fav_genre}")
    except Exception as exc:
        print("Error create Owner: ", exc)

def update_owner(_id):
    if owner := Owner.find_by_id(_id):
        try:
            name = input("Enter the new name: ")
            owner.name = name

            age = input("Enter the owner's age: ")
            owner.age = int(age)

            fav_genre = input("Enter the owner's favorite genre: ")
            owner.fav_genre = fav_genre

            owner.update()
            print(f'Success: {owner.name} || Age: {owner.age} || Favorite Genre: {owner.fav_genre}')
        except Exception as exc:
            print("Error updating owner: ", exc)
    else:
        print(f"Owner {name} not found")

def delete_owner(_id):
    if owner := Owner.find_by_id(_id):
        books = Book.find_by_owner_id(owner.id)
        for book in books:
            book.delete()
        owner.delete()
        print(f'Owner {owner.name} has been deleted')
    else:
        print(f'Owner {owner.name} not found')

def list_owners_books(_id):
    if owner := Owner.find_by_id(_id):
        for i, book in enumerate(owner.books(), start=1):
            print(f"{i}. Title: {book.title} || Author: {book.author}")
    return owner.books()

def grab_owners_books(_id):
    if owner := Owner.find_by_id(_id):
        return owner.books()