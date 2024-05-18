import os
os.chdir('D:/Python')
         
for f in os.listdir():
    f_name,f_ext=(os.path.splitext(f))
    f_course,f_title,f_num=(f_name.split('-'))
    f_num=f_num[1:]
    new_file=("{}-{}-{}{}".format(f_num,f_title,f_course,f_ext))
    
os.rename(f,new_file)