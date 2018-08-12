import os
def get_dirlist(path):
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist  
        
loc=r"C:\Users\JXYTi\Desktop\Test"

def cleanup(root, target):
    d=get_dirlist(root)
    for f in d:
        if f==target:
            f=root+"\\"+f
            os.remove(f)
        else:
            f=root+"\\"+f
        if os.path.isdir(f):
            cleanup(f, target)        

cleanup(loc, "trash.txt")