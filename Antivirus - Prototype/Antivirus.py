from code import InteractiveInterpreter
from fileinput import filename
import hashlib
from logging import root
import os
from os import listdir
from os.path import isfile, join
from functools import partial
import json
import socket
from tabnanny import check
import threading
from tkinter import font
from turtle import bgcolor, left
from typing import List
from numpy import pad
import urllib3
from tkinter import *
from tkinter import filedialog
from multiprocessing.dummy import Pool as ThreadPool


malware_found_file_list = []
virusCount = 0
fileCount = 0
virus_found = False

# Color variables
buttonColor = "#2D5731"
backgroundColor = "#033B3D"
backgroundColorLight = "#044a4d"
foregroundColor = "#ffffff"
warningColor = "#ff2b2b"
successColor = "#48e33d"




# Utility Methods
def calculateMD5(fileLocation):

    global md5_value

    with open(fileLocation, 'rb') as file_to_check:
        fileContent = file_to_check.read()    
        md5_value = hashlib.md5(fileContent).hexdigest()
        return md5_value

def calculateSHA1(fileLocation):

    global SHA1_value

    with open(fileLocation, 'rb') as file_to_check:
        fileContent = file_to_check.read()    
        sha1_value = hashlib.sha1(fileContent).hexdigest()
        return sha1_value

def calculateSHA256(fileLocation):

    global SHA256_value

    with open(fileLocation, 'rb') as file_to_check:
        fileContent = file_to_check.read()    
        sha256_value = hashlib.sha256(fileContent).hexdigest()
        return sha256_value

def checkMD5Signature(md5_value):
      virus_found = False

      with open("signatures/MD5 Virus Hashes.txt",'r') as f:
            lines = [line.rstrip() for line in f]
            for line in lines:
                  if str(md5_value.upper()) == str(line.split(";")[0].upper()):
                        virus_found = True
            f.close()

      if(virus_found): 
            return True

def checkSHA1Signature(sha1_value):
      virus_found = False
      
      with open('signatures/SHA1 HASHES.json', 'r') as f:
            dataset = json.loads(f.read())

            for index, item in enumerate(dataset["data"]):
                  if str(item['hash']) == str(sha1_value):
                        virus_found = True
            f.close()

      if(virus_found): 
            return True

def checkSHA256Signature(sha256_value):
      virus_found = False
      
      with open("signatures/SHA256.txt",'r') as f:
                lines = [line.rstrip() for line in f]
                for line in lines:
                      if str(sha256_value) == str(line.split(";")[0]):
                        virus_found = True
                f.close()

      if(virus_found): 
            return True 

def checkInternetConnectivity(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True

    except socket.error as ex:
        print(ex)
        return False

def online_scan(file):
      virus_found = False

      with open(file,"rb") as f:
            bytes = f.read()
            readable_hash = hashlib.md5(bytes).hexdigest()

def offline_scan(file):
      global malware_found_file_list

      md5_value = calculateMD5(file)
      sha1_value = calculateSHA1(file)
      sha256_value = calculateSHA256(file)

      if(checkMD5Signature(md5_value) or checkSHA1Signature(sha1_value) or checkSHA256Signature(sha256_value)):
            print("Virus detected! File quarantined")
            label_status.configure(text="Status: Virus detected! File Deleted!", width = 50, height = 4,  
                            fg = warningColor)
            #os.remove(file)       
      else:
            print("File is safe!")
            label_status.configure(text="Status: File is safe!", width = 50, height = 4,  
                            fg = successColor)

def bulk_offline_scan(file):
      global malware_found_file_list
      global virusCount
      global virus_found

      virus_found = False

      md5_value = calculateMD5(file)
      sha1_value = calculateSHA1(file)
      sha256_value = calculateSHA256(file)

      if(checkMD5Signature(md5_value) or checkSHA1Signature(sha1_value) or checkSHA256Signature(sha256_value)):
            virusCount = virusCount + 1
            virus_found = True
            malware_found_file_list.append(file)     
      #os.remove(file)       

def virusDatabase():
      a=1
      # virus_found = True
      # # malware_found_file_list.append()
      # virusCount = virusCount + 1

def scanAllFiles():
      global virusCount
      global fileCount
      global scanning_text_label
      global window

      label_status.configure(text="Status: ", width = 50, height = 4, fg = foregroundColor)
      opened_file.configure(text="File Opened: ", width = 50, height = 4, fg = foregroundColor)


      directoryName = filedialog.askdirectory(title='Select Folder') 

      for dirpath,_,filenames in os.walk(directoryName):
            for f in filenames:
                  fileCount = fileCount + 1
                  currentFile = os.path.abspath(os.path.join(dirpath, f))
                  bulk_offline_scan(currentFile)
                  scanning_text_label['text'] = "File Scanned: "+ str(fileCount)
                  window.update()

      if(virusCount>0):
            # for x in range(len(malware_found_file_list)):
            #       print(*malware_found_file_list, sep = "\n")    
            
            label_status.configure(text="Status: Malware Found", width = 50, height = 4, fg = warningColor)

      else:
            label_status.configure(text="Status: Malware not detected", width = 50, height = 4, fg = successColor)
      
      fileCount = 0
  
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.*"), ("all files", "*.*"))) 
    opened_file.configure(text="File Opened: "+filename)


    scanning_text_label.config(text="File Scanned: 1")
    offline_scan(filename)

#     if(checkInternetConnectivity()):
#           online_scan(filename)
#     else:
#           offline_scan(filename)

       
                                                                                                   
window = Tk() 
window.title('Antivirus') 
window.geometry("700x500")
# window.resizable(False, False)
window.config(background = backgroundColor)

# set the font with bold text
f = font.Font(weight="bold")
     
label_file_explorer = Label(window,  text = "Antivirus", width = 100, height = 4,  fg = "white", bg=backgroundColor)
label_file_explorer.config(font=("Calibri", 20))
       
button_browse = Button(window,  text = "Scan a File", command = browseFiles)
button_scan_all = Button(window,  text = "Scan a Directory", command = scanAllFiles)
   
label_file_explorer.grid(column = 1, row = 1)
label_file_explorer.place(x=-350, y=0)
# label_file_explorer['font'] = font.Font(weight="bold")

scanning_text_label = Label(window,  text = "File Scanned: ", width = 50, height = 4,  fg = "white" ,bg = backgroundColorLight, wraplength=200, justify="left")
scanning_text_label.config(font=("Calibri", 12))
scanning_text_label.grid(column = 1, row = 1)
scanning_text_label.place(x=150, y=150)

opened_file = Label(window,  text = "File Opened: ", width=50, height = 4,  fg = "white" , bg = backgroundColorLight,  wraplength=200, justify="left")
opened_file.config(font=("Calibri", 12))
opened_file.grid(column = 1, row = 1)
opened_file.place(x= 150, y=250)

label_status = Label(window,  text = "Status: ", width=50, height = 4, fg = "white" ,bg = backgroundColorLight, justify="center")
label_status.config(font=("Calibri", 12))
label_status.grid(column = 1, row = 1)
label_status.place(x= 150, y=300)
   
button_browse.grid(column = 1, row = 2)
button_browse.place(x=205, y=400)
button_browse.config(pady=10, padx=20, bd=0, bg=buttonColor, fg=foregroundColor)
button_browse['font'] = f

button_scan_all.grid(column = 1, row = 2)
button_scan_all.place(x=350, y=400)
button_scan_all.config(pady=10, padx=20, bd=0, bg=buttonColor, fg=foregroundColor)
button_scan_all['font'] = f

window.mainloop() 



