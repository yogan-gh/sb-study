count_employer = int(input("Кол-во сотрудников: "))
salary_list = []
for i_emp in range(1, count_employer + 1):
    print(f"Зарплата {i_emp} сотрудника: ", end='')
    salary = int(input())
    salary_list.append(salary)

while salary_list.count(0):
    salary_list.remove(0)
print(f'Максимальная ЗП: {max(salary_list)}')
print(f'Минимальная ЗП: {min(salary_list)}')
