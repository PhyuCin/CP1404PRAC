def process_data():
    data = ["2005, Q1, 0.00062", "2005, Q2, 0.000634"]

    for i in range(len(data)):
        data[i] = data[i].split(",")
        for n in range(len(data[i])):
            if n == 0:
                data[i][n] = int(data[i][n])
            elif n == 2:
                data[i][n] = float(data[i][n])
    print(data)


process_data()
