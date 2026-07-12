#----used Modules----
import re
import os
import time
from datetime import datetime

red="\033[91m"
green="\033[92m"
yellow="\033[93m"
blue="\033[94m"
purple="\033[95m"
reset="\033[0m"


while True:
    for i in range(20):
       print("=", end="", flush=True)
       time.sleep(0.02) 
    print()
    
    letters="Soc log analyser".center(20).upper()
    
    for letter in letters:
        print(letter, end="", flush=True)
        time.sleep(0.02)
    print()
    
    for i in range(20):
        print("=", end="", flush=True)
        time.sleep(0.02)
    print()
    
    
    print(yellow + "[$] Initializing" + reset, end="", flush=True)
    
    for i in range(10):
        print(yellow + "." + reset, end="", flush=True)
        time.sleep(0.30)
    print()
    
    print(yellow + "[$] Loading Modules" + reset, end="", flush=True)
    
    for i in range(10):
        print(yellow + "." + reset, end="", flush=True)
        time.sleep(0.30)
    print()
    
    print(yellow + "[$] Preparing Scanner" + reset, end="", flush=True)
    
    for i in range(10):
        print(yellow + "." + reset,end="",flush=True)
        time.sleep(0.30)
    print()
    
    print(green + "> Ready!" + reset)

    current_folder=os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_folder)

    #-----------MAIN PROGRAM-------------

    filename=input("\nEnter the log file name (with extension...):-") 
    
    print(yellow + "[#] Opening Log File" + reset, end="", flush=True)
    
    for i in range(10):
        print(yellow + "." + reset, end="", flush=True)
        time.sleep(0.30)
    print()
    
    print(yellow + "[#] Reading File" + reset, end="", flush=True)
    
    for i in range(15):
        print(yellow + "." + reset, end="" , flush=True)    
        time.sleep(0.30)    
    print()

    print(purple + "[#] Analyzing" + reset, end="", flush=True)    
    
    for i in range(10):
        print(purple + "." + reset, end="", flush=True)
        time.sleep(0.30)
    print()
    
    try:
     file=open(filename,"r")
     log=file.read()
     file.close()
     print(green + "[/]File Loaded Successfully!" + reset)
    except FileNotFoundError:
     print(red + "[?] File not exist/Found!" + reset)
     continue
     
    emails=re.findall(r"\S+@\S+",log)
    ips=re.findall(r"\d+\.\d+\.\d+\.\d+",log)
     
    leng1=len(log)
    leng2=len(log.split())
    leng3=len(log.splitlines())

    
    text1=log.count("INFO")
    text2=log.count("ERROR")
    text3=log.count("WARNING")
    
    leng5=len(emails)
    leng6=len(ips)
    size=os.path.getsize(filename)
    
    current=datetime.now()
    
    for i in range(30):
        print("=", end="", flush=True)
        time.sleep(0.02)
    print()
    
    letters_2="File statistics".center(30).upper()
    
    for l in letters_2:
        print(l, end="", flush=True)
        time.sleep(0.02)
    print()
    
    for i in range(30):
        print("=", end="", flush=True)
        time.sleep(0.02)
    print()
    
    report = (f"""\n
File Name : {filename} \n
File Size : {size} Bytes \n
Total Lines   : {leng3} \n
Total Words   : {leng2}  \n
Total Characters : {leng1} \n
           
INFO Entries : {text1} \n
Warning Entries : {text3} \n
Error Entries : {text2} \n
        
Emails Found :  {leng5}    \n
IP Addresses : {leng6}     \n
           
Scan Date   :  {current.strftime("%d-%m-%Y")} \n
Scan Time   :  {current.strftime("%H:%M:%S")} \n
           
            """)
    print(report)
    
    for i in range(40):
        print("=", end="", flush=True)
        time.sleep(0.02)
    print() 
    
    choice=str(input(blue + "[#] Do you want to save the report (Y/N)? :" + reset)).lower()
    
    if choice == "y":
          file1=str(input("Enter the name of file: "))
    else:
       exit=['|','/','-','\\']
       for i in range(20):
           print("\rExiting",exit[i%len(exit)],end="",flush=True)
           time.sleep(0.1)
       break

    if not file1.endswith(".txt"):
        file1+=".txt"
    
    loc=os.path.abspath(file1)
    
    file2=open(file1,"w")
    file2.write(report)
    file2.close()
    
    print(green + "[#] Report Saved Successfully !" + reset)
    print("Location : \n",loc)
    
    letters_3="Thank you for using \nSOC log analyzer".upper()
    
    for l in letters_3:
        print(green + l + reset,end="",flush=True)
        time.sleep(0.10)
        
    print(purple + "\nExiting" + reset,end="",flush=True)
    for i in range(10):
        print(purple + "." + reset,end="",flush=True)
        time.sleep(0.10)
    break
