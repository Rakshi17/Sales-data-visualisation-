import pandas as pd
import matplotlib.pyplot as plt

def information(months, sales):
    """Visualize the sales data using matplotlib."""
    df = pd.DataFrame({'Month': months, 'Sales': sales})
    plt.figure(figsize=(8, 5))
    plt.plot(df['Month'], df['Sales'], marker='o', linestyle='-', color='red')
    plt.title('Monthly Sales Data')
    plt.xlabel('Month')
    plt.ylabel('Sales (INR)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    try:
        df = pd.read_csv('/content/Stores.csv')
    except FileNotFoundError:
        print("Error: CSV file not found.")
        return

    # Extract months and sales from DataFrame
    months=df['Month'].tolist()
    sales =df['Sales'].tolist()

    # Visualize the sales data
    information(months, sales)

    # Calculate and print the total sales amount for all months
    total_sales = sum(sales)
    print(f"\n\t\tTotal sales amount for all months: ₹{total_sales:.2f}\n")

    # Additional feature: Display the highest and lowest sales months
    if months:
        max_sales_month = months[sales.index(max(sales))]
        min_sales_month = months[sales.index(min(sales))]
        print(f"\t\tHighest sales month: {max_sales_month} (₹{max(sales):.2f})\n")
        print(f"\t\tLowest sales month: {min_sales_month} (₹{min(sales):.2f})\n")
        
main()import pandas as pd
import matplotlib.pyplot as plt

def information(months, sales):
    """Visualize the sales data using matplotlib."""
    df = pd.DataFrame({'Month': months, 'Sales': sales})
    plt.figure(figsize=(8, 5))
    plt.plot(df['Month'], df['Sales'], marker='o', linestyle='-', color='red')
    plt.title('Monthly Sales Data')
    plt.xlabel('Month')
    plt.ylabel('Sales (INR)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    try:
        df = pd.read_csv('/content/Stores.csv')
    except FileNotFoundError:
        print("Error: CSV file not found.")
        return

    # Extract months and sales from DataFrame
    months=df['Month'].tolist()
    sales =df['Sales'].tolist()

    # Visualize the sales data
    information(months, sales)

    # Calculate and print the total sales amount for all months
    total_sales = sum(sales)
    print(f"\n\t\tTotal sales amount for all months: ₹{total_sales:.2f}\n")

    # Additional feature: Display the highest and lowest sales months
    if months:
        max_sales_month = months[sales.index(max(sales))]
        min_sales_month = months[sales.index(min(sales))]
        print(f"\t\tHighest sales month: {max_sales_month} (₹{max(sales):.2f})\n")
        print(f"\t\tLowest sales month: {min_sales_month} (₹{min(sales):.2f})\n")
        
main()
