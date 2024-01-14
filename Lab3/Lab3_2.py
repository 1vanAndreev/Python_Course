def find_common_participants(group1, group2, separator=','):
    participants1 = group1.split(separator)
    participants2 = group2.split(separator)

    set1 = set(participants1)
    set2 = set(participants2)

    common_participants = list(set1.intersection(set2))

    common_participants.sort()

    return common_participants

group1 = "Иван,Роман,Владислав,Андрей"
group2 = "Роман,Даниил,Владислав,Артемий"

result = find_common_participants(group1, group2)

print("Common participants:", result)
