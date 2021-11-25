CREATE DATABASE university
-- DROP DATABASE university
GO

USE university
--USE master
GO

CREATE TABLE institutes (
    id INT PRIMARY KEY IDENTITY(1, 1),
    full_name NVARCHAR(100),
    short_name NVARCHAR(10),
    head_id INT DEFAULT NULL --FOREIGN KEY REFERENCES teachers(id)
)
GO

CREATE TABLE teachers (
    id INT PRIMARY KEY IDENTITY(1, 1),
    first_name NVARCHAR(15),
    second_name NVARCHAR(15),
    last_name NVARCHAR(15),
    phone_number NVARCHAR(12),
    institute_id INT FOREIGN KEY REFERENCES institutes(id)
)
GO

ALTER TABLE institutes ADD FOREIGN KEY (head_id) REFERENCES teachers(id)
GO

CREATE TABLE departments (
    id INT PRIMARY KEY IDENTITY(1, 1),
    full_name NVARCHAR(100),
    short_name NVARCHAR(10),
    student_count INT DEFAULT 0,
    institute_id INT REFERENCES institutes(id)
)
GO

CREATE TABLE students (
    gradebook_number INT PRIMARY KEY IDENTITY(100000, 1),
    first_name NVARCHAR(15),
    second_name NVARCHAR(15),
    last_name NVARCHAR(15),
    phone_number NVARCHAR(12),
    birth_date DATE,
    department_id INT REFERENCES departments(id)
)
GO

CREATE TRIGGER students_IncreaseCountOfGroup
    ON students AFTER INSERT
AS BEGIN
    DECLARE @groupID INT
      
    SELECT @groupID = department_id FROM inserted

    UPDATE departments
    SET student_count = student_count + 1
    WHERE id = @groupID 
END
GO

CREATE TRIGGER students_DecreaseCountOfGroup
    ON students AFTER DELETE
AS BEGIN
    DECLARE @groupID INT
    SELECT @groupID = department_id from deleted

    UPDATE departments
    SET student_count = student_count - 1
    WHERE id = @groupID
END
GO

