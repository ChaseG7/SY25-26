from datetime import datetime, date  
tasks = []  
with open('tasks.txt', 'r') as f:  
    lines = f.readlines()  

for line in lines:  
    task, due_date = line.strip().split(",")  
    tasks.append((task, due_date))  

report_lines = []

for task, due_date in tasks:  
    completed = input(f"Did you complete '{task}' by {due_date}? (yes/no): ").strip().lower()  
    due_date_obj = datetime.strptime(due_date, '%Y-%m-%d').date()
    
    if completed == 'yes':
        completion_str = input(f"When did you complete '{task}'? (YYYY-MM-DD): ").strip()
        completion_date = datetime.strptime(completion_str, '%Y-%m-%d').date()
        days_late = (completion_date - due_date_obj).days
        if days_late > 0:
            report_lines.append(f"Task '{task}' was completed {days_late} day(s) late.")
        else:
            report_lines.append(f"Task '{task}' was completed on time.")
    else:
        report_lines.append(f"Task '{task}' was not completed.")

with open('task_report.txt', 'w') as report_file:
    for line in report_lines:
        report_file.write(line + "\n")

print(tasks)
print("Report saved to 'task_report.txt'.")