print("Electricity bill estimator\n")

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff = int(input("Which tariff? 11 or 31: "))
while tariff != 11 and tariff != 31:
    print("Invalid choice!")
    tariff = int(input("Which tariff? 11 or 31: "))

if tariff == 11:
    dollar_per_kwh = TARIFF_11
else:
    dollar_per_kwh = TARIFF_31

daily_use_in_kwh = float(input("Enter daily use in kWh: "))
num_of_days = int(input("Enter number of billing days: "))

bill = dollar_per_kwh * daily_use_in_kwh * num_of_days

print("\nEstimated bill: ${:.2f}.".format(bill))