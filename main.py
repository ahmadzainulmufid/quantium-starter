import pandas as pd
import glob

#data preprocessing & menggabungkan semua file CSV
all_files = glob.glob("data/*.csv")
df_list = [pd.read_csv(file) for file in all_files]
df = pd.concat(df_list, ignore_index=True)

df['product'] = df['product'].str.lower().str.strip()
df['price'] = df['price'].str.replace('$', '').astype(float)
df['quantity'] = df['quantity'].astype(int)

#filtering data untuk produk 'Pink Morsel'
df = df[df['product'] == 'pink morsel']

#menghitung total penjualan
df['sales'] = df['quantity'] * df['price']

#mengambil kolom yang diperlukan
final_df = df[['sales', 'date', 'region']]
final_df = final_df.rename(columns={'date': 'date', 'region': 'region'})

#menyimpan hasil akhir ke file CSV
final_df.to_csv("formated_output.csv", index=False)