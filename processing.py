import re
import subprocess
import os
cwd = os.getcwd()
path = cwd+'\dataset'
train_path=path+'\\trainResumes'
test_path=path+'\\testResumes'
def pdflist(path):
    dir_list = os.listdir(train_path)
    # prints all files
    return dir_list

os.listdir(cwd)
def extract_resume(path):
    import shutil
    shutil.copy2(path+'\\Job description.pdf',path+'\\req.pdf')
    i='req.pdf'
    tmp=path+"\\tmp.cmd"
    f = open(tmp, "w")
    f.write("pdftotext "+i)   ## Writing to Batch file the command to call XPDF
    f.close()
    subprocess.call('subprocess3.cmd',shell=True)
    
def extract_train(path):
    l1=cwd+'\\pdftotext.exe'
    l2=path+'\\pdftotext.exe'
    import shutil
    shutil.copyfile( l1 ,l2)
    pdf=[]
    text=[]
    for i in os.listdir(path):
        if(re.search('\.pdf$',i)):
            print(i)
            tmp=path+"\\tmp.bat"
            f = open(tmp, "w")
            f.write("pdftotext "+i)
            f.close()
            subprocess.call('subprocess1.cmd',shell=True)
    for i in os.listdir(path):
        if(re.search('\.txt$',i)):
            try:
                os.rename(path+'\\'+i,cwd+'\\train_txt\\'+i)
            except:
                pass
def extract_test(path):
    l1=cwd+'\\pdftotext.exe'  ## Calling XPDF to extract text from PDF
    l2=path+'\\pdftotext.exe'
    import shutil
    shutil.copyfile( l1 ,l2)
    pdf=[]
    text=[]
    for i in os.listdir(path):
        if(re.search('\.pdf$',i)):
            print(i)
            tmp=path+"\\tmp.bat"
            f = open(tmp, "w")
            f.write("pdftotext "+i)
            f.close()
            subprocess.call('subprocess2.cmd',shell=True)
    for i in os.listdir(path):
        if(re.search('\.txt$',i)):
            try:
                os.rename(path+'\\'+i,cwd+'\\test_txt\\'+i)
            except:
                os.remove(cwd+'\\test_txt\\'+i)
                os.rename(path+'\\'+i,cwd+'\\test_txt\\'+i)
                pass
extract_resume(path)
extract_train(train_path)
extract_test(test_path)
