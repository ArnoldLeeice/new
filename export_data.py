#модуль экспорта

def export_data():
    with open('phone.csv', 'r', encoding='utf-16') as file:
        data = []
        t = []
        for line in file:
            if line != '\n':
                t.append(line.strip())
            else:
                data.append(t)
                t = []
    return