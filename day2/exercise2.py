def build_user(*tag, **details):
    details["tag"] = tag
    return details
user_profile = build_user("Arjun", "Nepal", age = 22, role = "developer")
print (user_profile)