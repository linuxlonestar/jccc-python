def getFilename():
    fileName = input(f'Please enter the name of the file to process: ')
    return fileName

def getInput(fileName):
    # get input file
    with open(fileName, "r") as file:
        data = file.readlines()
        for line in data:
            inData.append(line)
         
    return inData
      
def processData(indata, keyWord):
    schoolOne = []
    schoolTwo = []
    schoolThree = []
    for line in inData:
        if line.find(keyWord) != -1:
            schoolOne.append(line)
        elif line.find(keyWord2) != -1:
            schoolThree.append(line)
        elif line.find(keyWord3) != -1:
            schoolTwo.append(line)
            
    return schoolOne, schoolTwo, schoolThree   

def main():
    s1 = []
    s2 = []
    s3 = []
    filename = getFilename()
    inData = getInput(filename)
    #print(inData)
    s1, s2, s3 = processData(inData, keyWord)
    
    print(f"\n\ndata for Avila\n\n {s1}")
    print(f"\n\ndata for Rockhurst\n\n {s3}")
    print(f"\n\ndata for JCCC\n\n {s2}\n")

    index = "Id	Fname	Lname	School id	School name	uGrad/Grad	Year	Student Loan"
    with open("avila.txt", "w") as file:
        file.write(f"{index}\n")
        for item in range(len(s1)):
            file.write(s1[item])
    with open("rockhurst.txt", "w") as file:
        file.write(f"{index}\n")
        for item in range(len(s3)):
            file.write(s3[item])
    with open("jccc.txt", "w") as file:
        file.write(f"{index}\n")
        for item in range(len(s2)):
            file.write(s2[item])

    print("All text files written.")


if __name__ == '__main__':
    inData = []
    keyWord = "Avila"
    keyWord2 = "Rockhurst"
    keyWord3 = "JCCC"
    main()

    

    