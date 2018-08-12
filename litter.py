import os
def get_dirlist(path):
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist  
        
loc=r"C:\Users\JXYTi\Desktop\Test"
       
def litter(root):
    os.chdir(root) 
    trash=open("trash.txt", "w")
    trash.write("nahyuta best prosecutor, chitoge best girl")
    trash.close()
    d=get_dirlist(root)
    for f in d:
        f=root+"\\"+f
        if os.path.isdir(f):
            litter(f)

litter(loc)