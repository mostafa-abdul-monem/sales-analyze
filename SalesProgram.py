import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def read_csv():
    df = pd.read_csv(r"D:\DEBI\python\1st project dataset\random_sales_data.csv")
    return df
df = read_csv()

null_count = df["Price"].isnull().sum()

#Print a message with the total number of nulls
def handling_nulls (df):
    
    if null_count > 0:
        df["Price"] = df["Price"].fillna(df["Price"].mean())
        print("\n****CHEKING NULLS****\n",df.isnull().sum().to_string(),"\n****CHEKING END****\n")
        print(f"{null_count} missing values replaced with the mean.")
        #Print the number of nulls replaced with mean

    else:
        print("No missing values found in the 'Price' column.")
    return df

def summary_analyze(df):

    print('\n****YOUR SALES ANALYSIS****\n')
    print(f"\nTotal Orders : {df.shape[0]}")

    avgOrderValue = (df['Total Sales'].mean()).round(2)
    print(f'\nAverage Order Value: {avgOrderValue}')

    totalRevenue = ((df['Quantity'] * df['Price']).sum()).round(2)
    print(f"\nTotal Revenue : {totalRevenue}")

    avgPrice = (df['Price'].mean()).round(2)
    print(f"\nAverage Product price: {avgPrice}")

def category_analyze(df):

    orderPerCategory = df.groupby('Category')['Order ID'].count()
    print("\nNumber of Orders Per Category:\n",orderPerCategory.to_string())
    #VISUALIZATION
    orderPerCategory.plot(kind='bar', color='skyblue')
    plt.title('Orders per Category')
    plt.xlabel('Category')
    plt.ylabel('Number of Orders')
    plt.tight_layout()
    plt.show()

    totalCatSales= df.groupby('Category')['Total Sales'].sum()
    print("\nTotal Sales Per Category:\n",totalCatSales.to_string())
    #VISUALIZATION
    totalCatSales.plot(kind='pie', autopct='%1.1f%%', title='Total Sales by Category')
    plt.title('Category Sales')
    plt.tight_layout()
    plt.show()

def sales_analyze(df):

    threshold = df['Total Sales'].mean()
    df['Sales Category'] = df['Total Sales'].apply(lambda x:'High' if x >= threshold else 'Low')
    salesCatPrecentage = ((df['Sales Category'].value_counts() / len(df)) * 100).round(2)
    print('\nThe Precentage of Sales Categories:\n',salesCatPrecentage.to_string())
    #VISUALIZATION
    sns.countplot(x='Sales Category', data=df)
    plt.title('Sales Category Distribution')
    plt.show

def product_analyze(df):

    totalProductSales = df.groupby('Product')['Total Sales'].sum()
    print("\nTotal Products Sales:\n", totalProductSales.to_string())
    #VISUALIZATION
    totalProductSales.sort_values(ascending=False).plot(kind='bar',title='Product Sales')
    plt.xlabel('Total Sales')
    plt.ylabel('Product')
    plt.tight_layout()
    plt.show()

handling_nulls(df)
summary_analyze(df)
category_analyze(df)
sales_analyze(df)
product_analyze(df)