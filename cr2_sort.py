import os
import glob
import shutil


if not os.path.exists(r"/Volumes/EOS_DIGITAL/DCIM/100CANON/CR2/"):
    os.mkdir(r"/Volumes/EOS_DIGITAL/DCIM/100CANON/CR2/")

print("\nStarting the program...\n")

files_to_copy = glob.glob('/Volumes/EOS_DIGITAL/DCIM/100CANON/*.CR2')
destination_path = (r'/Volumes/EOS_DIGITAL/DCIM/100CANON/CR2')
bin_path = (r'/Users/maxim/.Trash')

amount = len(files_to_copy)
print(amount, "files are found:")
if amount > 0:
    c = 0
    for file in files_to_copy:
        c += 1
        shutil.copy2(file, destination_path)
        print(file, "is moved. ", f"({c})")

    print("\n Copying files to CR2 is completed.\n")

    c = 0
    for file in files_to_copy:
        c += 1
        shutil.move(file, bin_path)
        print(file, "is moved to bin. ", f"({c})")

print("\nThe program is completed.")