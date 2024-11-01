import os
import glob
all_ui_files = glob.glob("*.ui")
for ui_file_name in all_ui_files:
	os.system(f"pyuic5 -x \"{ui_file_name}\" -o \"pyfiles/{ui_file_name[:-2]}py\"")
print("tamom")
