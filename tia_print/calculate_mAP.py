# 输入三个数字，用逗号分隔
input_str = input("请输入三个数字，用逗号分隔: ")

# 将输入的字符串按逗号分割，并转换为浮点数
numbers = [float(num) for num in input_str.split(',')]

# 计算均值
mean = sum(numbers) / len(numbers)
mean_rounded = round(mean, 2)
# 输出均值
print("这三个数字的均值是:", mean_rounded)