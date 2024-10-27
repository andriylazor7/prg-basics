def hide(card_number):
    hided_card_number = ''
    for index, digit in enumerate(card_number):
        if index >= len(card_number) - 14 and index < len(card_number) - 4:
            hided_card_number += '*'
        else:
            hided_card_number += digit
    return hided_card_number

      
    