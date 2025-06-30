
id = 1
lst = []

def careate(name, surname, age, course, city):
    global id
    dit = {
        'id': id,
        'name': name,
        'surname': surname,  
        'age': age,
        'course': course,
        'city': city
    }
    lst.append(dit)
    id += 1  
    print('student created successfully')

def get_all_students():
    return lst

def get_sudent_by_id (search_id):

    found = False
    for student in lst:
            if student['id'] == search_id:
                print('student found:', student)
                f = True
                break
    if student['id'] != search_id:
            print('student not found')
        

def update_student_by_id(updare_student):
    found = False
    for student in lst:
         if student['id'] == updare_student:
            found = True
            student['name']= input ('enter new name -->')
            student['surname']= input('enter new surname -->')
            student['age'] = input('enter new age -->')
            student['course']= input('enter new course -->')
            student['sity'] =input('enter new city-->')
            print('student updete successfully')
            break
    if not found:
         print('student not found')
        
def delete_student_by_id(dlete_student):
    found = False
    for student in lst:
            if student['id'] == dlete_student:
             found = True
            lst.remove(student)
            print('student dleted seccessfully')
            break
    if not found:
        print('student not found')
