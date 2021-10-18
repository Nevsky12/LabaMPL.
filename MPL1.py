import matplotlib.pyplot as plt
data, N, file_name = [], 0, ""
size = 5
try:
    file_name = input()
    with open(file_name, "r") as file:
        N = file.readline()
        for line in file:
            if len(line.split()) == 1:
                break
            else:
                data.append([float(x) for x in line.split()])
except FileNotFoundError:
    pass
if file_name == "005.dat":
    size = 0.005
data_x, data_y = [x[0] for x in data], [y[-1] for y in data]
plt.scatter(data_x,data_y, color='blue', s=size)
plt.title(f'Number of points: {N}')
plt.show()


