import xarray as xr
import pandas as pd
import os
import matplotlib.pyplot as plt

# 指定数据文件夹路径
data_folder = 'D:\wget\GPMfinal07big'

# 获取所有 .nc4 文件
nc4_files = [filename for filename in os.listdir(data_folder) if filename.endswith('.nc4')]

# 给定的五个经纬度坐标
locations = {
    'top': (103.72, 31.7),
    'king': (103.75, 31.69),
    'middle': (103.78, 31.72),
    'ka': (103.78, 31.72),
    'mouth': (103.80, 31.65)
}

# 创建一个空的 xarray 数据集列表
datasets = []

# 遍历所有 .nc4 文件
for filename in nc4_files:
    file_path = os.path.join(data_folder, filename)

    # 使用 xarray 打开单个 .nc4 文件并添加到数据集列表中
    datasets.append(xr.open_dataset(file_path))

# 创建一个空的降水数据列表
precipitation_data = {}

# 提取特定经纬度的降水数据
for location, coordinates in locations.items():
    lon, lat = coordinates

    location_precipitation_data = []
    for dataset in datasets:
        # 假设降水数据的变量名为 'precipitation'
        # 如果不知道确切的变量名，请根据实际数据集中的变量名修改此处
        precipitation = dataset['precipitation'].sel(lon=lon, lat=lat, method='nearest')
        location_precipitation_data.append(precipitation)

    # 合并降水数据
    combined_location_data = xr.concat(location_precipitation_data, dim='time')
    precipitation_data[location] = combined_location_data

# 将数据合并到一个 DataFrame 中
dataframes = [data.to_dataframe(name=location) for location, data in precipitation_data.items()]
combined_dataframe = pd.concat(dataframes, axis=1)

# 保存合并后的数据到 CSV 文件
combined_dataframe.to_csv(os.path.join(data_folder, 'combined_precipitation_data0718-0725.csv'))

# Visualizing precipitation data over time for specified locations
for location, data in precipitation_data.items():
    data.plot(label=location)

plt.xlabel('Time')
plt.ylabel('Precipitation')
plt.title('Precipitation Variation Over Time at Specified Locations')
plt.legend(loc='upper left')
plt.show()
