# Student Marks Calculator

# Function to calculate grade
def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

# Input number of subjects
num_subjects = int(input("Enter number of subjects: "))

marks = []  # list to store marks

# Loop to take input
for i in range(num_subjects):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

# Calculate total and average
total = sum(marks)
average = total / num_subjects

# Calculate grade
grade = calculate_grade(average)

# Print results
print("\n===== Student Report =====")
print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)
