import os
import re
import xarray as xr

# 指定数据文件夹路径

# 指定数据文件夹路径
data_folder = 'D:\wget\GPMfinal07big'

# 遍历文件夹中的所有文件
for filename in os.listdir(data_folder):
    # 使用正则表达式匹配日期信息
    match = re.search(r'\d{8}-S\d{6}-E\d{6}', filename)
    if match:
        # 提取匹配的日期信息

        date_info = match.group(0)

        # 构建新的文件名
        new_filename = f"precipitation_{date_info}.nc4"

        # 重命名文件
        os.rename(os.path.join(data_folder, filename), os.path.join(data_folder, new_filename))
        print(f"Renamed {filename} to {new_filename}")
    else:
        print(f"No date information found in {filename}")