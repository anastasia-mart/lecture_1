def main():
    students = []
    
    while True:
        print("\n--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Show report (all students)")
        print("4. Find top performer")
        print("5. Exit")
        
        try:
            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                add_student(students)
            elif choice == "2":
                add_grades(students)
            elif choice == "3":
                show_report(students)
            elif choice == "4":
                find_top_performer(students)
            elif choice == "5":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter 1-5.")
                
        except Exception as e:
            print(f"An error occurred: {e}")

def add_student(students):
    name = input("Enter student name: ").strip()
    
    if any(student["name"] == name for student in students):
        print("Student already exists.")
        return
    
    students.append({"name": name, "grades": []})
    print(f"Student {name} added successfully.")

def add_grades(students):
    name = input("Enter student name: ").strip()
    
    student = next((s for s in students if s["name"] == name), None)
    if not student:
        print("Student not found.")
        return
    
    print("Enter grades (0-100) or 'done' to finish:")
    while True:
        grade_input = input("Enter a grade: ").strip().lower()
        
        if grade_input == "done":
            break
        
        try:
            grade = float(grade_input)
            if 0 <= grade <= 100:
                student["grades"].append(grade)
                print(f"Grade {grade} added.")
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid grade. Please enter a number or 'done'.")

def show_report(students):
    if not students:
        print("No students available.")
        return
    
    print("\n--- Student Report ---")
    
    averages = []
    for student in students:
        try:
            avg = sum(student["grades"]) / len(student["grades"])
            print(f"{student['name']}'s average grade is {avg:.1f}.")
            averages.append(avg)
        except ZeroDivisionError:
            print(f"{student['name']}'s average grade is N/A.")
    
    if averages:
        print("---")
        print(f"Max Average: {max(averages):.1f}")
        print(f"Min Average: {min(averages):.1f}")
        print(f"Overall Average: {sum(averages)/len(averages):.1f}")

def find_top_performer(students):
    valid_students = [s for s in students if s["grades"]]
    
    if not valid_students:
        print("No students with grades available.")
        return
    
    top_student = max(valid_students, 
                     key=lambda s: sum(s["grades"])/len(s["grades"]))
    top_avg = sum(top_student["grades"]) / len(top_student["grades"])
    
    print(f"The student with the highest average is {top_student['name']} with a grade of {top_avg:.1f}.")

if __name__ == "__main__":
    main()
