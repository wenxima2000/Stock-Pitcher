# main.py
from data_loader import load_data
from analysis import analyze_returns
from visualize import plot_stock
from investment_advisor import give_investment_advice
from fetch_data import fetch_data
import os

def main():
    print("📈 This is Stock Pitcher, a tool to help you analyze capital market.")

    while True:
        print("\n=== Main Menu ===")
        print("1. Load your local stock date")
        print("2. Fetch data online from Yahoo Finance")
        print("3. Exit Stock Pitcher")
        choice = input("Please select function (1-3): ")

        if choice == "1":
            filename = input("Type in file path(format: data/AAPL.csv): ").strip()
            if not os.path.exists(filename):
                print("❌ Cannot find it, please check the path.")
                continue

            try:
                data = load_data(filename)
                data = analyze_returns(data)
            except Exception as e:
                print(f"⚠️ Error happens: {e}")
                continue

        elif choice == "2":
            ticker = input("Type in stock ticker(e.g. AAPL、TSLA、MSFT): ").strip().upper()
            data = fetch_data(ticker)
            if data is None:
                continue
            data = analyze_returns(data)

        elif choice == "3":
            print("👋 Thanks for choosing Stock Pitcher, See you!")
            break

        else:
            print("⚠️ Please choose between 1-3")
            continue

        while True:
            print("\n=== Analyze Menu ===")
            print("1. Trend Visualization")
            print("2. Investment advice")
            print("3. Pitch another stock")
            print("4. Back to main menu")
            next_choice = input("Please select function (1-4): ")

            if next_choice == "1":
                plot_stock(data)
                continue
            elif next_choice == "2":
                give_investment_advice(data)
                continue
            elif next_choice == "3":
                break 
            elif next_choice == "4":
                break  
            else:
                print("⚠️ Please choose between 1-4")

if __name__ == "__main__":
    main()
