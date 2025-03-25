import os

# 设置目标文件夹路径
folder_path = 'patch' 
output_file = 'plausible_patch_list.txt'         # 输出的txt文件名

# 获取文件夹下的所有文件（不包括子文件夹内的）
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# 写入到txt文件中
with open(output_file, 'w', encoding='utf-8') as f:
    for file_name in files:
        f.write(file_name + '\n')

print("文件名已写入", output_file)

