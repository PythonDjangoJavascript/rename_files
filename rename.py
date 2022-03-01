import os
import shutil
from openpyxl import load_workbook
from pathlib import Path

"""automate file renaming. just add the file extension as file extension var
create new folder named ->'for_rename' and put this module to the dir whre
all file is available ath needs to rename
also don't forget to add all data in two row inside 'rename_files.xlsx' file
firs column is the original files name and second column is new name"""

file_extension = ".jpg"

wb = load_workbook('rename_files.xlsx')
ws = wb.active

vals = ws.values

to_dir = os.getcwd() + "/for_rename/"

rename_data = {}
for val in vals:
    if val[0] is not None and val[1] is not None:
        rename_data[str(val[0]).strip() + file_extension] = to_dir +  str(val[1]).strip() + file_extension
        
# print(rename_data)
        

print(to_dir)
a = 0
for x in os.listdir():
    if x.endswith(file_extension):
        # Prints only text file present in My Folder
        if rename_data.get(x) is not None:
            # shutil.copy(x, to_dir)
            shutil.move(x, rename_data.get(x), copy_function=shutil.copy2)
            a += 1
        else:
            print(x)
            
print(f'total {a}')