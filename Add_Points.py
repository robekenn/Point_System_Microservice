def add_points(userID, num, data):
    for user in data.get("users", []):
        if user.get("id") == userID:
            user["points"] = user.get("points", 0) + num
            return user.get("points", 0)
    return "NA"