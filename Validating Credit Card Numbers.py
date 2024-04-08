def is_valid_credit_card(credit_card_number):
    if credit_card_number[0] not in ['4', '5', '6']:
        return False
    
    credit_card_number = credit_card_number.replace("-", "")
    if not credit_card_number.isdigit() or len(credit_card_number) != 16:
        return False
    
    for i in range(len(credit_card_number) - 3):
        if credit_card_number[i] == credit_card_number[i+1] == credit_card_number[i+2] == credit_card_number[i+3]:
            return False
    
    return True

n = int(input().strip())
for _ in range(n):
    credit_card_number = input().strip()
    if is_valid_credit_card(credit_card_number):
        print("Valid")
    else:
        print("Invalid")
