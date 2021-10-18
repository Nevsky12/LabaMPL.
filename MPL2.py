import matplotlib.pyplot as plt
import time

data_x, data_y, count = [], [], 0
try:
    with open("frames.dat.txt", "r") as file:
        for line in file:
            if count % 2 == 0:
                data_x = [float(x) for x in line.split()]
            else:
                data_y = [float(y) for y in line.split()]
            count += 1
            if count >= 2 and count % 2 == 0:
                plt.ion()
                plt.clf()
                plt.axis([0,16, -9,14])
                plt.title(f'Frame {count // 2}')
                plt.plot(data_x, data_y)
                plt.draw()
                plt.grid(True)
                plt.gcf().canvas.flush_events()
                time.sleep(0.5)
                plt.show()
        data_x = []
        data_y = []
except FileNotFoundError:
    pass
plt.ioff()
