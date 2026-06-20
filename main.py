from library import Library
from book import Book
from student import Student


library = Library()

while True:

    print("\n========== LIBRARY MANAGEMENT ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Add Student")
    print("6. View Students")
    print("7. Search Student")
    print("8. Delete Student")
    print("9. Borrow Book")
    print("10. Return Book")
    print("0. Exit")

    choice = input("Choose: ")

    try:

        # Add Book
        if choice == "1":

            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")

            quantity = int(input("Quantity: "))

            if quantity < 0:
                raise ValueError(
                    "Quantity cannot be negative!"
                )

            book = Book(
                book_id,
                title,
                author,
                quantity
            )

            library.add_book(book)

            print("Book added successfully!")

        # View Books
        elif choice == "2":
            library.view_books()

        # Search Book
        elif choice == "3":

            book_id = input("Enter Book ID: ")

            book = library.search_book(book_id)

            if book:
                print("Book found:")
                book.show_info()
            else:
                print("Book not found!")

        # Delete Book
        elif choice == "4":

            book_id = input("Enter Book ID: ")
            library.delete_book(book_id)

        # Add Student
        elif choice == "5":

            student_id = input("Student ID: ")
            name = input("Name: ")
            class_name = input("Class: ")

            student = Student(
                student_id,
                name,
                class_name
            )

            library.add_student(student)

            print("Student added successfully!")

        # View Students
        elif choice == "6":
            library.view_students()

        # Search Student
        elif choice == "7":

            student_id = input(
                "Enter Student ID: "
            )

            student = library.search_student(
                student_id
            )

            if student:
                print("Student found:")
                student.show_info()
            else:
                print("Student not found!")

        # Delete Student
        elif choice == "8":

            student_id = input(
                "Enter Student ID: "
            )

            library.delete_student(
                student_id
            )

        # Borrow Book
        elif choice == "9":

            student_id = input(
                "Student ID: "
            )

            book_id = input(
                "Book ID: "
            )

            library.borrow_book(
                student_id,
                book_id
            )

        # Return Book
        elif choice == "10":

            book_id = input(
                "Book ID: "
            )

            library.return_book(
                book_id
            )

        # Exit
        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")

    except ValueError as e:
        print("Error:", e)

    except Exception as e:
        print("Unexpected error:", e)