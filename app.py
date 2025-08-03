import os
import csv

data_dir = "./data"
output_file = "./formated_data.csv"

with open(output_file, "w") as output_file:
    writer = csv.writer(output_file)

    header = ['sales', 'date', 'region']
    writer.writerow(header)

    for filename in os.listdir(data_dir):
        with open(f"{data_dir}/{filename}", "r") as input_file:
            reader = csv.DictReader(input_file)

            row_index = 0
            for input_row in reader:
                if row_index > 0:
                    product = input_row['product']
                    raw_price = input_row['price']
                    quantity = input_row['quantity']
                    transaction_date = input_row['date']
                    region = input_row['region']

                    if product == 'pink morsel':
                        price = float(raw_price[1:])                    
                        sale = price * int(quantity)

                        output_row = [sale, transaction_date, region]
                        writer.writerow(output_row)
                row_index += 1