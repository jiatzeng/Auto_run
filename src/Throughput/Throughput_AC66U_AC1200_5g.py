# -*- coding: utf8 -*-

'''
Created on 2010/1/11

@author: Jocabion
'''


import time
import re
import subprocess
import getpass
import sys
import telnetlib
import SendKeys
import socket
import random
import string   
import logging
import os,sys
import xlrd 
import fileinput
import datetime
import shutil, errno
import subprocess
import distutils.dir_util
import win32com.client
import win32gui 
import win32con
import win32api
import wmi 
import math
import _winreg
import ctypes
import selenium







#import tkMessageBox
#import tkSimpleDialog


# from VideoBridge import *
from threading import Thread

#from ddr_utility import *
from datetime import datetime
from ConfigParser import SafeConfigParser
from ConfigParser import RawConfigParser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver import Ie
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


#from turtle import goto
#from wx.lib.pubsub import Publisher
#from Tkinter import *
#from tkSimpleDialog import askstring
from win32gui import GetWindowText, GetForegroundWindow
from subprocess import Popen,PIPE




def copyanything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

def convertSize(size):
   size_name = ("Bytes","KB","MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size,1024)))
   p = math.pow(1024,i)
   s = round(size/p,2)
   if (s > 0):
       return '%s %s' % (s,size_name[i])
   else:
       return '0B'


    





if __name__ == '__main__':
    
    reload(sys)
#     sys.setdefaultencoding('utf8')
         
    conf = RawConfigParser()
    conf.read('config.ini')
    
       
    
    DUT_IP = conf.get ('ip','Dut_ip1')
    
    Account_password = conf.get ('Accountpassword','Account_password1')
    
    save_profile = os.getcwd() + '//Profile'
    
    save_result = os.getcwd() +'//Result//Throughput5g.txt'
    
    chrome_path = os.getcwd() + '//chromedriver_win32//chromedriver.exe'
    
    chariot_path = os.getcwd() + '/Chariot_tst'
    
     
    
    DST = 'http://' + Account_password + DUT_IP
    
    Basic2g_link = conf.get ('Basic_link','Basic2g')
    
    Basic5g_link = conf.get ('Basic_link','Basic5g')
    
    entry2g_link = conf.get ('Encryption_link','entry2g')
    
    entry5g_link = conf.get ('Encryption_link','entry5g')
    
    
    
    
    Basic2g = 'http://' + Account_password + DUT_IP + str(Basic2g_link)
    
    Basic5g = 'http://' + Account_password + DUT_IP + str(Basic5g_link)
    
    entry2g = 'http://' + Account_password + DUT_IP + str(entry2g_link)
    
    entry5g = 'http://' + Account_password + DUT_IP + str(entry5g_link)
    
    
    Channel_ID = conf.get ('Channel_ID','channel5g')
    
    
    Appy_ID_1 = conf.get ('Appy_ID','apply1_5g')

    Appy_ID_2 = conf.get ('Appy_ID','apply2_5g')
    
    
    ssid2g = conf.get ('Telnet','SSID1')
    
    ssid5g =  conf.get ('Telnet','SSID2')
    
    timesleep = conf.get ('5G_Time_sleep','sleep_time')
    
    channel2g_rangea = conf.get ('Channel','channel2g_rangea')

    channel2g_rangeb = conf.get ('Channel','channel2g_rangeb')

    channel5g_rangea = conf.get ('Channel','channel5g_rangea')

    channel5g_rangeb = conf.get ('Channel','channel5g_rangeb')
    
    Authentication2g = conf.get ('Encryption2g','Authentication')

    Encryption2g = conf.get ('Encryption2g','Encryption')

    KeyFormat2g = conf.get ('Encryption2g','Key Format')

    PresharedKey2g = conf.get ('Encryption2g','Pre-shared Key')
    
    Authentication5g = conf.get ('Encryption5g','Authentication')

    Encryption5g = conf.get ('Encryption5g','Encryption')

    KeyFormat5g = conf.get ('Encryption5g','Key Format')

    PresharedKey5g = conf.get ('Encryption5g','Pre-shared Key')
    
    model_name = conf.get('Model','name')
    
    model_fw = conf.get('Model','FW')
    
    channel_range = conf.get('Channel','channel5g')
    
    LAN_name = conf.get ('LAN','name')
    
    
    WLAN_name = conf.get ('WLAN','name')
    
    
    wifi_enable = 'http://' + Account_password + DUT_IP + '/index3.asp'
    
    
    DUT_IP = conf.get ('Telnet','Dut_ip')
        
    Account = conf.get ('Telnet','Account')
       
    Password = conf.get ('Telnet','password')
    
    Authentication2g = conf.get ('Telnet','Authentication')
    
    Encryption2g = conf.get ('Telnet','Encryption')
    
    Auth_mode2g = conf.get ('Telnet','Auth_mode')
    
    PresharedKey2g = conf.get ('Telnet','PresharedKey')
        
    Authentication5g = conf.get ('Telnet','Authentication')
    
    Encryption5g = conf.get ('Telnet','Encryption')
    
    Auth_mode5g = conf.get ('Telnet','Auth_mode')
    
    PresharedKey5g = conf.get ('Telnet','PresharedKey')  
    
    MAC = conf.get('Telnet','MAC')
    
    
    channel_5g_range = [0,36,40,44,48,149,153,157,161,165]
    
    for i , n in enumerate ([0,36,40,44,48,149,153,157,161,165]) :
         
        print i ,n
        if int(channel5g_rangea) == n :
           channel5g_rangea = i
    
        elif int(channel5g_rangeb) == n :
           channel5g_rangeb = i
       
    print channel5g_rangea
    print channel5g_rangeb
     
    
    print channel_range
    
    try :
            for filename in os.listdir(save_profile):
#                 print filename
#                 match_name = re.findall('\d[TR]{,1}[Xx]{,1}',filename) 
#                 print match_name
                os.chdir(save_profile)
                
                if filename.endswith(".xml") : 
                   
                   
                   print filename
                   
                   os.system('netsh wlan add profile filename='+filename)
                   
  
                   
    except :
        
            pass   
    
    
    
    
    if ',' in channel_range :
    
        channel_range_text = re.split(',',str(channel_range))
        
        print channel_range_text
        

        
    elif '~' in channel_range :
        
        channel_range_text = re.split('~',str(channel_range))
        
        print channel_range_text
        
        print range(int(channel_range_text[0]), int(channel_range_text[1])+1)
        
        channel_range_text = range(int(channel_range_text[0]), int(channel_range_text[1])+1)
        
        print channel_range_text
        
    else :
        
        channel_range_text = [channel_range] 
         
        print  channel_range_text
        

    
    
#     cmd3 = 'netsh wlan connect name='+str(ssid5g)+ ' ssid='+ str(ssid5g)
#     print cmd3
#     os.system(cmd3)
#     
#     time.sleep(10)
    
    try :
            for filename in os.listdir(chariot_path):
#                 print filename
#                 match_name = re.findall('\d[TR]{,1}[Xx]{,1}',filename) 
#                 print match_name
                if filename.endswith(".html") or filename.endswith(".gif") : 
                   print filename
                   os.remove(chariot_path+filename)
                   
    except :
        
            pass   
        
        
        
        
    
    
    file = open(save_result,'a') 
    
    file.write('Start time :      '+str(datetime.now())+"\n"+"\n")
       
    file.write(str(model_name)+'  '+ str(model_fw)+"\n"+"\n")
    
    file.write('Channel and Bandwidth Throughput'+"\n"+"\n")
             
    file.write('          5G AC 5M BW=80  Open'+"\n" +"\n"+"\n")
    
    channel5g_a = conf.get ('Channel','channel5g_rangea')

    channel5g_b = conf.get ('Channel','channel5g_rangeb')
    
         
    file.write('Channel'+' ' + str(channel5g_a) + ' ~ ' + str(channel5g_b)  +   '  Throughput Average Mbps'+"\n" +"\n")    
    
      
    
    list_Throughput = []
    
    
    print channel_range_text
    
    band_width = ['80']
    
    

    for u in band_width:    
        
        for j in channel_range_text:   
             
              
            file = open(save_result,'a')
             
            try :
                   tn = telnetlib.Telnet(str(DUT_IP),"23") 
                   time.sleep(3)                      
                   content = tn.read_very_eager()
                   print content
                   print("Auto login...")
                
                   if 'login' in content:
                          
                        print("Login to account...")
                        
                        tn.write(str(Account)+"\n")
                        time.sleep(1)
                        content = tn.read_very_eager()
                        
                        print content
                
                        print("Login to password...")
                        tn.write(str(Password)+"\n")
                        time.sleep(2)
                        content = tn.read_very_eager()
                        
                        print content
                        
                        time.sleep(2)
           
                   else :
                        
                        print 'Telnet connect fail !!!'
                        pass 
             
                   time.sleep(10)
                   tn.write('nvram set wl1_ssid='+str(ssid5g)+"\n")
                   time.sleep(2)   
#                    tn.write('nvram set wl_ssid='+str(ssid5g)+"\r\n")
#                    time.sleep(2)                  
                   tn.write('nvram set wl1_bw_cap=7'+"\n")
                   time.sleep(2)   
                   tn.write('nvram set wl1_chanspec='+str(j)+'/'+str(u)+"\n")
                   time.sleep(2) 
                   tn.write('nvram set wl1_contry_code=AR'+"\n")
                   time.sleep(2) 
                   tn.write('nvram set wl1_contry_rev=23'+"\n")
                   time.sleep(2) 
                   tn.write('nvram set wl1_akm='+ str(Authentication5g)+"\n")
                   time.sleep(2) 
                   tn.write('nvram set wl1_auth_mode_x='+ str(Authentication5g)+"\n")
                   time.sleep(2) 
                   tn.write('nvram set wl1_auth_mode='+ str(Auth_mode5g)+"\n")
                   time.sleep(2) 
                   tn.write('nvram set wl1_crypto='+ str(Encryption5g)+"\n")
                   time.sleep(2) 
                   tn.write('nvram set wl1_wpa_psk='+ str(PresharedKey5g)+"\n")
                   time.sleep(2)                     
                   tn.write('wlconf eth2 down'+"\n")
                   time.sleep(2)                   
                   tn.write('wlconf eth2 up'+"\n")
                   time.sleep(2) 
                   tn.write('wlconf eth2 start'+"\n")
                   time.sleep(2) 

                   tn.write('wl -i eth2 status'+"\n")
                   time.sleep(2) 
                   tn.write('nvram get wl1_chanspec'+"\n")
                   time.sleep(2) 
                   content = tn.read_very_eager()
                   print content
                   time.sleep(2) 
                   tn.write("exit\n") 
                   print 'Channel ' + str(j)
                   time.sleep(10) 

            except:
                 pass
             
      
                        
            time.sleep(int(timesleep))
             
            cmd3 = 'netsh wlan disconnect'
            print cmd3
            os.system(cmd3)  
             
            time.sleep(5)
             
             
                 
            cmd3 = 'netsh wlan connect name='+str(ssid5g)+ ' ssid='+ str(ssid5g)
            print cmd3
            pingPopen = subprocess.Popen(args=cmd3, shell=True, stdout=subprocess.PIPE)
            pingstring = pingPopen.stdout.read()
            print pingstring 
    
            time.sleep(10)
             
            if 'not' in pingstring : 
                 
                
                cmd3 = 'netsh interface set interface '+str(WLAN_name)+ ' disable'
                print cmd3
                os.system(cmd3)  
                
                time.sleep(3)
                
                cmd3 = 'netsh interface set interface '+str(WLAN_name)+ ' enable'
                print cmd3
                os.system(cmd3)  
                
                time.sleep(3)
                  
                 
                 
                 
                 
                cmd3 = 'netsh wlan connect name='+str(ssid5g)+ ' ssid='+ str(ssid5g)
                print cmd3
                os.system(cmd3)  
                time.sleep(int(timesleep))
                
            else :
                 
                 pass  
             
#             try :    
#                  tn = telnetlib.Telnet(str(DUT_IP),"23") 
#                  time.sleep(3)        
#                 
#         
#                  content = tn.read_very_eager()
#                  print content
#                  print("Auto login...")
#         
#                  if 'login' in content:
#                   
#                     print("Login to account...")
#                     
#                     tn.write(str(Account)+"\r\n")
#                     time.sleep(1)
#                     content = tn.read_very_eager()
#                     
#                     print content
#             
#                     print("Login to password...")
#                     tn.write(str(Password)+"\r\n")
#                     time.sleep(2)
#                     content = tn.read_very_eager()
#                     
#                     print content
#                     
#                     time.sleep(2)
#                 
#                
#         
#                  else :
#                 
#                     print 'Telnet connect fail !!!'
#                     pass      
#              
#             except :
#             
#               pass  
             
             
             
              
                
             
            for i in range(1 , 4 , 1):
            
             time.sleep(5) 
        
             test_script = conf.get ('Test_script','script'+str(i))
              
             print '===== 5G '+'Channel ' + str(j) + ' script ' + str(test_script) + ' ======='
           
             
             
  
    
             try :
              if 'root' in content :
                           

    
    #              if str(Authentication2g) in str(pingstring6) is True  :  
                 if 1 :
#                  if str(Authentication5g) == str(Authentication5g) :
                     
     
                 
                     print 'Start throughput test !!!'
                     
           
                     
                     
                     time.sleep(5)
                 

        
                     os.chdir(chariot_path)
                             
                              
                     print str(test_script)
                     print 'Please wait 1 min 30 secs ....'
                     cmd ='runtst -v '+ str(test_script)+'.tst' +' > ' + str(test_script)+'.csv'
                     print cmd
                     pingPopen = subprocess.Popen(args= str(cmd), shell=True, stdout=subprocess.PIPE)
                     pingstring = pingPopen.stdout.read()
                     print pingstring
                             
                             
                         
                     cmd2 = 'fmttst '+ '-h ' + str(test_script)+'.tst ' + '> ' + str(test_script) +'.html' 
                     print cmd2
                     p=Popen(cmd2,shell=True,stdin=PIPE)
                     p.stdin.write("y\n")
                     time.sleep(1)
                         
                     time.sleep(5)   
                             
                            
                     driver = webdriver.Chrome(chrome_path)  
                                
                     driver.get(chariot_path+'/'+str(test_script)+'.html')
                            
                     i = driver.find_element_by_xpath("/html/body/table[6]/tbody/tr[2]/td[2]")
                                
                     print format(i.text)
                 
                 else :
                     
                    print 'Channel or security is fail !!!!!'
                 
             except :
             
                print 'Connect to Router fail !!!!!' 
    
                pass    
             

             
             try :
             
                 format_value = str(format(i.text))
                 try :
                     format_value =  format_value.replace(",","")
                 except :
                     pass
                 
                 format_value = float(format_value)
                             
                 print format_value
                             
                 format_value = round(format_value)
                 
                 format_value = int(format_value)
                             
                 print format_value   
                 
                 file = open(save_result,'a') 
    
                 file.write(' Channel ' + str(j) + '   Throughtput = ' +str(format_value) +'    BW '+str(u) +'      script ' + str(test_script)+"\n") 
                 
                 
                 
                 try :
                  driver.quit()
                 except:
                  pass   
             except :
                                          
                 file.write(' Channel '+str(j)+'   Throughtput & RSSI  ' +'   script ' + str(test_script) + '    Error!!! ' +"\n")
                 
                 try :
                  driver.quit()
                 except:
                  pass   
                 pass   
                  


              
           
                
             try :   
                  for filename in os.listdir(chariot_path):
                    
                    
                    if filename.endswith('S'+'.html'): 
                         pass  
                    elif filename.endswith('S'+'_resp_time.gif'): 
                         pass
                     
                    elif filename.endswith('S'+'_throughput.gif'): 
                         pass
                     
                    elif filename.endswith('S'+'_trans_rate.gif'): 
                         pass 
                     
                      
                    elif filename.endswith("H.html"): 
                         os.chdir(chariot_path)
                         os.rename(filename,str(test_script)+'Channel '+str(j)+'   '+ '5G AC' +'    BW '+str(u)+ '   '+ 'WPA2-AES'+'.html')
                      
                    elif filename.endswith("H.gif"):
                             os.chdir(chariot_path)
                             os.rename(filename,str(test_script)+'Channel '+str(j)+'   '+ '5G AC' +'    BW '+str(u)+ '   '+ 'WPA2-AES'+'_resp_time.gif')
                            
                    elif filename.endswith("H.gif"):
                             os.chdir(chariot_path)
                             os.rename(filename,str(test_script)+'Channel '+str(j)+'   '+ '5G AC' +'    BW '+str(u)+'   '+'WPA2-AES'+'_throughput.gif')
                          
                    elif filename.endswith("H.gif"):
                             os.chdir(chariot_path)
                             os.rename(filename,str(test_script)+'Channel '+str(j)+'   '+ '5G AC' +'    BW '+str(u)+'   '+ 'WPA2-AES'+'_trans_rate.gif')
                           
                             
                     
                 
             except :
                     
                     pass

    
    
    time.sleep(2) 
    
    file.write("\n"+"\n")        
                
    file.write('End time :      '+str(datetime.now())+"\n"+"\n")
    

    
    
    print datetime.now()
    
  
    match_time = re.findall('[0-9]{4,}\W[0-9][0-9]\W[0-9][0-9]\W[0-9][0-9]\:[0-9][0-9]\:[0-9][0-9]',str(datetime.now()))
    print match_time
    match_time = str(match_time).replace(':','')
#             print match_time
#             match_time = re.findall('[0-9]\W[0-9][0-9][0-9][0-9][0-9][0-9]',str(match_time))
#             print match_time
        
    match_time = str(match_time).replace('-','')
    
    print match_time
  
    match_time = str(match_time).replace('[','')
    
    print match_time
    
    match_time = str(match_time).replace(']','')
    
    print match_time


    
#     for filename in os.listdir("C:\\"):
#         if filename.startswith("Throughput5g"): 
#             print 'copy 5g'
#             shutil.copyfile("C:\\"+str(filename), "D:\\Report\\"+str(model_name)+'  '+str(model_fw)+'  '+ '5G AC' + '   '+ str(match_time)+'.txt')

    
    
    
    try :
            
        print datetime.now()
        
      
        match_time = re.findall('[0-9]{4,}\W[0-9][0-9]\W[0-9][0-9]\W[0-9][0-9]\:[0-9][0-9]\:[0-9][0-9]',str(datetime.now()))
        print match_time
        match_time = str(match_time).replace(':','')
    #             print match_time
    #             match_time = re.findall('[0-9]\W[0-9][0-9][0-9][0-9][0-9][0-9]',str(match_time))
    #             print match_time
            
        match_time = str(match_time).replace('-','')
        
        print match_time
      
        match_time = str(match_time).replace('[','')
        
        print match_time
        
        match_time = str(match_time).replace(']','')
        
        print match_time
        
        
        
        if not os.path.exists(str(model_name)+' '+str(match_time)):
       
          os.makedirs(str(model_name)+' '+str(match_time))
        else :
            
          print 'Dir Already exist !!!'  
        
        
        for filename in os.listdir(chariot_path):
    #                 print filename
    #                 match_name = re.findall('\d[TR]{,1}[Xx]{,1}',filename) 
    #                 print match_name
            if filename.endswith(".html") : 
               print filename
               shutil.move(chariot_path+'\\'+str(filename),os.getcwd()+'\\'+str(model_name)+' '+str(match_time)) 
            elif filename.endswith(".gif") :
               print filename
               shutil.move(chariot_path+'\\'+str(filename),os.getcwd()+'\\'+str(model_name)+' '+str(match_time)) 
    
        file.close() 
        os._exit(1) 
    
    
    
    
    except :
         
         pass
  