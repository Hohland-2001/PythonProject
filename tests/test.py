# from .src.masks import get_mask_card_number, get_mask_account


def get_mask_card_number(number: str) -> str:
    mask_card_number = number[:4] + " " + number[4:6] + "** ****" + " " + number[12:]
    return mask_card_number


def get_mask_account(number: str) -> str:
    mask_account = number.replace(number[:-4], "**")
    return mask_account


print(get_mask_card_number("1234567898631472"))
print(get_mask_account('1855778781818'))
