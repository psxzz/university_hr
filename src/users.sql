USE university
GO

-- Role for hr employees
CREATE ROLE hr_employees
GRANT SELECT, INSERT, DELETE ON groups TO hr_employees
GRANT SELECT, INSERT, DELETE ON departments TO hr_employees
GRANT SELECT, INSERT, DELETE ON teachers TO hr_employees
GRANT SELECT, INSERT, DELETE ON students TO hr_employees
GO

-- Role for all teachers in department
CREATE ROLE all_teachers
GRANT SELECT ON teachers TO all_teachers
GO

-- Role for head of departments
CREATE ROLE department_heads
GRANT SELECT ON teachers TO department_heads
GRANT SELECT ON groups TO department_heads
GRANT SELECT ON students TO department_heads
GO


CREATE LOGIN hr_employee_1 WITH PASSWORD = 'Password_1234'
CREATE USER hr_1 FOR LOGIN hr_employee_1
GO

ALTER ROLE hr_employees ADD MEMBER hr_1

CREATE LOGIN teacher1 WITH PASSWORD = 'My_stupid_Password123'
CREATE USER best_teacher FOR LOGIN teacher1
GO

CREATE LOGIN teacher2 WITH PASSWORD = 'My_stupid_Password321'
CREATE USER worst_teacher FOR LOGIN teacher2
GO

ALTER ROLE all_teachers 
ADD MEMBER [best_teacher]
GO

ALTER ROLE all_teachers
ADD MEMBER [worst_teacher]
GO

ALTER ROLE department_heads
ADD MEMBER [worst_teacher]
GO

-- WITH CTE_Roles (role_principal_id)
-- AS
-- (
-- SELECT role_principal_id
-- FROM sys.database_role_members
-- WHERE member_principal_id = USER_ID()
-- UNION ALL
-- SELECT drm.role_principal_id
-- FROM sys.database_role_members drm
--   INNER JOIN CTE_Roles CR
--     ON drm.member_principal_id = CR.role_principal_id
-- )
-- SELECT USER_NAME(role_principal_id) RoleName
-- FROM CTE_Roles
-- UNION ALL
-- SELECT 'public'
-- ORDER BY RoleName;