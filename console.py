import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()


author1 = Author("author1")
author_repository.save(author1)
author2 = Author("author2")
author_repository.save(author2)

book1 = Book("title1", "genre1", "publisher1", author1, "year1")
book_repository.save(book1)
book2 = Book("title2", "genre2", "publisher2", author1, "year2")
book_repository.save(book2)
book3 = Book("title3", "genre3", "publisher3", author1, "year3")
book_repository.save(book3)



for book in book_repository.select_all():
    print(book.title, book.author.name, book.publisher, book.genre)


book_repository.delete(book1.id)
# author_repository.delete(author2.id)

for book in book_repository.select_all():
    print(book.title, book.author.name, book.publisher, book.genre)
print (author1.name, book1.title)

for author in author_repository.select_all():
    print(author.name)