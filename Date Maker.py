from os import walk
import os, time
import shutil
import tkinter as tk
from tkinter import filedialog

direction = input("Select Location: ")

# root = tk.Tk()
# root.withdraw()
# direction = filedialog.askdirectory(title = "Select a Directory")
# if (not direction):
#     print("No Direction Selected.")
# else:
#     os.chdir(direction)

files = []
for (dirpath, dirnames, filenames) in walk(direction):
    files.extend(filenames)
    break

file_year = []
file_date = []

for file in files:
	file_date_temp = time.ctime(os.path.getmtime(file))
	file_year.append(file_date_temp.split()[-1])
	file_date.append(file_date_temp.split()[-1])

file_year = list(dict.fromkeys(file_year))

for year in file_year:
	try:
		os.mkdir(year)
	except:
		pass

years = {}

for i in range(len(file_year)):
	years[i] = file_year[i]

# print(file_date)

for i in range(len(files)):
	if file_date[i] in years.values():
		shutil.move(files[i], file_date[i])