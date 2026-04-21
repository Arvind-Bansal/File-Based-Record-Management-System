from pathlib import Path

#THIS FUNCTION IS FOR READING THE FILE AND FOLDE
def readfileandfolder():#[this funtion will give all the file and folder present in the path]
    path=Path('')#HERE EMPTY SPACE MEANS THAT YOU WILL GET THE PATH OF THE FILE OR FOLDER IN WHICH THIS PYTHON FILE IS PRESENT IN THIS VARIABLE
    items=list(path.rglob('*'))#IT IS USED TO READ THE FILE AND FOLDER IN THE PATH RECURSIVELY AND PROVIDE THE ITEMS OF THEM
    for i,items in enumerate(items):#WE USE ENUMERATE FUNCTION TO GET THE INDEX OF THE ITEM AND THE ITEM ITSELF
        print(f"{i+1}. {items}")

def createfile():
    try:
        readfileandfolder()
        name=input("enter the name of your file")
        p=Path(name)
        if not p.exists():
            with open(p, mode='w') as f:#THIS IS USED TO OPEN THE FILE IN WRITE MODE
                content=input("enter the content of the file")
                f.write(content)
                print("file created successfully")
        else:
            print("file already exists")
    except Exception as Err:
        print(f"an error as occured as {Err}")


def readfile():
    try:
        readfileandfolder()
        name=input("enter the name of your file")
        p=Path(name)
        if p.exists() and p.is_file():#THIS IS USED TO CHECK WHETHER THE FILE EXISTS OR NOT AND WHETHER IT IS A FILE OR NOT
            with open(p, mode='r') as f:#THIS IS USED TO OPEN THE FILE IN READ MODE
                content=f.read()
                print(content)
        else:
            print("file does not exist")
    except Exception as Err:
        print(f"an error as occured as {Err}")


def updatefile():
    try:
        readfileandfolder()
        name=input("enter the name of your file")
        p=Path(name)
        if p.exists() and p.is_file():
            print("1 for changing the name of the file")
            print("press 2 for overwritting the content of the file")
            print("press 3 for appending the content of the file")
            response=int(input("enter your choice:"))
            if response==1:
                name2=input("enter the new name of the file")
                p2=Path(name2)
                if not p2.exists():
                    p.rename(p2)
                    print("file name changed successfully")
                else:
                    print("file with the new name already exists")
            elif response==2:
                with open(p, mode='w') as f:
                    content=input("enter the new content of the file")
                    f.write(content)
                    print("file content updated successfully")
            elif response==3:
                with open(p, mode='a') as f:
                    content=input("enter the content to append to the file")
                    f.write(" "+content)
                    print("content appended to the file successfully")
        else:
            print("file does not exist")
    except Exception as Err:
        print(f"an error as occured as {Err}")


def deletefile():    
    try:
        readfileandfolder()
        name=input("enter the name of your file which you want to delete")
        p=Path(name)

        if p.exists() and p.is_file():
            p.unlink()#THIS IS USED TO DELETE THE FILE
            print("file deleted successfully")
        else:
            print("file does not exist")
    except Exception as Err:
        print(f"an error as occured as {Err}")


print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

choice=int(input("enter your choice:"))
if choice==1:
    createfile()
elif choice==2:
    readfile()
elif choice==3:
    updatefile()
elif choice==4:
    deletefile()
else:
    print("invalid choice")