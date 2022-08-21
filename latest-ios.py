from bs4 import BeautifulSoup
import requests
import os


def adaptive_clear():
    os.system("clear") if os.name == "posix" else os.system("cls")


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

Models_Try_Again = f"""
    {Models}
    Make sure you are only typing the given numbers above (1-34)
"""

SelectionUsed = Models

phones = {
    "1":
        {
            "id": "14,6",
            "device": "iPhone SE (3rd generation)"
        },
    "2":
        {
            "id": "14,5",
            "device": "iPhone 13"
        },
    "3":
        {
            "id": "14,1",
            "device": "iPhone 13 mini"
        },
    "4":
        {
            "id": "14,3",
            "device": "iPhone 13 Pro Max"
        },
    "5":
        {
            "id": "14,2",
            "device": "iPhone 13 Pro"
        },
    "6":
        {
            "id": "13,3",
            "device": "iPhone 12 Pro"
        },
    "7":
        {
            "id": "13,4",
            "device": "iPhone 12 Pro Max"
        },
    "8":
        {
            "id": "13,1",
            "device": "iPhone 12 mini"
        },
    "9":
        {
            "id": "13,2",
            "device": "iPhone 12"
        },
    "10":
        {
            "id": "12,8",
            "device": "iPhone SE (2020)"
        },
    "11":
        {
            "id": "12,3",
            "device": "iPhone 11 Pro"
        },
    "12":
        {
            "id": "12,1",
            "device": "iPhone 11"
        },
    "13":
        {
            "id": "12,5",
            "device": "iPhone 11 Pro Max"
        },
    "14":
        {
            "id": "11,8",
            "device": "iPhone XR"
        },
    "15":
        {
            "id": "11,6",
            "device": "iPhone XS Max"
        },
    "16":
        {
            "id": "11,2",
            "device": "iPhone XS"
        },
    "17":
        {
            "id": "10,3",
            "device": "iPhone X"
        },
    "18":
        {
            "id": "10,2",
            "device": "iPhone 8 Plus"
        },
    "19":
        {
            "id": "10,1",
            "device": "iPhone 8"
        },
    "20":
        {
            "id": "9,2",
            "device": "iPhone 7 Plus"
        },
    "21":
        {
            "id": "8,4",
            "device": "iPhone 7"
        },
    "22":
        {
            "id": "8,4",
            "device": "iPhone SE"
        },
    "23":
        {
            "id": "8,2",
            "device": "iPhone 6s+"
        },
    "24":
        {
            "id": "8,1",
            "device": "iPhone 6s"
        },
    "25":
        {
            "id": "7,2",
            "device": "iPhone 6"
        },
    "26":
        {
            "id": "7,1",
            "device": "iPhone 6+"
        },
    "27":
        {
            "id": "6,2",
            "device": "iPhone 5s"
        },
    "28":
        {
            "id": "5,4",
            "device": "iPhone 5c"
        },
    "29":
        {
            "id": "5,2",
            "device": "iPhone 5"
        },
    "30":
        {
            "id": "4,1",
            "device": "iPhone 4s"
        },
    "31":
        {
            "id": "3,1",
            "device": "iPhone 4"
        },
    "32":
        {
            "id": "2,1",
            "device": "iPhone 3Gs"
        },
    "33":
        {
            "id": "1,2",
            "device": "iPhone 3G"
        },
    "34":
        {
            "id": "1,1",
            "device": "iPhone 2g"
        },
}

adaptive_clear()
SelectionUsed = Models

while True:
    selectedModel = input(f"{SelectionUsed}\niPhone model selected: ")

    if not phones.get(selectedModel, 0):
        adaptive_clear()
        SelectionUsed = Models_Try_Again
    else:
        device = phones[selectedModel]["device"]
        id = phones[selectedModel]["id"]
        break

adaptive_clear()

url = f"https://ipsw.me/iPhone{id}"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}

result = requests.get(url, headers=headers)
doc = BeautifulSoup(result.text, "html.parser")

iosVersion = doc.find_all("td")[1].string

print("Powered by: ipsw.me\n")
print(f"The newest version of iOS for the {device} is: {iosVersion}.\n")

if id == "1,1":
    print(
        f"ALERT: You cannot restore this iPhone through iTunes, since {iosVersion} is no longer signed.\n")
