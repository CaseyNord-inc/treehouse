teachers_courses = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], 'Kenneth Love': ['Python Basics', 'Python Collections', 'Something Else']}

def num_teachers(teachers_courses):
    count = 0
    for teacher in teachers_courses:
        count +=1
    return count


def num_courses(teachers_courses):
    count = 0
    for key in teachers_courses.keys():
        courses = teachers_courses[key]
        for course in courses:
            count +=1
    return count


def courses(teachers_courses):
    course_list = []
    for key in teachers_courses.keys():
        courses = teachers_courses[key]
        for course in courses:
            course_list.append(course)
    return course_list


def most_courses(teachers_courses):
    course_count = {}
    for key in teachers_courses.keys():
        max_count = 0
        courses = teachers_courses[key]
        for course in courses:
            max_count +=1
            course_count.update({key: max_count})
    most_courses = max(course_count, key=course_count.get)
    return(most_courses)


def stats(teachers_courses):
    course_count = {}
    teacher_list = []
    for key in teachers_courses.keys():
        max_count = 0
        courses = teachers_courses[key]
        for course in courses:
            max_count +=1
            course_count.update({key: max_count})
    for key in course_count.keys():
        teacher_list.append([key, course_count[key]])
    return teacher_list


