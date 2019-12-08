import pandas as pd
import matplotlib.pyplot as plt


data = []
df = pd.read_csv("data.csv")
for index, row in df.iterrows():
    data.append([row[1], row[2], row[3]])


# Draw a point based on the x, y axis value.
def draw_points(point_locs):
    # x axis value list.
    x_list = []
    for point in point_locs:
        x_list.append(point[0])
    # y axis value list.
    y_list = []
    for point in point_locs:
        y_list.append(point[1])
    condition_list = []
    for point in point_locs:
        stat = point[2]
        if stat == 1:
            condition_list.append("r")
        elif stat == 2:
            condition_list.append("g")
        else:
            condition_list.append("b")

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



def main():
    draw_points(data)


if __name__ == '__main__':
    main()
