import numpy as np
from scipy.stats import norm

# Dữ liệu từ bảng phân phối xác xuất\
#Dữ liệu đề cho 
#X(Nhiệt độ) 20-22 22-24 24-26 26-28 28-30
#Số tháng 20 15 25 36 29
#X(Nhiệt độ) 21 23 25 27 29
#Số tháng    20 15 25 36 29
#Độ tin cậy 95%
temperature_ranges = np.array([21, 23, 25, 27, 29])
months = np.array([20, 15, 25, 36, 29])

# a.) Ước lượng nhiệt độ trung bình
sample_mean = np.sum(temperature_ranges * months) / np.sum(months)
print("Nhiệt độ trung bình ước lượng:", sample_mean)

# b.) Khoảng tin cậy
#Độ lệch chuẩn (standard deviation) = căn bậc hai của phương sai (variance)

variance = np.sum(((temperature_ranges - sample_mean)**2) * months) / np.sum(months)
standard_deviation = np.sqrt(variance)
confidence_interval = norm.interval(0.95, loc=sample_mean, scale=standard_deviation / np.sqrt(np.sum(months)))

print("Khoảng tin cậy:", confidence_interval)
print("Nhiệt độ trung bình tối đa:", confidence_interval[1])
print("Nhiệt độ trung bình tối thiểu:", confidence_interval[0])
