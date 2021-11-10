CREATE DATABASE hr_university
USE hr_university
GO

CREATE TABLE departments (
    id INT PRIMARY KEY IDENTITY,
    full_name NVARCHAR(100),
    short_name NVARCHAR(10),
    head_id INT NOT NULL --FOREIGN KEY REFERENCES teachers(id)
)
GO

CREATE TABLE teachers (
    id INT PRIMARY KEY IDENTITY,
    first_name NVARCHAR(15),
    second_name NVARCHAR(15),
    last_name NVARCHAR(15),
    phone_number NVARCHAR(12),
    department_id INT FOREIGN KEY REFERENCES departments(id)
)
GO

ALTER TABLE departments ADD FOREIGN KEY (head_id) REFERENCES teachers(id)
GO

CREATE TABLE groups (
    id INT PRIMARY KEY IDENTITY,
    full_name NVARCHAR(100),
    short_name NVARCHAR(10),
    student_count INT DEFAULT 0,
    department_id INT REFERENCES departments(id)
)
GO

CREATE TABLE students (
    gradebook_number INT PRIMARY KEY IDENTITY,
    first_name NVARCHAR(15),
    second_name NVARCHAR(15),
    last_name NVARCHAR(15),
    phone_number NVARCHAR(12),
    birth_date DATE,
    group_id INT REFERENCES groups(id)
)
GO
