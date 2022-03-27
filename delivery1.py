import pandas as pd 
import plotly.express as px

#read the files into pandas dataframes
df_customers = pd.read_excel("/Users/oliverkaminski/Desktop/my_shop_data.xlsx", sheet_name = "customers")
df_order = pd.read_excel("/Users/oliverkaminski/Desktop/my_shop_data.xlsx", sheet_name = "order")
df_employee = pd.read_excel("/Users/oliverkaminski/Desktop/my_shop_data.xlsx", sheet_name = "employee")
df_products = pd.read_excel("/Users/oliverkaminski/Desktop/my_shop_data.xlsx", sheet_name = "products")

#join the first and last name into an emp_name column (to later on merge)
df_employee['emp_name'] = df_employee['firstname'] + ' ' + df_employee['lastname']

#merging the employee name onto the order dataframe
df_order_emp = pd.merge(df_order,df_employee[['employee_id','emp_name']],on='employee_id', how='right')

#merging the product name onto the order dataframe
#some orders have product name 0, since we don't have that ID in our product table, we omit those
df_order_product = pd.merge(df_order,df_products[['product_id','productname']],on='product_id', how='right')

def sales_by_employee():
    # x axis - employee names (index of the value counts)
    # y axis - the amonut of sales (per employee)
    fig = px.bar(x=list(df_order_emp['emp_name'].value_counts().index),
            y= list(df_order_emp['emp_name'].value_counts().values),
            title='Sales by Employee', labels={
                        "x": "Employee name",
                        "y": "No. of orders",
                    }, orientation="v")
    fig.show()

def sales_by_product():
    # x axis - product names
    # y axis - the amount of sales (per product)
    fig = px.bar(x=list(df_order_product['productname'].value_counts().index),
            y=list(df_order_product['productname'].value_counts().values), 
            title='Sales by Product', labels={
                        "x": "Product",
                        "y": "No. of sales",
                    }, orientation="v")
    fig.show()


sales_by_product()
sales_by_employee()
