import pandas as pd
import numpy as np
import string
import random
import pyarrow as pa
import pyarrow.parquet as pq

# Generate random names
def generate_name():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(6))

# Generate random email addresses
def generate_email():
    domain = ['gmail.com', 'yahoo.com', 'hotmail.com']
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for _ in range(6))
    return f'{name}@{random.choice(domain)}'

# Generate a large dataset for the Students table
def generate_students_data(num_records):
    student_ids = np.arange(1, num_records+1)
    first_names = [generate_name() for _ in range(num_records)]
    last_names = [generate_name() for _ in range(num_records)]
    dates_of_birth = pd.date_range(start='1980-01-01', periods=num_records)
    genders = np.random.choice(['Male', 'Female'], size=num_records)
    emails = [generate_email() for _ in range(num_records)]
    phone_numbers = np.random.randint(1000000000, 9999999999, size=num_records, dtype=np.int64)

    df = pd.DataFrame({
        'student_id': student_ids,
        'first_name': first_names,
        'last_name': last_names,
        'date_of_birth': dates_of_birth,
        'gender': genders,
        'email': emails,
        'phone_number': phone_numbers
    })

    return df

# Terminal Command to activate the virtual environment
#    source /Users/deen/Documents/Work/Utilities/Converters/DataConverter_env/bin/activate

# Generate a large dataset for the Courses table
def generate_courses_data(num_records):
    course_ids = np.arange(1, num_records+1)
    course_names = [f'Course {i}' for i in range(1, num_records+1)]
    department_ids = np.random.randint(1, 10, size=num_records)

    df = pd.DataFrame({
        'course_id': course_ids,
        'course_name': course_names,
        'department_id': department_ids
    })

    return df

# Generate a large dataset for the Departments table
def generate_departments_data(num_records):
    department_ids = np.arange(1, num_records+1)
    department_names = [f'Department {i}' for i in range(1, num_records+1)]
    head_of_departments = [generate_name() for _ in range(num_records)]
    office_locations = [f'Office {i}' for i in range(1, num_records+1)]
    phone_numbers = np.random.randint(1000000000, 9999999999, size=num_records, dtype=np.int64)
    emails = [generate_email() for _ in range(num_records)]

    df = pd.DataFrame({
        'department_id': department_ids,
        'department_name': department_names,
        'head_of_department': head_of_departments,
        'office_location': office_locations,
        'phone_number': phone_numbers,
        'email': emails
    })

    return df

# Generate a large dataset for the Enrollments table
def generate_enrollments_data(num_records, max_student_id, max_course_id):
    enrollment_ids = np.arange(1, num_records+1)
    student_ids = np.random.randint(1, max_student_id+1, size=num_records)
    course_ids = np.random.randint(1, max_course_id+1, size=num_records)
    enrollment_dates = pd.date_range(start='2020-01-01', periods=num_records)
    grades = np.random.choice(['A', 'B', 'C', 'D', 'F'], size=num_records)

    df = pd.DataFrame({
        'enrollment_id': enrollment_ids,
        'student_id': student_ids,
        'course_id': course_ids,
        'enrollment_date': enrollment_dates,
        'grade': grades
    })

    return df

# Generate a large dataset for the Professors table
def generate_professors_data(num_records, max_department_id):
    professor_ids = np.arange(1, num_records+1)
    first_names = [generate_name() for _ in range(num_records)]
    last_names = [generate_name() for _ in range(num_records)]
    dates_of_birth = pd.date_range(start='1960-01-01', periods=num_records)
    genders = np.random.choice(['Male', 'Female'], size=num_records)
    emails = [generate_email() for _ in range(num_records)]
    phone_numbers = np.random.randint(1000000000, 9999999999, size=num_records, dtype=np.int64)
    department_ids = np.random.randint(1, max_department_id+1, size=num_records)
    office_locations = [f'Office {i}' for i in range(1, num_records+1)]
    office_hours = [f'9:00 AM - 12:00 PM' for _ in range(num_records)]

    df = pd.DataFrame({
        'professor_id': professor_ids,
        'first_name': first_names,
        'last_name': last_names,
        'date_of_birth': dates_of_birth,
        'gender': genders,
        'email': emails,
        'phone_number': phone_numbers,
        'department_id': department_ids,
        'office_location': office_locations,
        'office_hours': office_hours
    })

    return df

