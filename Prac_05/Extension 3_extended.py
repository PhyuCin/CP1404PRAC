"""Asks the user the tariff they use, daily use in kWh, and number of billing days to calculate estimated bill.
(Adds more tariffs)"""


def main():
    print("Electricity bill estimator\n")

    tariff_to_cost = {'11': 0.244618, '31': 0.136928, '15': 0.15031996, '23': 0.23022016, '25': 0.25021999}
    tariff = ""
    valid = False
    while valid is False:
        print(", ".join("{}: {}".format(k, v) for k, v in tariff_to_cost.items()))
        tariff = input("Which tariff? 11, 15, 23, 25 or 31: ")
        valid = check(tariff, tariff_to_cost)

    dollar_per_kwh = tariff_to_cost[tariff]
    print("Dollar per kWh: ", dollar_per_kwh)

    daily_use_in_kwh = float(input("\nEnter daily use in kWh: "))
    num_of_days = int(input("Enter number of billing days: "))

    bill = dollar_per_kwh * daily_use_in_kwh * num_of_days

    print("\nEstimated bill: ${:.2f}.".format(bill))


def check(tariff, tariff_to_cost):
    for key, value in tariff_to_cost.items():
        if key == tariff:
            return True
    print("Invalid choice!\n")
    return False


main()
