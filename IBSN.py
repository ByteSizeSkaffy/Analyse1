import string

input_data_file = 'books_isbn_01.csv'
list_of_book_isbn = []

def load_data():
    try:
        with open(input_data_file , 'r', encoding='UTF-8') as books_file_obj:
            files_content = books_file_obj.readlines()
        for item in files_content:
            book_name_isbn = item.split(',')
            book_name, book_isbn = book_name_isbn[0], book_name_isbn[1].removesuffix('\n')
            list_of_book_isbn.append((book_name, book_isbn))
    except:
        print('Exception openning file')
    return files_content

load_data()
print('Data values imported from the file:',list_of_book_isbn)

# Implement your solution starting from next line
result_isbn = list_of_book_isbn

def valid_isbn(isbn):
    
    # check for length
    if len(isbn) != 10:
        return False
     
    # Computing weighted sum
    # of first 9 digits
    _sum = 0
    for i in range(9):
        if 0 <= int(isbn[i]) <= 9:
            _sum += int(isbn[i]) * (10 - i)
        else:
            return False
         
    # Checking last digit
    if(isbn[9] != 'X' and
       0 <= int(isbn[9]) <= 9):
        return False
     
    # If last digit is 'X', add
    # 10 to sum, else add its value.
    _sum += 10 if isbn[9] == 'X' else int(isbn[9])
     
    # Return true if weighted sum of
    # digits is divisible by 11
    return (_sum % 11 == 0)


if valid_isbn(result_isbn[0][1]):
    print('Valid')
else:
    print("Invalid")

print(len(result_isbn))