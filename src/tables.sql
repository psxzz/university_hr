CREATE TABLE departments (
    id INT PRIMARY KEY IDENTITY,
    full_name VARCHAR(100),
    short_name VARCHAR(10),
    head_id INT REFERENCES teachers(id)
)
GO

CREATE TABLE teachers (
    id INT PRIMARY KEY IDENTITY,
    first_name VARCHAR(15),
    second_name VARCHAR(15),
    last_name VARCHAR(15),
    department_id INT REFERENCES departments(id)
)
GO

CREATE TABLE groups (
    id INT PRIMARY KEY IDENTITY,
    full_name VARCHAR(100),
    short_name VARCHAR(10),
    department_id INT REFERENCES departments(id)
)
GO

CREATE TABLE students (
    id INT PRIMARY KEY IDENTITY,
    first_name VARCHAR(15),
    second_name VARCHAR(15),
    last_name VARCHAR(15),
    group_id INT REFERENCES groups(id)
)
GO
