def calculate_continuous_sums(data):
    results = []
    for x in range(2, len(data) + 1):
        max_sum = max(sum(data[i:i + x]) for i in range(len(data) - x + 1))
        results.append((x, max_sum))
    return results

# 读取txt文件中的数据并保留两位小数
file_path = 'D:\data\count/count.txt'  # 替换为你的文件路径
output_file = 'D:\data\count/output_results.txt'  # 输出文件路径

with open(file_path, 'r') as file:
    data = [float("{:.2f}".format(float(line.strip()))) for line in file]

# 计算连续的2到48个数字的和的最大值
results = calculate_continuous_sums(data[:37])

# 输出结果到txt文件
with open(output_file, 'w') as output:
    for x, max_sum in results:
        output.write(f'{x}\t{max_sum}\n')

print(f"Results saved to {output_file}")