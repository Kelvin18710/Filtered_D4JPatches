import os
from collections import Counter

# 设置目标文件夹路径
folder_path = 'patch' 
output_file = 'plausible_patch_type_count.txt'   # 输出统计结果的txt文件

# 初始化计数器
type_counter = Counter()

# 遍历文件夹
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        if '-' in file_name:
            prefix = file_name.split('-')[0]
            type_counter[prefix] += 1

# 写入结果到txt文件
with open(output_file, 'w', encoding='utf-8') as f:
    for prefix, count in sorted(type_counter.items()):
        f.write(f"{prefix}: {count}\n")

print("分类统计结果已写入", output_file)

