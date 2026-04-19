import os
import shutil

folder = "test_folder"

if not os.path.exists(folder):
    os.mkdir(folder)

for i in range(3):
    file_name = f"{folder}/file{i}.txt"
    with open(file_name, "w") as f:
        f.write("This is a test file")

clean_folder = "organized_folder"

if not os.path.exists(clean_folder):
    os.mkdir(clean_folder)

for file in os.listdir(folder):
    shutil.move(os.path.join(folder, file), clean_folder)
