"""
本地测试的sample太多
这个脚本可以随机删除指定文件夹里面的内容
最后只剩下500张

直接终端输入 python src/random_delete.py

"""

import os
import random

def random_delete(folder_path):
    all_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # 如果文件数大于500，随机删除多余的文件
    cnt = 0
    if len(all_files) > 500:
        files_to_delete = random.sample(all_files, len(all_files) - 500)  # 随机选择要删除的文件
        for file in files_to_delete:
            file_path = os.path.join(folder_path, file)
            os.remove(file_path)
            cnt += 1
        print(f"Deleted {cnt} files")
    else:
        print("The folder already contains 500 or fewer files.")


current_path = os.path.dirname(os.path.abspath(__file__))
train_real_folder = current_path + "/../AIGC-Detection-Dataset/train/0_real"
train_fake_foledr = current_path + "/../AIGC-Detection-Dataset/train/1_fake"
random_delete(train_real_folder)
random_delete(train_fake_foledr)