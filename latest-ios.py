from bs4 import BeautifulSoup
import requests
import os

def adaptive_clear():
    os_version = os.name

    if os_version == "posix":
        os.system("clear")
    else:
        os.system("cls")

adaptive_clear()

id = ""
device = ""

Models = """
    Powered by: ipsw.me

    WARNING: These are only the basic releases. GSM/CDMA/GLOBAL models aren't included.

     1. iPhone SE (3rd generation)
     2. iPhone 13
     3. iPhone 13 mini
     4. iPhone 13 Pro Max
     5. iPhone 13 Pro
     6. iPhone 12 Pro
     7. iPhone 12 Pro Max
     8. iPhone 12 mini
     9. iPhone 12
    10. iPhone SE (2020)
    11. iPhone 11 Pro
    12. iPhone 11
    13. iPhone 11 Pro Max
    14. iPhone XR
    15. iPhone XS Max
    16. iPhone XS
    17. iPhone X
    18. iPhone 8 Plus
    19. iPhone 8
    20. iPhone 7 Plus
    21. iPhone 7
    22. iPhone SE
    23. iPhone 6s+
    24. iPhone 6s
    25. iPhone 6
    26. iPhone 6+
    27. iPhone 5s
    28. iPhone 5c
    29. iPhone 5
    30. iPhone 4
    31. iPhone 4s
    32. iPhone 3Gs
    33. iPhone 3G
    34. iPhone 2G
    """

Models_Try_Again = """
    Powered by: ipsw.me

    WARNING: These are only the basic releases. GSM/CDMA/GLOBAL models aren't included.

     1. iPhone SE (3rd generation)
     2. iPhone 13
     3. iPhone 13 mini
     4. iPhone 13 Pro Max
     5. iPhone 13 Pro
     6. iPhone 12 Pro
     7. iPhone 12 Pro Max
     8. iPhone 12 mini
     9. iPhone 12
    10. iPhone SE (2020)
    11. iPhone 11 Pro
    12. iPhone 11
    13. iPhone 11 Pro Max
    14. iPhone XR
    15. iPhone XS Max
    16. iPhone XS
    17. iPhone X
    18. iPhone 8 Plus
    19. iPhone 8
    20. iPhone 7 Plus
    21. iPhone 7
    22. iPhone SE
    23. iPhone 6s+
    24. iPhone 6s
    25. iPhone 6
    26. iPhone 6+
    27. iPhone 5s
    28. iPhone 5c
    29. iPhone 5
    30. iPhone 4
    31. iPhone 4s
    32. iPhone 3Gs
    33. iPhone 3G
    34. iPhone 2G

    Make sure you are only typing the given numbers above (1-34)

"""

SelectionUsed = Models


while True:
    print(SelectionUsed)
    selectedModel = int(input("iPhone model selected: "))

    if selectedModel == 1:
        id = "14,6"
        device = "iPhone SE (3rd generation)"
        break
    elif selectedModel == 2:
        id = "14,5"
        device = "iPhone 13"
        break
    elif selectedModel == 3:
        id = "14,1"
        device = "iPhone 13 mini"
        break
    elif selectedModel == 4:
        id = "14,3"
        device = "iPhone 13 Pro Max"
        break
    elif selectedModel == 5:
        id = "14,2"
        device = "iPhone 13 Pro"
        break
    elif selectedModel == 6:
        id = "13,3"
        device = "iPhone 12 Pro"
        break
    elif selectedModel == 7:
        id = "13,4"
        device = "iPhone 12 Pro Max"
        break
    elif selectedModel == 8:
        id = "13,1"
        device = "iPhone 12 mini"
        break
    elif selectedModel == 9:
        id = "13,2"
        device = "iPhone 12"
        break
    elif selectedModel == 10:
        id = "12,8"
        device = "iPhone SE (2020)"
        break
    elif selectedModel == 11:
        id = "12,3"
        device = "iPhone 11 Pro"
        break
    elif selectedModel == 12:
        id = "12,1"
        device = "iPhone 11"
        break
    elif selectedModel == 13:
        id = "12,5"
        device = "11 Pro Max"
        break
    elif selectedModel == 14:
        id = "11,8"
        device = "iPhone XR"
        break
    elif selectedModel == 15:
        id = "11,6"
        device = "iPhone XS Max"
        break
    elif selectedModel == 16:
        id = "11,2"
        device = "iPhone XS"
        break
    elif selectedModel == 17:
        id = "10,3"
        device = "iPhone X"
        break
    elif selectedModel == 18:
        id = "10,2"
        device = "iPhone 8 Plus"
        break
    elif selectedModel == 19:
        id = "10,1"
        device = "iPhone 8"
        break
    elif selectedModel == 20:
        id = "9,2"
        device = "iPhone 7 Plus"
        break
    elif selectedModel == 21:
        id = "9,1"
        device = "iPhone 7"
        break
    elif selectedModel == 22:
        id = "8,4"
        device = "iPhone SE"
        break
    elif selectedModel == 23:
        id = "8,2"
        device = "iPhone 6s+"
        break
    elif selectedModel == 24:
        id = "8,1"
        device = "iPhone 6s"
        break
    elif selectedModel == 25:
        id = "7,2"
        device = "iPhone 6"
        break
    elif selectedModel == 26:
        id = "7,1"
        device = "iPhone 6+"
        break
    elif selectedModel == 27:
        id = "6,2"
        device = "iPhone 5s"
        break
    elif selectedModel == 28:
        id = "5,4"
        device = "iPhone 5c"
        break
    elif selectedModel == 29:
        id = "5,2"
        device = "iPhone 5"
        break
    elif selectedModel == 30:
        id = "3,1"
        device = "iPhone 4"
        break
    elif selectedModel == 31:
        id = "4,1"
        device = "iPhone 4s"
        break
    elif selectedModel == 32:
        id = "2,1"
        device = "iPhone 3Gs"
        break
    elif selectedModel == 33:
        id = "1,2"
        device = "iPhone 3G"
        break
    elif selectedModel == 34:
        id = "1,1"
        device = "iPhone 2G"
        break

    else:
        adaptive_clear()
        SelectionUsed = Models_Try_Again


adaptive_clear()

url = "https://ipsw.me/iPhone{}".format(id)
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

tag = str(doc.find_all("td")[1])

tagNoBeginningSuc = tag.replace('<td class="text-success">', '')
tagNoEndSuc = tagNoBeginningSuc.replace('</td>', '')

tagNoBeginningFail = tag.replace('<td class="text-danger">', '')
tagNoEndFail = tagNoBeginningFail.replace('</td>', '')

if id == "1,1":
    print("Powered by: ipsw.me")
    print("")
    print("The newest version of iOS for the", device, "is: {}.".format(tagNoEndFail))
    print("")
    print("ALERT: You cannot restore this iPhone through iTunes, since {} is no longer signed.".format(tagNoEndFail))
    print("")
else:
    print("Powered by: ipsw.me")
    print("")
    print("The newest version of iOS for the", device, "is: {}.".format(tagNoEndSuc))
    print("")