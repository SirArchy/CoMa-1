# module_2.py

import module_1

print("Text aus module_2.py")
module_1.function()

if __name__ == "__main__":
    print("module_2.py wird direkt ausgefuehrt")
else:
    print(__name__ + " wird importiert")
