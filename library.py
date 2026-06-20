class Library:

    def __init__(self):
        self.books = []
        self.students = []

    def add_book(self, book):
        self.books.append(book)

    def view_books(self):
        if not self.books:
            print("No books found!")
            return

        for book in self.books:
            book.show_info()

    def search_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def delete_book(self, book_id):
        book = self.search_book(book_id)

        if book:
            self.books.remove(book)
            print("Delete successful!")
        else:
            print("Book not found!")


    def add_student(self, student):
        self.students.append(student)

    def view_students(self):
        if not self.students:
            print("No students found!")
            return

        for student in self.students:
            student.show_info()

    def search_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def delete_student(self, student_id):
        student = self.search_student(student_id)

        if student:
            self.students.remove(student)
            print("Delete successful!")
        else:
            print("Student not found!")


    def borrow_book(self, student_id, book_id):

        student = self.search_student(student_id)

        if not student:
            print("Student not found!")
            return

        book = self.search_book(book_id)

        if not book:
            print("Book not found!")
            return

        try:
            book.borrow_book()
            print("Borrow successful!")
        except ValueError as e:
            print(e)


    def return_book(self, book_id):

        book = self.search_book(book_id)

        if not book:
            print("Book not found!")
            return

        book.return_book()
        print("Return successful!")