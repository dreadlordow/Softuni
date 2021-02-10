class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author, book_name, days_to_return , library):
        if book_name in library.books_available[author]:
            library.books_available[author].remove(book_name)
            if self.username in library.rented_books.keys():
                library.rented_books[self.username].update({book_name: days_to_return})
            else:
                library.rented_books[self.username] = {book_name: days_to_return}
            self.books.append(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"

        else:
            for k, v in library.rented_books.items():
                if book_name in library.rented_books[k].keys():
                    return f'The book "{book_name}" is already rented and will be available ' \
                           f'in {library.rented_books[k][book_name]} days!'

    def return_book(self, author, book_name, library):
        if book_name not in self.books:
            return f'{self.username} doesn\'t have this book in his/her records!'
        self.books.remove(book_name)
        library.books_available[author].append(book_name)
        del library.rented_books[self.username][book_name]

    def info(self):
        res = ', '.join(sorted([book for book in self.books]))
        return res

    def __str__(self):
        return f'{self.user_id}, {self.username}, {self.books}'