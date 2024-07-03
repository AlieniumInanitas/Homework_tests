import unittest

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def get_name(doc_number):
    for doc in documents:
        if doc_number == doc['number']:
            return doc['name']
    return "Документ не найден"
    
def get_directory(doc_number):
    for key in directories.keys():
        number_list = directories[key]
        if doc_number in number_list:
            return key
    return "Полки с таким документом не найдено"
    
def add(document_type, number, name, shelf_number):
    key = str(shelf_number)
    directories[key].append(number)
    documents.append({'type': document_type, 'number': number, 'name': name})

def check_document_existance(user_doc_number):
    doc_founded = False
    for current_document in documents:
        doc_number = current_document['number']
        if doc_number == user_doc_number:
            doc_founded = True
            break
    return doc_founded

def remove_doc_from_shelf(doc_number):
    for directory_number, directory_docs_list in directories.items():
        if doc_number in directory_docs_list:
            directory_docs_list.remove(doc_number)
            break

def delete_doc(user_doc_number):
    doc_exist = check_document_existance(user_doc_number)
    if doc_exist:
        for current_document in documents:
            doc_number = current_document['number']
            if doc_number == user_doc_number:
                documents.remove(current_document)
                remove_doc_from_shelf(doc_number)
                return doc_number, True    
        



class TestAccounting(unittest.TestCase):
    def test_get_name(self):
        self.assertEqual(get_name("10006"), 'Аристарх Павлов')
    def test_get_directory(self):
        self.assertEqual(get_directory("11-2"), '1')
    def test_add(self):
        add('international passport', '311 020203', 'Александр Пушкин', 3)
        self.assertEqual(get_name("311 020203"), 'Александр Пушкин')
        self.assertEqual(get_directory("311 020203"), '3')
    def test_delete_doc(self):
        delete_doc('311 020203')
        self.assertNotEqual(get_name("311 020203"), 'Александр Пушкин')
        self.assertNotEqual(get_directory("311 020203"), '3')
    


if __name__ == '__main__':
    unittest.main()