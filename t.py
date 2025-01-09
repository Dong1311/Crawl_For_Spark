import pandas as pd

# Đọc dữ liệu từ file shopee_product_id.csv
input_file = "shopee_product_id.csv"
output_file = "text.csv"

# Đọc từ dòng 100 đến dòng 500 (index bắt đầu từ 0, dòng 100 là index 99)
df = pd.read_csv(input_file, skiprows=2500, nrows=500)

# Lưu vào file text.csv
df.to_csv(output_file, index=False)

output_file
