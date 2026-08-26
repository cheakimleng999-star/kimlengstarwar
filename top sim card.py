import csv
from datetime import datetime
import os

def get_carrier(choice):
    carriers = {
        'm': 'Metfone',
        's': 'Smart',
        'c': 'Cellcard'
    }
    return carriers.get(choice.lower(), 'Unknown')

def save_top_up(amount, name, carrier):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    data = [date, time, name, carrier, f"${amount:.2f}"]  # Fixed amount formatting to 2 decimal places

    file_exists = os.path.isfile('topups.csv')

    with open('topups.csv', 'a', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "Time", "Name", "Carrier", "Amount"])
        writer.writerow(data)

    print(f"✅ Saved: {date} {time} | {name} | {carrier} | ${amount:.2f}")

def main():
    print("=======================================")
    print("=======================================")
    print("========welcome to system suga=========")
    print("=======================================")
    print("=======================================")
    print("📱 SIM CARD TOP-UP SYSTEM")
    print("(Enter 'q' to quit)\n")

    while True:
        try:
            name = input("Name (支持中文/English): ")
            if name.lower() == 'q':
                break

            while True:
                carrier_choice = input("Select Carrier (M)etfone/(S)mart/(C)ellcard: ").lower()
                if carrier_choice in ['m', 's', 'c']:
                    carrier = get_carrier(carrier_choice)
                    break
                elif carrier_choice == 'q':
                    return
                else:
                    print("Please enter M, S, or C")

            amount = input("Amount (e.g., 1.50): $")
            if amount.lower() == 'q':
                break

            save_top_up(float(amount), name, carrier)

        except ValueError:
            print("Please enter a valid amount (e.g. 1.5)")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()