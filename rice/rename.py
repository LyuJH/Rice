import os

path = r"images"

for file in os.listdir(path):
    print(file)
    print(type(file))
    name = file[-7: -4]
    print(int(name))
    name = int(name)
    os.rename(os.path.join(path, file), os.path.join(path, str(name) + ".jpg"))
    print(file, "修改完成")
