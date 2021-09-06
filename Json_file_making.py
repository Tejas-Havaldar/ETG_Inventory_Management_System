import json

stock = {
            '1001': {'Name': 'Wired Mouse', 'Price': 950, 'Quantity': 20, 'Mfg_Date': '01/21\n'},
            '1002': {'Name': 'Wireless Mouse', 'Price': 1250, 'Quantity': 20, 'Mfg_Date': '01/21'},
            '1003': {'Name': 'Wired Keyboard', 'Price': 1400, 'Quantity': 15, 'Mfg_Date': '01/21'},
            '1004': {'Name': 'Wireless Keyboard', 'Price': 1650, 'Quantity': 20, 'Mfg_Date': '08/20'},
            '1005': {'Name': 'Pen-drive 8gb', 'Price': 450, 'Quantity': 10, 'Mfg_Date': '09/20'},
            '1006': {'Name': 'Pen-drive 16gb', 'Price': 650, 'Quantity': 10, 'Mfg_Date': '10/20'},
            '1007': {'Name': 'Pen-drive 64gb', 'Price': 750, 'Quantity': 10, 'Mfg_Date': '06/19'},
            '1008': {'Name': 'Pen-drive 1tb', 'Price': 1000, 'Quantity': 10, 'Mfg_Date': '01/21'},
            '1009': {'Name': 'RJ-45 cable', 'Price': 50, 'Quantity': 45, 'Mfg_Date': '08/20'},
            '1010': {'Name': 'HDMI cable', 'Price': 150, 'Quantity': 50, 'Mfg_Date': '08/20'},
            '1011': {'Name': 'Charger C-Type', 'Price': 800, 'Quantity': 10, 'Mfg_Date': '06/20'},
            '1012': {'Name': 'Charger Laptop', 'Price': 2000, 'Quantity': 10, 'Mfg_Date': '02/20'},
            '1013': {'Name': 'Cooling Pad', 'Price': 760, 'Quantity': 20, 'Mfg_Date': '08/21'},
            '1014': {'Name': 'Laptop Stand', 'Price': 300, 'Quantity': 20, 'Mfg_Date': '08/20'},
            '1015': {'Name': 'Headphones', 'Price': 3500, 'Quantity': 15, 'Mfg_Date': '01/21'},
            '1016': {'Name': 'Earphones', 'Price': 900, 'Quantity': 25, 'Mfg_Date': '08/20'},
            '1017': {'Name': 'Arduino Board', 'Price': 700, 'Quantity': 12, 'Mfg_Date': '10/20'},
            '1018': {'Name': 'Raspberry pi', 'Price': 900, 'Quantity': 14, 'Mfg_Date': '05/21'},
            '1019': {'Name': '8051 Microcontroller', 'Price': 650, 'Quantity': 10, 'Mfg_Date': '05/20'},
            '1020': {'Name': 'PIC Microcontroller', 'Price': 500, 'Quantity': 10, 'Mfg_Date': '06/20'},
            '1021': {'Name': 'Ethernet Shield', 'Price': 750, 'Quantity': 10, 'Mfg_Date': '07/20'},
            '1022': {'Name': 'Servo Motor', 'Price': 25, 'Quantity': 50, 'Mfg_Date': '07/20'},
            '1023': {'Name': 'Ultrasonic Sensor', 'Price': 75, 'Quantity': 30, 'Mfg_Date': '08/19'},
            '1024': {'Name': 'LDR', 'Price': 15, 'Quantity': 40, 'Mfg_Date': '08/21'},
            '1025': {'Name': 'Metal Sensor', 'Price': 1000, 'Quantity': 10, 'Mfg_Date': '08/21'},
            '1026': {'Name': 'Glass Sensor', 'Price': 960, 'Quantity': 10, 'Mfg_Date': '08/21'},
            '1027': {'Name': 'Wifi Module', 'Price': 245, 'Quantity': 10, 'Mfg_Date': '07/20'},
            '1028': {'Name': 'Bluetooth Module ', 'Price': 300, 'Quantity': 15, 'Mfg_Date': '11/20'},
            '1029': {'Name': 'Web Camera', 'Price': 8000, 'Quantity': 7, 'Mfg_Date': '09/20'},
            '1030': {'Name': 'Speakers', 'Price': 4600, 'Quantity': 3, 'Mfg_Date': '08/21'},
         }

json_object = json.dumps(stock)


with open("stock.json", "w") as f:
    f.write(json_object)

with open("stock.json", "r") as f:
    r = f.read()
    r = stock

print(stock)
