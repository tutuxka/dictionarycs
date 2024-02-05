import os

# 定义转换函数
def convert_file(input_file, output_file):
    # 打开输入文件，读取其中的词汇
    with open(input_file, 'r', encoding='utf-8') as file:
        words = file.readlines()

    # 处理每个词汇，转换为第一个词库的格式
    converted_words = []
    for word in words:
        word = word.strip()  # 去除词汇两端的空白字符
        converted_word = f"{word}\t{word}\ten"  # 转换为第一个词库的格式
        converted_words.append(converted_word)

    # 将转换后的词汇写入输出文件
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(converted_words))

# 定义输入文件夹路径和输出文件夹路径
input_folder = 'work/'
output_folder = 'cs/'

# 遍历文件夹中的所有文件
for file_name in os.listdir(input_folder):
    if file_name.endswith('.txt'):  # 只处理txt文件
        input_file = os.path.join(input_folder, file_name)
        output_file = os.path.join(output_folder, file_name)
        convert_file(input_file, output_file)
      
