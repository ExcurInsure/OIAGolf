import pandas as pd
import hashlib

def generate_hash_id(row):
    # Create a unique string for each course using course name and total yardage
    unique_str = f"{row['CourseName']}{row['TotalYds']}"
    # Generate a MD5 hash of this unique string
    return hashlib.md5(unique_str.encode()).hexdigest()

def add_course_ids(csv_path, output_path):
    # Load the CSV file
    courses_df = pd.read_csv(csv_path)
    
    # Apply the hash ID function to each row
    courses_df['CourseID'] = courses_df.apply(generate_hash_id, axis=1)
    
    # Save the modified DataFrame to a new CSV file
    courses_df.to_csv(output_path, index=False)

# Replace 'path_to_your_courses.csv' with the path to your courses CSV file
# and 'path_to_output_csv.csv' with where you want to save the modified file
csv_path = 'courses.csv'
output_path = 'courses_sql.csv'
add_course_ids(csv_path, output_path)
