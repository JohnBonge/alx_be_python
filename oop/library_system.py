class Book:
	def __init__(self, title, author):
		self.title = title
		self.author = author

	def get_details(self):
		print(f"Book: {selft.title} by {self.author}")

	def __str__(self):
		return self.get_details()

class EBook(Book):
	def __init__(self, title, author, file_size):
		self.file_size = file_size

	def get_details(self):
		print(f"EBook: {self.title} by {self.author}, filesize: {self.file_size}")

	def __str__(self):
		return self.get_details()

class PrintBook(Book):
	def __init__(self, title, author, page_count):
		self.page_count = page_count

	def get_details(self):
		print(f"PrintBook: {self.title} by {self.author}, page count: {self.page_count}")

	def __str__(self):
		return self.get_details()

class Library():
	def __init__(self):
		self.books = []

	def add_book(self, book):
		self.books.append(book)

	def list_books(self):
		for book in self.books:
			print(book.get_details())