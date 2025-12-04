-- ============================================
-- ЛАБОРАТОРНАЯ РАБОТА №4: БАЗА ДАННЫХ ШКОЛЫ
-- ============================================

-- 1. СОЗДАНИЕ ТАБЛИЦ
DROP TABLE IF EXISTS grades;
DROP TABLE IF EXISTS students;

CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    birth_year INTEGER NOT NULL
);

CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    grade INTEGER NOT NULL CHECK (grade >= 1 AND grade <= 100),
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
);

-- 2. ВСТАВКА ДАННЫХ
INSERT INTO students (name, birth_year) VALUES 
('Alice Johnson', 2005),
('Brian Smith', 2004),
('Carla Reyes', 2006),
('Daniel Kim', 2005),
('Eva Thompson', 2003),
('Felix Nguyen', 2007),
('Grace Patel', 2005),
('Henry Lopez', 2004),
('Isabella Martinez', 2006);

INSERT INTO grades (student_id, subject, grade) VALUES 
(1, 'Math', 88),
(1, 'English', 92),
(1, 'Science', 85),
(2, 'Math', 75),
(2, 'History', 83),
(2, 'English', 79),
(3, 'Science', 95),
(3, 'Math', 91),
(3, 'Art', 89),
(4, 'Math', 84),
(4, 'Science', 88),
(4, 'Physical Education', 93),
(5, 'English', 90),
(5, 'History', 85),
(5, 'Math', 88),
(6, 'Science', 72),
(6, 'Math', 78),
(6, 'English', 81),
(7, 'Art', 94),
(7, 'Science', 87),
(7, 'Math', 90),
(8, 'History', 77),
(8, 'Math', 83),
(8, 'Science', 80),
(9, 'English', 96),
(9, 'Math', 89),
(9, 'Art', 92);

-- 3. ИНДЕКСЫ
CREATE INDEX idx_students_birth_year ON students(birth_year);
CREATE INDEX idx_grades_student_id ON grades(student_id);
CREATE INDEX idx_grades_subject ON grades(subject);
CREATE INDEX idx_grades_grade ON grades(grade);

-- 4. ЗАПРОСЫ ИЗ ЗАДАНИЯ
-- Запрос 3: Все оценки Alice Johnson
SELECT g.subject, g.grade
FROM grades g
JOIN students s ON g.student_id = s.id
WHERE s.name = 'Alice Johnson';

-- Запрос 4: Средний балл каждого студента
SELECT 
    s.id,
    s.name,
    ROUND(AVG(g.grade), 2) as average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.name
ORDER BY average_grade DESC;

-- Запрос 5: Студенты, родившиеся после 2004 года
SELECT id, name, birth_year
FROM students
WHERE birth_year > 2004
ORDER BY birth_year;

-- Запрос 6: Средняя оценка по каждому предмету
SELECT 
    subject,
    ROUND(AVG(grade), 2) as average_grade,
    COUNT(*) as grades_count
FROM grades
GROUP BY subject
ORDER BY average_grade DESC;

-- Запрос 7: Топ-3 студента по среднему баллу
SELECT 
    s.name,
    ROUND(AVG(g.grade), 2) as average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.name
ORDER BY average_grade DESC
LIMIT 3;

-- Запрос 8: Студенты с оценкой ниже 80
SELECT DISTINCT
    s.id,
    s.name,
    g.subject,
    g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.grade < 80
ORDER BY s.name, g.grade;