# Generate a large dataset for the Grades table
def generate_grades_data(num_records, max_enrollment_id, max_professor_id):
    grade_ids = np.arange(1, num_records+1)
    enrollment_ids = np.random.randint(1, max_enrollment_id+1, size=num_records)
    professor_ids = np.random.randint(1, max_professor_id+1, size=num_records)
    grades = np.random.choice(['A', 'B', 'C', 'D', 'F'], size=num_records)

    df = pd.DataFrame({
        'grade_id': grade_ids,
        'enrollment_id': enrollment_ids,
        'professor_id': professor_ids,
        'grade': grades
    })

    return df

# Generate a large dataset for the Assignments table
def generate_assignments_data(num_records, max_course_id, max_professor_id):
    assignment_ids = np.arange(1, num_records+1)
    course_ids = np.random.randint(1, max_course_id+1, size=num_records)
    professor_ids = np.random.randint(1, max_professor_id+1, size=num_records)
    assignment_names = [f'Assignment {i}' for i in range(1, num_records+1)]
    descriptions = [f'Description {i}' for i in range(1, num_records+1)]
    max_scores = np.random.randint(50, 100, size=num_records)
    deadlines = pd.date_range(start='2023-01-01', periods=num_records)

    df = pd.DataFrame({
        'assignment_id': assignment_ids,
        'course_id': course_ids,
        'professor_id': professor_ids,
        'assignment_name': assignment_names,
        'description': descriptions,
        'max_score': max_scores,
        'deadline': deadlines
    })

    return df

# Generate a large dataset for the Submissions table
def generate_submissions_data(num_records, max_assignment_id, max_enrollment_id):
    submission_ids = np.arange(1, num_records+1)
    assignment_ids = np.random.randint(1, max_assignment_id+1, size=num_records)
    enrollment_ids = np.random.randint(1, max_enrollment_id+1, size=num_records)
    submission_dates = pd.date_range(start='2023-01-01', periods=num_records)
    scores = np.random.randint(0, 100, size=num_records)
    comments = [f'Comment {i}' for i in range(1, num_records+1)]

    df = pd.DataFrame({
        'submission_id': submission_ids,
        'assignment_id': assignment_ids,
        'enrollment_id': enrollment_ids,
        'submission_date': submission_dates,
        'score': scores,
        'comments': comments
    })

    return df

# Generate and save the dataset to Parquet file
def generate_and_save_parquet(dataframe, table_name):
    table = pa.Table.from_pandas(dataframe)
    pq.write_table(table, f'{table_name}.parquet')

# Generate and save a large dataset for each table
num_records = 1000000  # Modify this number to control the size of the dataset
num_records = 100000
# Generate and save datasets for each table
students_df = generate_students_data(num_records)
generate_and_save_parquet(students_df, 'students')
num_records = 1000
courses_df = generate_courses_data(num_records)
generate_and_save_parquet(courses_df, 'courses')

departments_df = generate_departments_data(num_records)
generate_and_save_parquet(departments_df, 'departments')

enrollments_df = generate_enrollments_data(num_records, num_records, num_records)
generate_and_save_parquet(enrollments_df, 'enrollments')

professors_df = generate_professors_data(num_records, num_records)
generate_and_save_parquet(professors_df, 'professors')

grades_df = generate_grades_data(num_records, num_records, num_records)
generate_and_save_parquet(grades_df, 'grades')

assignments_df = generate_assignments_data(num_records, num_records, num_records)
generate_and_save_parquet(assignments_df, 'assignments')

submissions_df = generate_submissions_data(num_records, num_records, num_records)
generate_and_save_parquet(submissions_df, 'submissions')

print("Parquet files generated successfully!")
