import PyPDF2
import os 

def find_path(filename):
    for root, dirs, files in os.walk('C:\\', topdown=True):
        if filename in files:
            return os.path.join(root, filename)
    return None

filename_search = input("Enter the name of the PDF (example.pdf => format) : ")
file_path = find_path(filename_search)

new_file_pth = "modified_version_{}".format(filename_search)

def_p = '~/Desktop'
p_path = os.path.expanduser(def_p)
final_p = os.path.join(p_path,new_file_pth)


f = open(file_path,"rb")
read_obj =  PyPDF2.PdfReader(f)
write_obj = PyPDF2.PdfWriter()
writing = open(final_p,"wb")

num = int(input("Enter the number of pages you want to delete : "))
my_list =[]
for i in range(num):
    page_del= int(input("Enter the page numbers : "))
    my_list.append(page_del-1)


try:
    for j in range(len(read_obj.pages)):
        if j not in my_list:
            pagess = read_obj.pages[j]
            write_obj.add_page(pagess)
            write_obj.write(writing)

    print("Pages deleted successfully...!")
    print("Your new PDF is saved as {0} at {1}".format(new_file_pth,p_path))

except:
    print("Sorry something went wrong..!")
    
f.close()
writing.close()