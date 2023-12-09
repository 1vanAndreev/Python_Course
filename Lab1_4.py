def get_visits_statistics(users_list):
  visits_statistics = {
    "Общее количество": 0,
    "Уникальные посещения": 0
  }
  visits_statistics["Общее количество"] = len(users_list)
  unique_users = set(users_list)
  visits_statistics["Уникальные посещения"] = len(unique_users)
  return visits_statistics

users_list = ["Иван", "Петр", "Сергей", "Иван", "Петр"]
visits_statistics = get_visits_statistics(users_list)
print(visits_statistics)
