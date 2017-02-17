

users = {
    'Students': [
        {'first_name': 'Michael', 'last_name' : 'Jordan'},
        {'first_name': 'John', 'last_name': 'Rosales'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ],
    'Instructors': [
        {'first_name': 'Martin', 'last_name': 'Choi'},
        {'first_name': 'Martin', 'last_name': 'Puryear'}
    ]
}
# print users
# print users['Students']
# print users['Students'][0]['first_name']
#
# value_at_index = users.values()[index]
# print value_at_index

for groups in users:
    print groups

    for rows, key in enumerate(users[groups]):
        # print rows
        # print key
        name_length = len(key["first_name"]) + len(key["last_name"])
        print str(rows + 1), "-", key["first_name"], key["last_name"], "-", str(name_length)
