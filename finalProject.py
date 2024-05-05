keyWord = input("\nPlease input keyword to search in Project_Data.txt\n")
fList = []

def search():
    with open(r'Project_Data.txt', 'r') as data:
        lines = data.readlines()
        for row in lines:
            # check if string present on a current line
            #print(row.find(word))
            # find() method returns -1 if the value is not found,
            # if found it returns index of the first occurrence of the substring
            data.index(keyWord)
            if row.find(keyWord) != -1:
                fList.append(keyWord, )
                print('line Number:', lines.index(row))

search()   