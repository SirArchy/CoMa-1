# module_1.py

def function():
    print("function() aus module_1.py")

print("Text aus module_1.py")

if __name__ == "__main__":
    print("module_1.py wird direkt ausgefuehrt")
else:
    print(__name__ + " wird importiert")
