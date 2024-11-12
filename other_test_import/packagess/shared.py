from packagess import agee

print("this file is ",__name__)

def take_data(list):
    data = {"name": "", 
            "age": "",
            "list": list}
    data["name"] = input("type your name: ")
    data["age"] = agee.multipli_age()
    
    
    return data