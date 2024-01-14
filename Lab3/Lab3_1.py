def find_item_index(item_list, target_item):
    try:
        index = item_list.index(target_item)
        return index
    except ValueError:
        return None

item_list = ["яблоко", "груша", "апельсин", "груша", "банан"]
target_item = "груша"

result = find_item_index(item_list, target_item)

if result is not None:
    print(f"Индекс первого вхождения товара '{target_item}': {result}")
else:
    print(f"Товар '{target_item}' не найден в списке")
