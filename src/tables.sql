CREATE DATABASE university
-- DROP DATABASE university
GO

USE university
--USE master
GO

CREATE TABLE departments (
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
    department_id INT FOREIGN KEY REFERENCES departments(id)
)
GO

ALTER TABLE departments ADD FOREIGN KEY (head_id) REFERENCES teachers(id)
GO

CREATE TABLE groups (
    id INT PRIMARY KEY IDENTITY(1, 1),
    full_name NVARCHAR(100),
    short_name NVARCHAR(10),
    student_count INT DEFAULT 0,
    department_id INT REFERENCES departments(id)
)
GO

CREATE TABLE students (
    gradebook_number INT PRIMARY KEY IDENTITY(100000, 1),
    first_name NVARCHAR(15),
    second_name NVARCHAR(15),
    last_name NVARCHAR(15),
    phone_number NVARCHAR(12),
    birth_date DATE,
    group_id INT REFERENCES groups(id)
)
GO

CREATE TRIGGER students_IncreaseCountOfGroup
    ON students AFTER INSERT
AS BEGIN
    DECLARE @groupID INT
      
    SELECT @groupID = group_id FROM inserted

    UPDATE groups
    SET student_count = student_count + 1
    WHERE id = @groupID 
END
GO

CREATE TRIGGER students_DecreaseCountOfGroup
    ON students AFTER DELETE
AS BEGIN
    DECLARE @groupID INT
    SELECT @groupID = group_id from deleted

    UPDATE groups
    SET student_count = student_count - 1
    WHERE id = @groupID
END
GO
