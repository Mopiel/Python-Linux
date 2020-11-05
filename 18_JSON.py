import json

def printData(data):
    for d in data:
        print("_________________________________")
        for key,value in d.items():
            print("{}\t{}".format(key,value))

fileName = 'json/myJsonFile.json'
data = []
try:
    with open(fileName) as f:
        data = json.load(f)
except:
    print("No specific file")
else:
    print("All your json data:")
    printData(data)

while True:
    inputData = input("What you want to do - Add data (+), quit program (q) or delete all data (-),show all data (*)\n")
    if(inputData == "q"):
        print("See you soon")
        break
    if (inputData == "-"):
        data = []
        print("All data removed")
        continue
    if (inputData == "*"):
        printData(data)
        continue
    if (inputData == "+"):
        print("Specyfy your car:")
        brand = input("Brand \n")
        color = input("Color \n")
        price = input("Price \n")
        height = input("Height \n")
        newData = {"Brand":brand,"Color":color,"Price":price,"Height":height}
        data.append(newData)

        continue
    print("Wrong command")

with open(fileName, 'w') as json_file:
  json.dump(data, json_file)