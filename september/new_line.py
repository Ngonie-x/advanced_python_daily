


def strip_file(file_name):
    flist = open(file_name, 'r').readlines()
    
    new_file = open('new_file.py', 'a')
    
    for line in flist:
        new_file.write(line.strip())
        
    new_file.close()
