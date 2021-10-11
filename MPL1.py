import matplotlib.pyplot as plt
data, N = [], 0
try:
    with open("001.dat", "r") as file: #Вместо 001 - номер любого другого файла
        N = file.readline()
        for line in file:
            if len(line.split()) == 1:
                break
            else:
                data.append([float(x) for x in line.split()])
except FileNotFoundError:
    pass
data_x, data_y = [x[0] for x in data], [y[-1] for y in data]
plt.scatter(data_x,data_y, color='blue', s=40, marker='o')
plt.title(f'Number of points: {N}')
plt.show()


