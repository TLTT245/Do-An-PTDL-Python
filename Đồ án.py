import pandas as pd
import xlrd
import xlwt
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm


# Đọc dữ liệu từ file excel 
df = pd.read_excel(r'D:\Dataset-Temperature-by-years.xls')
# #in ra các cột dữ liệu
# print(df.head(10))
# print(df.Season)
# print(df.Year)
# print(df.Salinity)
# #Bài toán ước lượng 
# #1.Số lượng quan sát (sample size)
# print(len(df))
#2.Giá trị trung bình (mean)
# Xài Hàm GroupBy để tính theo tùy thuộc
grouped = df.groupby('Year').agg({'Temperature':max, 'Salinity':max})
print(grouped)
print('=========================')
grouped1 = df.groupby('Month').agg({'Salinity':min})
print(grouped1)
grouped2 = df.groupby('Season').agg({'Temperature':max})
print(grouped2)
grouped3 = df.groupby('Year').agg({'Temperature':min,'Salinity':min,'CHLFa':min})
print(grouped3)
# print("Trung bình of Salinity:", mean_salinity)
# print("Trung bình of Temperature:", mean_temperature)
# print("Trung bình  of CHLFa:", mean_chlfa)
# #3.Phương sai(Variance)
# variance_salinity = df['Salinity'].var()
# variance_temperature = df['Temperature'].var()
# variance_chlfa = df['CHLFa'].var()
# print("Phương sai của Độ ẩm:", variance_salinity)
# print("Phương sai của nhiệt độ là:", variance_temperature)
# print("Phương sai của là CHLFa:", variance_chlfa)
# #4.Độ lệch chuẩn
# std_dev_salinity = df['Salinity'].std()
# std_dev_temperature = df['Temperature'].std()
# std_dev_chlfa = df['CHLFa'].std()

# print("Độ lệch chuẩn của độ ẩm:", std_dev_salinity)
# print("Độ lệch chuẩn của nhiệt độ:", std_dev_temperature)
# print("Độ lệch chuẩn của nhiệt độ :", std_dev_chlfa)
# #5 Phân bố tần suất (frequency distribution)
# # Tính phân bố tần xuất cho các cột dữ liệu
# frequency_salinity = df['Salinity'].value_counts(normalize=True)
# frequency_temperature = df['Temperature'].value_counts(normalize=True)
# frequency_chlfa = df['CHLFa'].value_counts(normalize=True)

# print("Phân bố tần xuất của độ ẩm:")
# print(frequency_salinity)
# print("\nPHân bố tần xuất của nhiệt độ là:")
# print(frequency_temperature)
# print("\nPhân bố tần xuất của CHFLA là:")
# print(frequency_chlfa)
# #6. Giá trị tối đa tối thiểu 
# min_salinity = df['Salinity'].min()
# min_temperature = df['Temperature'].min()
# min_chlfa = df['CHLFa'].min()
# max_salinity = df['Salinity'].max()
# max_temperature = df['Temperature'].max()
# max_chlfa = df['CHLFa'].max()

# print("Giá trị nhỏ nhất của Salinity:", min_salinity)
# print("Giá trị lớn nhất của Temperature:", max_temperature)
# print("Giá trị nhỏ nhất  của CHLFa:", min_chlfa)
# Kiểm định t-test:
# Đọc data set từ file Excel
# Chọn cột dữ liệu cần kiểm định
# group1 = df[df['Season'] == 'spring']['Salinity']
# group2 = df[df['Season'] == 'summer']['Salinity']
# print(group1)
# print(group2)



