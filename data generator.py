import csv
import random
import time


x1_value = 0
y1_value = 0
x2_value = 0
y2_value = 0
x3_value = 0
y3_value = 0
x4_value = 0
y4_value = 0
x5_value = 0
y5_value = 0
x6_value = 0
y6_value = 0
x7_value = 0
y7_value = 0
x8_value = 0
y8_value = 0

fieldnames = ["x1_value", "y1_value","x2_value", "y2_value","x3_value", "y3_value","x4_value", "y4_value","x5_value", "y5_value","x6_value", "y6_value","x7_value", "y7_value","x8_value", "y8_value"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()


while True:

    with open('data.csv','a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        info = {
            "x1_value": x1_value,
            "y1_value": y1_value,
            "x2_value": x2_value,
            "y2_value": y2_value,
            "x3_value": x3_value,
            "y3_value": y3_value,
            "x4_value": x4_value,
            "y4_value": y4_value,
            "x5_value": x5_value,
            "y5_value": y5_value,
            "x6_value": x6_value,
            "y6_value": y6_value,
            "x7_value": x7_value,
            "y7_value": y7_value,
            "x8_value": x8_value,
            "y8_value": y8_value
    
        }

        csv_writer.writerow(info)
        


        x1_value = x1_value + 1
        y1_value = y1_value + random.random()
        if y1_value>100:
            y1_value=0
        elif x1_value> 8:
            x1_value = 0
        print(x1_value, y1_value)

        x2_value = x2_value + 1
        y2_value = y2_value + random.random()
        if y2_value>100:
            y2_value=0
        elif x2_value> 8:
            x2_value = 0
        print(x2_value, y2_value)

        x3_value = x3_value + 1
        y3_value = y3_value + random.random()
        if y3_value>100:
            y3_value=0
        elif x3_value> 8:
            x3_value = 0
        print(x3_value, y3_value)

        x4_value = x4_value + 1
        y4_value = y4_value + random.random()
        if y4_value>100:
            y4_value=0
        elif x4_value> 8:
            x4_value = 0
        print(x4_value, y4_value)

        x5_value = x5_value + 1
        y5_value = y5_value + random.random()
        if y5_value>100:
            y5_value=0
        elif x5_value> 8:
            x5_value = 0
        print(x5_value, y5_value)

        x6_value = x6_value + 1
        y6_value = y6_value + random.random()
        if y6_value>100:
            y6_value=0
        elif x6_value> 8:
            x6_value = 0
        print(x6_value, y6_value)

        x7_value = x7_value + 1
        y7_value = y7_value + random.random()
        if y7_value>100:
            y7_value=0
        elif x7_value> 8:
            x7_value = 0
        print(x7_value, y7_value)

        x8_value = x8_value + 1
        y8_value = y8_value + random.random()
        if y8_value>100:
            y8_value=0
        elif x8_value> 8:
            x8_value = 0
        print(x8_value, y8_value)
        
        time.sleep(1)
