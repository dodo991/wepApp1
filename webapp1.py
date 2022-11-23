import random

student_list = ['Toygun Togay', 'Ilteris Kagan Emeksiz', 'Begum Topaloglu', 'Demet Yildirim', 'Dogukan Hazar Yurdunkulu']

# pick a random choice from a list of strings.
student = random.choice(student_list)
print(student)
for i in range(2):
    student = random.choice(student_list)
    print(student)
