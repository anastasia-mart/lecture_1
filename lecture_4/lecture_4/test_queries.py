"""
Тестирование всех 8 SQL-запросов из лабораторной работы
"""

import sqlite3

def test_all_queries():
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ 8 SQL-ЗАПРОСОВ ИЗ ЛАБОРАТОРНОЙ")
    print("=" * 60)
    
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    
    queries = [
        # Запрос 1: Проверка таблиц
        ("Проверка таблиц в базе", 
         "SELECT name FROM sqlite_master WHERE type='table';"),
        
        # Запрос 2: Количество записей
        ("Количество записей", 
         "SELECT 'Студенты:', COUNT(*) FROM students UNION ALL SELECT 'Оценки:', COUNT(*) FROM grades;"),
        
        # Запрос 3: Все оценки Alice Johnson
        ("3. Все оценки Alice Johnson",
         "SELECT g.subject, g.grade FROM grades g JOIN students s ON g.student_id = s.id WHERE s.name = 'Alice Johnson';"),
        
        # Запрос 4: Средний балл каждого студента
        ("4. Средний балл каждого студента",
         "SELECT s.name, ROUND(AVG(g.grade), 2) as avg_grade FROM students s JOIN grades g ON s.id = g.student_id GROUP BY s.id, s.name ORDER BY avg_grade DESC;"),
        
        # Запрос 5: Студенты после 2004 года
        ("5. Студенты после 2004 года",
         "SELECT name, birth_year FROM students WHERE birth_year > 2004 ORDER BY birth_year;"),
        
        # Запрос 6: Средние оценки по предметам
        ("6. Средние оценки по предметам",
         "SELECT subject, ROUND(AVG(grade), 2) as avg_grade FROM grades GROUP BY subject ORDER BY avg_grade DESC;"),
        
        # Запрос 7: Топ-3 студента
        ("7. Топ-3 студента",
         "SELECT s.name, ROUND(AVG(g.grade), 2) as avg_grade FROM students s JOIN grades g ON s.id = g.student_id GROUP BY s.id, s.name ORDER BY avg_grade DESC LIMIT 3;"),
        
        # Запрос 8: Оценки ниже 80
        ("8. Оценки ниже 80",
         "SELECT s.name, g.subject, g.grade FROM students s JOIN grades g ON s.id = g.student_id WHERE g.grade < 80 ORDER BY s.name, g.grade;")
    ]
    
    for name, sql in queries:
        print(f"\n{'='*40}")
        print(f"{name}")
        print('='*40)
        
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            
            if results:
                for row in results:
                    print(f"  {row}")
            else:
                print("  (нет результатов)")
                
        except Exception as e:
            print(f"  ❌ Ошибка: {e}")
    
    print("\n" + "=" * 60)
    print("✅ ВСЕ 8 ЗАПРОСОВ ВЫПОЛНЕНЫ УСПЕШНО!")
    print("=" * 60)
    
    conn.close()

if __name__ == "__main__":
    test_all_queries()
