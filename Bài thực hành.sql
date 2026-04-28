CREATE DATABASE OnlineLearning;
USE OnlineLearning;

CREATE TABLE Student (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    fullname VARCHAR(255) NOT NULL,
    birthday DATE,
    email VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE Instructor (
    instructor_id INT PRIMARY KEY AUTO_INCREMENT,
    fullname VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE Course (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(255) NOT NULL,
    description TEXT,
    total_sessions INT,
    instructor_id INT,
    FOREIGN KEY (instructor_id) REFERENCES Instructor(instructor_id)
);

CREATE TABLE Enrollment (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    enroll_date DATE,
    UNIQUE(student_id, course_id), -- không đăng ký trùng
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

CREATE TABLE Result (
    result_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    mid_score DECIMAL(4,2),
    final_score DECIMAL(4,2),
    UNIQUE(student_id, course_id), -- mỗi SV 1 kết quả / khóa
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id),
    CHECK (mid_score BETWEEN 0 AND 10),
    CHECK (final_score BETWEEN 0 AND 10)
);

INSERT INTO Student (fullname, birthday, email) VALUES
('Nguyen Van A', '2000-01-01', 'a@gmail.com'),
('Tran Thi B', '2001-02-02', 'b@gmail.com'),
('Le Van C', '2002-03-03', 'c@gmail.com'),
('Pham Thi D', '2000-04-04', 'd@gmail.com'),
('Hoang Van E', '1999-05-05', 'e@gmail.com');

INSERT INTO Instructor (fullname, email) VALUES
('Teacher 1', 't1@gmail.com'),
('Teacher 2', 't2@gmail.com'),
('Teacher 3', 't3@gmail.com'),
('Teacher 4', 't4@gmail.com'),
('Teacher 5', 't5@gmail.com');

INSERT INTO Course (course_name, description, total_sessions, instructor_id) VALUES
('SQL Basic', 'Learn SQL', 10, 1),
('Java Core', 'Java fundamentals', 12, 2),
('Web Dev', 'HTML CSS JS', 15, 3),
('Python', 'Python basics', 8, 4),
('Data Analysis', 'Analyze data', 10, 5);

INSERT INTO Enrollment (student_id, course_id, enroll_date) VALUES
(1,1,'2025-01-01'),
(1,2,'2025-01-02'),
(2,1,'2025-01-03'),
(3,3,'2025-01-04'),
(4,4,'2025-01-05');

INSERT INTO Result (student_id, course_id, mid_score, final_score) VALUES
(1,1,8,9),
(1,2,7,8),
(2,1,6,7),
(3,3,9,9.5),
(4,4,5,6);

UPDATE Student
SET email = 'newemail@gmail.com'
WHERE student_id = 1;

UPDATE Course
SET description = 'Advanced SQL course'
WHERE course_id = 1;

UPDATE Result
SET final_score = 10
WHERE student_id = 1 AND course_id = 1;

DELETE FROM Enrollment
WHERE enrollment_id = 5;

DELETE FROM Result
WHERE student_id = 4 AND course_id = 4;
SELECT * FROM Student;
SELECT * FROM Instructor;
SELECT * FROM Course;
SELECT * FROM Enrollment;
SELECT * FROM Result;