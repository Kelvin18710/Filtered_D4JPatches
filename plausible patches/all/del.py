import os
import shutil

def move_files_with_substring(src_folder, substring="Time", dest_folder_name="../problematic/Time/patchINFO"):
    # 目标文件夹路径（在源文件夹下）
    dest_folder = os.path.join(src_folder, dest_folder_name)
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
        print(f"创建目标文件夹: {dest_folder}")

    # 遍历源文件夹中的所有文件
    for file_name in os.listdir(src_folder):
        file_path = os.path.join(src_folder, file_name)
        # 如果是文件且文件名包含指定字符串
        if os.path.isfile(file_path) and substring in file_name:
            dest_path = os.path.join(dest_folder, file_name)
            try:
                shutil.move(file_path, dest_path)
                print(f"已移动文件: {file_path} -> {dest_path}")
            except Exception as e:
                print(f"移动文件 {file_path} 时出错: {e}")

if __name__ == "__main__":
    # 请修改下面的路径为你实际要处理的文件夹路径
    folder_path = "patchINFO"  # 例如 "C:/data/files"
    move_files_with_substring(folder_path)

