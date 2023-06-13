import json

def convert_date(date):
    return '.'.join(date[:10].split('-')[::-1])

''' :param date:
    :return:
    example 2018-06-30T02:08:58. -> 30.06.2018    '''

def masking_card(card_info:str):
    if card_info.startswith('Visa Classic') or card_info.startswith('Maestro') or card_info.startswith('Visa Platinum'):
        card_info = card_info.split()
        number = card_info[-1]
        hide_number = number[:4] + ' ' + number[4:6] + '** ' + '***** ' + number[-4:]

        return ' '.join(card_info[:-1] + [hide_number])

    elif card_info.startswith('Счет'):
        card_info = card_info.split()
        number = card_info[-1]
        hide_number = '**' + number[-4:]

        return ' '.join(card_info[:-1] + [hide_number])

def show_operation(operation):
    out = f"""{convert_date(operation['date'])} Перевод организации
{masking_card(operation['from'])} -> {masking_card(operation['to'])} 
{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}"""

    print()
    print(out)

def main():
    with open('data/operations.json', mode='r', encoding='utf-8') as file:
        data = json.load(file)

    data = filter(lambda x: x.get('state') == "EXECUTED" and x.get('from'), data)
    data = sorted(data, key=lambda x: x.get('state'), reverse=True)

    for operation in data[:5]:
        show_operation(operation)

if __name__ == '__main__':
    main()