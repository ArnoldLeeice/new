#модуль поиска

from export_data import export_data
from print_data import print_data

def search_data(word, data):
    if len(data) > 0:
        for item in data:
            if word in item:
                return data
    else:
        return None