file_path = 'd:/Eli Cutchen/OneDrive - BYU-Idaho/2023 (12) Spring/cse110/w06/books.txt'

books = open(file_path, 'r')
for i in books:
    print(i.strip())

books.close()