def get_top_student(subject:str, dataset:dict) -> tuple:
    if subject not in dataset:
        return None
    
    subject_data = dataset[subject]
    top_student = max(subject_data, key=subject_data.get)
    return top_student, subject_data[top_student]

def get_top_student_in_class(dataset:dict) -> tuple:
    students_dic = {}
    for students in dataset.values():
        for student, mark in students.items():
            print(student, mark)
            if student not in students_dic.keys():
                students_dic[student] = mark
            else:
                students_dic[student] +=mark
            
    print('dic', students_dic)
    return max(students_dic, key=students_dic.get), students_dic[max(students_dic, key=students_dic.get)]
    
            
lines = None
with open('marks.txt') as file:
    lines = file.readlines()
    print(type(lines))

if not lines:
    print("something went wrong, no lines read")
    exit()
    
marks_lines = lines[1:]  # Skip the header line

subject_marks  = {}

for line in marks_lines:
    entries = line.strip(',')
    name = entries.split(',')[0].strip()
    subject = entries.split(',')[1].strip()
    mark = int(entries.split(',')[2].strip())
    
    if subject not in subject_marks:
        subject_marks[subject] = {}
        
    subject_marks[subject][name] = mark
    
print(subject_marks)
msg = "Results\n========================================\n"

for subject in subject_marks.keys():
    name, marks = get_top_student(subject, subject_marks)
    msg += f'\nTop student in {subject}: {name} - {marks}'

# Top student in entire class
name, total = get_top_student_in_class(subject_marks)
msg += f'\n\nTop student in class: {name} - {total}'

with open('results.txt', 'w') as file:
    file.write(msg)