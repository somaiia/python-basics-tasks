#Q2
salaries = {
    101: 50000,
    102: 60000,
    103: 55000
}
increments = [
    (101, 10),  
    (104, 5),   
    (102, 15)
]
for item in increments:
    emp_id = item[0]
    increment_percentage = item[1]
    if emp_id in salaries:
        new_salary = salaries[emp_id] + (salaries[emp_id] * increment_percentage / 100)
        salaries[emp_id] = new_salary

print("Updated salaries:", salaries)