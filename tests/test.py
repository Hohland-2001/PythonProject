def get_mask_card_number(number: str) -> str:
    """Функция маскирует номер карты"""
    mask_card_number = number[:4] + " " + number[4:6] + "** **** " + number[12:]
    return mask_card_number


def get_mask_account(number: str) -> str:
    """Функция маскирует номер счёта"""
    mask_account = number.replace(number[:-4], "**")
    return mask_account


def mask_account_card(number: str) -> str:
    number_list = number.split()
    if number_list[0] == 'Счет':
        number_list[1] = get_mask_account(number_list[1])
    else:
        number_list[1] = get_mask_card_number(number_list[1])
    mask = ' '.join(number_list)
    return mask


def get_date(date: str) -> str:
    new_date = date[8:10] + date[4:8] + date[:4]
    new_date = new_date.replace('-', '.')
    return new_date


print(mask_account_card('MasterCard 7158300734726758'))
print(mask_account_card('Счет 64686473678894779589'))
