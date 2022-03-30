try:
    fileName = "GuestList.txt"
    accessMode = "r"
    myFile=open(fileName, accessMode)
    line = myFile.readline()
    a=0
    while line != "" :
        if line !='':
            a=a+1
        print(a,":",line)
        line = myFile.readline()
except FileNotFoundError:
    print("파일이 존재하지 않습니다.")

myFile.close()
