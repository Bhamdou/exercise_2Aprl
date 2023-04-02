import pandas as pd

def read_employee_data(file_path):
    return pd.read_csv(file_path)

def filter_and_sort_employees(data, salary_threshold):
    filtered_data = data[data['Salary'] > salary_threshold]
    sorted_data = filtered_data.sort_values(by='Salary', ascending=False)
    return sorted_data

def main():
    employee_data = read_employee_data('employees.csv')
    salary_threshold = int(input("Enter salary threshold: "))
    filtered_and_sorted_data = filter_and_sort_employees(employee_data, salary_threshold)
    print("\nEmployees with salary above the threshold:")
    print(filtered_and_sorted_data)

if __name__ == "__main__":
    main()
