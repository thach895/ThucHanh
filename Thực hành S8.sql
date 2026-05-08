create database Company_db;
use Company_db;

create table Department(
	dept_id int primary key auto_increment,
    dept_name varchar(100) not null,
    location varchar(100)
);

create table Employee(
	emp_id int primary key auto_increment,
    emp_name varchar(100) not null,
    gender int default 1,
    birth_date date,
    salary decimal(10,2),
    dept_id int,
    foreign key(dept_id) references Department(dept_id) on update cascade
);

create table Project(
	project_id int primary key auto_increment,
    project_name varchar(100) not null,
    emp_id int,
    start_date date default(current_date()),
    end_date date
);

alter table Employee
add email varchar(100) unique;

alter table Project
modify project_name varchar(200),
 add constraint chk_project_date
check (end_date >= start_date);

insert into Department (dept_name,location)
values
('IT', 'Ha Noi'),
('HR','HCM'),
('Marketing','Da Nang');

insert into Employee (emp_name,gender,birth_date,salary,email)
values
('Nguyen Van A',1,'1990-01-15',1500,'a@gmail.com'),
('Tran Thi B',0,'1995-05-20',1200,'b@gmail.com'),
('Le Minh C',1,'1988-10-10',2000,'c@gmail.com'),
('Pham Thi D',0,'1992-12-05',1800,'d2gmail.com');





