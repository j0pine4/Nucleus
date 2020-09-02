import os

FILE_LIST = []

def fileManager():
    start = 'CSV Files/'
    get_files = os.listdir('CSV Files/')

    for items in get_files:
        FILE_LIST.append(start + items)

    print(FILE_LIST)

fileManager()



