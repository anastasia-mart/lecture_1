"""
Скрипт для создания базы данных school.db из SQL-файла
"""

import sqlite3
import os

def main():
    print("=" * 50)
    print("СОЗДАНИЕ БАЗЫ ДАННЫХ ШКОЛЫ")
    print("=" * 50)
    
    # Удаляем старую базу, если существует
    if os.path.exists('school.db'):
        os.remove('school.db')
        print("🗑️  Старый school.db удален")
    
    # Создаем подключение к базе данных
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    print("✅ База данных school.db создана")
    
    try:
        # Читаем SQL-скрипт
        with open('school_queries.sql', 'r', encoding='utf-8') as f:
            sql_script = f.read()
        
        print("📖 Выполняю SQL-скрипт...")
        
        # Выполняем весь SQL-скрипт
        cursor.executescript(sql_script)
        
        # Сохраняем изменения
        conn.commit()
        print("💾 Все изменения сохранены")
        
        # Проверяем, что данные добавлены
        cursor.execute("SELECT COUNT(*) FROM students")
        students_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM grades")
        grades_count = cursor.fetchone()[0]
        
        print(f"📊 Студентов в базе: {students_count}")
        print(f"📊 Оценок в базе: {grades_count}")
        
        print("\n" + "=" * 50)
        print("🎉 БАЗА ДАННЫХ УСПЕШНО СОЗДАНА!")
        print("=" * 50)
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        print("Проверьте файл school_queries.sql")
    
    finally:
        conn.close()

if __name__ == "__main__":
    main()
