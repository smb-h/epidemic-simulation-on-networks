import pandas as pd
import matplotlib.pyplot as plt
from time import sleep
from random import randrange


data = []
df = pd.read_csv("data.csv")
for index, row in df.iterrows():
    data.append([row[1], row[2], int(row[3]), row[4]])

data.sort()

# find neighbor points
def find_neighbors(x, y, point_locs):
    # calculate with radius of 3000
    rs = []
    r = 3000
    for point in point_locs:
        x_diff_range = [abs(x - r), abs(x + r)]
        y_diff_range = [abs(y - r), abs(y + r)]
        if (x_diff_range[0] < point[0] < x_diff_range[1]) and (y_diff_range[0] < point[1] < y_diff_range[1]) :
            rs.append(point)
    print("#########################################################")
    print(rs)
    return rs


# Draw a point based on the x, y axis value.
def draw_points(point_locs):
    # x axis value list.
    x_list = []
    # y axis value list.
    y_list = []
    # time list
    time_list = []
    # condition list - red as infected, green for cured, blue for normal
    condition_list = []
    for point in point_locs:
        x_list.append(point[0])
        y_list.append(point[1])
        time_list.append(point[2])
        condition_list.append(point[3])
        # find closest to infected


    # Draw point based on above x, y axis values.
    # plt.scatter(x_list, y_list, s=15, c="b")
    for indx in range(len(x_list)):
        plt.scatter(x_list[indx], y_list[indx], s=15, c=condition_list[indx])
    # Set chart title.
    plt.title("people", fontsize=19)
    # Set x axis label.
    plt.xlabel("X", fontsize=10)
    # Set y axis label.
    plt.ylabel("Y", fontsize=10)
    # Display the plot in the matplotlib's viewer.
    plt.show()
    # input("press any key to continue")


# Update time
def update_time(point_locs):
    for point in point_locs:
        point[2] += 1
        stat = point[3]
        # cure after 3 sec of infection
        if stat == "r" and point[2] >= 3:
            p = randrange(100)
            # 95% chance to cure
            if p < 95:
                point[3] = "g"
                point[2] = 0
        # infect
        elif stat == "r":
            p = randrange(100)
            # 95% chance to infect
            if p < 95:
                neighbors = find_neighbors(point[0], point[1], point_locs)
                if neighbors:
                    for ng in neighbors:
                        ng_stat = ng[3]
                        p2 = randrange(100)
                        # 99% to infect
                        if ng_stat == "b" and p2 < 99:
                            ng[3] = "r"
                            ng[2] = 0
                        # 1% chance to infect cured people
                        elif (p2 < 1) and ng_stat == "g":
                            ng[3] = "r"
                            ng[2] = 0

    draw_points(point_locs)




def main():
    draw_points(data)
    # Time to live
    for t in range(20):
        sleep(.1)
        update_time(data)




if __name__ == '__main__':
    main()
