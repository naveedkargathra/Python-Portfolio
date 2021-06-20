import os

def rename_multiple_files():
    i = 0
    path = "C:\\Users\\navee\\Downloads\\Shan Photos\\"
    for filename in os.listdir(path):
        my_name = "Shaan_" + str(filename) + "jpg"
        my_source = path+filename
        my_name = path + my_name
        os.rename(my_source, my_name)
        i +=1

if __name__ == '__main__':
    rename_multiple_files()