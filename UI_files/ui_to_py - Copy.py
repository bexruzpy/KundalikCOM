import os
import glob
all_ui_files = glob.glob("*.ui")
for ui_file_name in all_ui_files:
	os.system(f"pyuic5 -x \"{ui_file_name}\" -o \"../Desktop/ui_pyfiles/{ui_file_name[:-2]}py\"")
print("""########     ####    #      #   ######   #      #  
   #        #    #   ##    ##  #      #  ##    ##  
   #       ########  #  ##  #  #      #  #  ##  #  
   #       #      #  #      #  #      #  #      #  
   #       #      #  #      #   ######   #      #

""")
def keyingi(matn):
   for i in matn:
      ord(i)
   return matn
# matn1 = "f72aa084535a23445ac38a885954336e"
# matn2 = "2295c732e47f4f31b7eb1f2a884cd4a7"
# a = True
# while a:
#    a = False
#    for i in matn1:
#       if matn1.cout(i) != matn2.cout(i):
#          matn1 = keyingi(matn1)
#          print(matn1)
#          a = True
#          break
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# print(matn1)
# print(matn2)
#    