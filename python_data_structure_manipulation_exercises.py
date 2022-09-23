# How many students are there?
students = len(students)
print(students)

# How many students prefer light coffee? For each type of coffee roast?

light_coffee = 0
for student in students:
    if student['coffee_preference'] == 'light':
        light_coffee += 1
print(light_coffee)


# How many types of each pet are there?

pet_types = []
for student in students:
    pet_types.append(student['pet'])
print(max(set(pet_types), key=pet_types.count))


# How many grades does each student have? Do they all have the same number of grades?

grades = []
for student in students:
    grades.append(len(student['grades']))
print(max(set(grades), key=grades.count))

# What is each student's grade average?

for student in students:
    print(sum(student['grades']) / len(student['grades']))


# How many pets does each student have?

pets = []
for student in students:
    pets.append(len(student['pet']))
print(max(set(pets), key=pets.count))


# How many students are in web development? data science?

web_development = 0
data_science = 0
for student in students:

    if student['course'] == 'web development':
        web_development += 1
    elif student['course'] == 'data science':
        data_science += 1
print(web_development)
print(data_science)


# What is the average number of pets for students in web development?

pets = []
for student in students:
    if student['course'] == 'web development':
        pets.append(len(student['pet']))
print(sum(pets) / len(pets))


# What is the average pet age for students in data science?

pet_ages = []
for student in students:
    if student['course'] == 'data science':
        pet_ages.append(student['pet_age'])
print(sum(pet_ages) / len(pet_ages))


# What is most frequent coffee preference for data science students?

coffee_preferences = []
for student in students:
    if student['course'] == 'data science':
        coffee_preferences.append(student['coffee_preference'])
print(max(set(coffee_preferences), key=coffee_preferences.count))


# What is the least frequent coffee preference for web development students?

coffee_preferences = []
for student in students:
    if student['course'] == 'web development':
        coffee_preferences.append(student['coffee_preference'])
print(min(set(coffee_preferences), key=coffee_preferences.count))


# What is the average grade for students with at least 2 pets?

grades = []
for student in students:
    if len(student['pet']) >= 2:
        grades.append(sum(student['grades']) / len(student['grades']))
print(sum(grades) / len(grades))


# How many students have 3 pets?

students_with_3_pets = 0
for student in students:
    if len(student['pet']) == 3:
        students_with_3_pets += 1
print(students_with_3_pets)


# What is the average grade for students with 0 pets?

grades = []
for student in students:
    if len(student['pet']) == 0:
        grades.append(sum(student['grades']) / len(student['grades']))
print(sum(grades) / len(grades))


# What is the average grade for web development students? data science students?

web_development_grades = []
data_science_grades = []
for student in students:
    if student['course'] == 'web development':
        web_development_grades.append(sum(student['grades']) / len(student['grades']))
    elif student['course'] == 'data science':
        data_science_grades.append(sum(student['grades']) / len(student['grades']))
print(sum(web_development_grades) / len(web_development_grades))
print(sum(data_science_grades) / len(data_science_grades))

# What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?

grades = []
for student in students:
    if student['coffee_preference'] == 'dark':
        grades.append(max(student['grades']) - min(student['grades']))
print(sum(grades) / len(grades))


# What is the average number of pets for medium coffee drinkers?

avg_pets_coffee = [student['pets'] for student in students if student['coffee_preference'] == 'medium']

# What is the most common type of pet for web development students?

pet_web_dev = [student['pets'] for student in students if student['course'] == 'web development']

# What is the average name length?

avg_name_length = [len(student['name']) for student in students]

# What is the highest pet age for light coffee drinkers?

pet_age_high = [student['pets'] for student in students if student['coffee_preference'] == 'light']


students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]