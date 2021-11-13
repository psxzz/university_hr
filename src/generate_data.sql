USE university
GO

INSERT INTO departments(full_name, short_name) VALUES
    ('Юридический институт', 'ЮИ'),
    ('Институт машиностроения', 'ИМиАТ'),
    ('Институт информационных технологий', 'ИиТР') --,
    -- ('Институт Архитектуры', 'ИА'),
    -- ('Институт прикладной математики', 'ИПФМИ'),
    -- ('Институт Биологии и Экологии', 'ИБиЭ'),
    -- ('Педагогический институт', 'ПИ')
GO

--SELECT * from departments

INSERT INTO groups(full_name, short_name, department_id, student_count) VALUES
    ('Теория и история государства и права', 'ТИГП', 1, 3),
    ('Уголовно-правовые дисциплины', 'УПД', 1, 3),
    ('Гражданское право', 'ГП', 1, 3),
    ('Технология машиностроения', 'ТМ', 2, 3),
    ('Автомобильный транспорт', 'АТ', 2, 3),
    ('Управление качеством', 'УК', 2, 3),
    ('Вычислительная техника', 'ВТ', 3, 3),
    ('Прикладная информатика', 'ПИПб', 3, 3),
    ('Информатика и защита информации', 'ИБ', 3, 3)
GO

-- SELECT * from groups

INSERT INTO teachers(second_name, first_name, last_name, phone_number, department_id) VALUES
    ('Иванов', 'Иван', 'Иванович', '+78005553535', 1),
    ('Сидоров', 'Артем', 'Тарасович', '+79009009090', 1),
    ('Пушкин', 'Александр', 'Сергеевич', '+79051231231', 2),
    ('Тарасов', 'Корней', 'Витальевич', '+78889998765', 2),
    ('Воронин', 'Константин', 'Евгеньевич', '+79652321488', 3),
    ('Степанова', 'Марина', 'Сергеевна', '+79458458989', 3)
GO

-- SELECT * from teachers

INSERT INTO students(second_name, first_name, last_name, phone_number, birth_date, group_id) VALUES 
    ('Украинин', 'Вячеслав', 'Валерьевич', '+79001112233', '25-09-2000', 1),
    ('Семенов', 'Андрей', 'Юрьевич', '+79123770990', '15-03-2001', 1),
    ('Покрышкин', 'Игорь', 'Ильич', '+79881345643', '03-12-1999', 1),
    ('Кавинов', 'Денис', 'Витальевич', '+79011415432', '30-07-2000', 2),
    ('Горбачев', 'Михаил', 'Сергеевич', '+79169991212', '12-06-2001', 2),
    ('Петров', 'Денис', 'Альбертович', '+79008831543', '09-09-2000', 2),
    ('Чертилов', 'Антон', 'Романович', '+79042345437', '19-11-2000', 3),
    ('Ослова', 'Евгения', 'Михайловна', '+79313312415', '01-02-2001', 3),
    ('Вернов', 'Давид', 'Кириллович', '+79073948812', '17-05-1999', 3),
    ('Пугачева', 'Алла', 'Борисовна', '+79999999999', '25-03-1992', 4),
    ('Галкин', 'Максим', 'Александрович', '+79807771212', '11-11-2004', 4),
    ('Ивлев', 'Павел', 'Игоревич', '+79032281337', '13-01-2000', 4),
    ('Вавилов', 'Илья', 'Родионович', '+79026458393', '07-07-2007', 5),
    ('Кравченко', 'Мария', 'Игоревна', '+79900567891', '12-04-1999', 5),
    ('Макаров', 'Кирилл', 'Петрович', '+79418992354', '27-05-2001', 5),
    ('Приколов', 'Василий', 'Андреевич', '+79150738912', '10-01-2000', 6),
    ('Ломоносова', 'Оксана', 'Владимировна', '+79075608855', '18-06-1998', 6),
    ('Максимова', 'Ирина', 'Сергеевна', '+79213548213', '18-06-1999', 6),
    ('Ширяев', 'Максим', 'Дмитриевич', '+79213548216', '18-06-2000', 7),
    ('Дубровский', 'Григорий', 'Александрович', '+79213548217', '10-06-1998', 7),
    ('Лишайкин', 'Руслан', 'Артемович', '+79213548215', '17-09-1999', 7),
    ('Рыбин', 'Макар', 'Владимирович', '+79213548219', '30-10-2000', 8),
    ('Киркоров', 'Филипп', 'Михайлович', '+79213548218', '09-06-2001', 8),
    ('Валуев', 'Семен', 'Ярославович', '+79213548220', '28-11-1999', 8),
    ('Лебедев', 'Александр', 'Романович', '+79213548222', '15-12-2000', 9),
    ('Коровин', 'Сергей', 'Данилович', '+79213548221', '08-08-1998', 9),
    ('Пчелкина', 'Лилия', 'Антоновна', '+79213548225', '18-04-1997', 9)
GO

SELECT * from students
    