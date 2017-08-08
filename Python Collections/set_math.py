COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers(set_of_topics):
    list_of_courses = []
    for key, value in COURSES.items():
        if value & set_of_topics:
            list_of_courses.append(key)
    print(list_of_courses)


def covers_all(set_of_topics):
    list_of_courses = []
    for key, value in COURSES.items():
        if value >= set_of_topics:
            list_of_courses.append(key)
    print(list_of_courses)

covers_all({"conditions", "input"})