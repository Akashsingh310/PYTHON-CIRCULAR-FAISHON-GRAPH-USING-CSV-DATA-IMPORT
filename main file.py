import random
from itertools import count
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

index = count()

def animate(i):
    data = pd.read_csv('data.csv')
    x1 = data['x1_value']
    y1 = data['y1_value']
    x2 = data['x2_value']
    y2 = data['y2_value']
    x3 = data['x3_value']
    y3 = data['y3_value']
    x4 = data['x4_value']
    y4 = data['y4_value']
    x5 = data['x5_value']
    y5 = data['y5_value']
    x6 = data['x6_value']
    y6 = data['y6_value']
    x7 = data['x7_value']
    y7 = data['y7_value']
    x8 = data['x8_value']
    y8 = data['y8_value']
        
    
    plt.cla()
    plt.plot(x1, y1, label='Communication Channel 1')
    plt.plot(x2, y2, label='Communication Channel 2')
    plt.plot(x3, y3, label='Communication Channel 3')
    plt.plot(x4, y4, label='Communication Channel 4')
    plt.plot(x5, y5, label='Communication Channel 5')
    plt.plot(x6, y6, label='Communication Channel 6')
    plt.plot(x7, y7, label='Communication Channel 7')
    plt.plot(x8, y8, label='Communication Channel 8')

    plt.legend(loc='upper left')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval = 1000)

plt.tight_layout()

plt.show()
