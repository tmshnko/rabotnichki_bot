import html

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

    if office:
        text += "<b>Сегодня в офисе:</b>\n" + "\n".join(office) + "\n\n"

    if lunch:
        text += "<b>Можно наланчи:</b>\n" + "\n".join(lunch)

    return text

def build_text_lunch(votes):
    lunch = []
    for username, choice in votes:
        if "no_nalunch" not in choice:
            lunch.append(username)

    if len(lunch) == 0:
        lunch.append('ничей :(') 
        
    text = "<b>Можно наланчи:</b>\n" + "\n".join(lunch)

    return text