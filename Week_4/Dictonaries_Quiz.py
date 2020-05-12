"""
1.Question 1
The email_list function receives a dictionary, which contains domain names as keys,
and a list of users as values. Fill in the blanks to generate a list that contains complete
email addresses (e.g. diana.prince@gmail.com).
"""


def email_list(domains):
    emails = []
    for names, users in domains.items():
        for user in users:
            emails.append(user + "@" + names)
    return (emails)


print(email_list(
    {"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"],
     "hotmail.com": ["bruce.wayne"]}))

"""
2.Question 2
The groups_per_user function receives a dictionary, which contains group names 
with the list of users. Users can belong to multiple groups. 
Fill in the blanks to return a dictionary 
with the users as keys and a list of their groups as values.
"""

def groups_per_user(group_dictionary):
    user_groups = {}
    for group, users in group_dictionary.items():
        for user in users:
            if user not in user_groups:
                user_groups[user] = []
            user_groups[user].append(group)
    return user_groups


print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))
