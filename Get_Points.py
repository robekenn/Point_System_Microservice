def get_points(userID, data):
    for user in data.get("users", []):
        if user.get("id") == userID:
            return user.get("points", 0)
    return "NA" 