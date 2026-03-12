def build_text(votes):
    office = []
    lunch = []

    for username, choice in votes:

        if "office" in choice:
            office.append(username)

        if "no_nalunch" not in choice:
            lunch.append(username)

    text = "Ну что братва?\n\n"

    if not votes:
        return text

    text += "**Сегодня в офисе:**\n"
    for user in office:
        text += f"{user}\n"

    text += "\n**Можно наланчи:**\n"
    for user in lunch:
        text += f"{user}\n"

    return text