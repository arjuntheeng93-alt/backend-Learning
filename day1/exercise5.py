def safe_append(original_list, items):
    new_list = original_list.copy()
    new_list.append(items)
    return new_list

name = ["alice", "bob"]

new_name = safe_append(name, "charlie")
print("new_list:", new_name)
print("original_list:", name)
