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
    
       
    
    DUT_IP = conf.get ('Telnet','Dut_ip')
    
    Account_password = conf.get ('Accountpassword','Account_password1')
     
    save_profile = os.getcwd() + '//Profile'
    
    save_result = os.getcwd() +'//Result//Throughput2g.txt'
    
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
    
    
    Channel_ID = conf.get ('Channel_ID','channel2g')
    
    
    Appy_ID_1 = conf.get ('Appy_ID','apply1_2g')

    Appy_ID_2 = conf.get ('Appy_ID','apply2_2g')
    
    wifi_enable = 'http://' + Account_password + DUT_IP + '/index3.asp'
    
    ssid2g = conf.get ('Telnet','SSID1')
    
    ssid5g =  conf.get ('Telnet','SSID2')
    
    timesleep = conf.get ('2.4G_Time_sleep','sleep_time')
    
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
    
    Bandwidth_2g = conf.get('Band_width','2.4G_BW1')
    
    Bandwidth_5g = conf.get('Band_width','5G_BW1')
    
    channel_range = conf.get('Channel','channel2g')
    
    LAN_name = conf.get ('LAN','name')
    
    WLAN_name = conf.get ('WLAN','name')
    
    
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
    
    
    
    for i , n in enumerate ([0,36,40,44,48,149,153,157,161,165]) :
        
        print i ,n
        if int(channel5g_rangea) == n :
           channel5g_rangea = i
   
        elif int(channel5g_rangeb) == n :
           channel5g_rangeb = i
      
    print channel5g_rangea
    print channel5g_rangeb
    
    
    print channel_range
    
    if ',' in channel_range :
    
        channel_range_text = re.split(',',str(channel_range))
        
        print channel_range_text
        
#         print channel_range_text.sort(key=int)
#         
#         channel_range_list = channel_range_text.sort(key=int)
#         
#         print channel_range_list
        
    elif '~' in channel_range :
        
        channel_range_text = re.split('~',str(channel_range))
        
        print channel_range_text
        
        print range(int(channel_range_text[0]), int(channel_range_text[1])+1)
        
        channel_range_text = range(int(channel_range_text[0]), int(channel_range_text[1])+1)
        
        print channel_range_text
        
    else :
        
        channel_range_text = [channel_range] 
         
        print  channel_range_text  
     
        
        
    
#     time.sleep(3)
#     cmd3 = 'netsh wlan connect name='+str(ssid2g)+ ' ssid='+ str(ssid2g)
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
        
        
        
        
    file = open(save_result,'a') 
    
    file.write(str(model_name)+'  '+ str(model_fw)+"\n"+"\n")
    
    file.write('Channel and Bandwidth Throughput'+"\n"+"\n")
    
    file.write('Start time :      '+str(datetime.now())+"\n"+"\n")
         
    file.write('          2.4G BGN 5M BW=20~40 Open'+"\n" +"\n"+"\n")
         
    file.write('Channel'+' ' + str(channel2g_rangea) + ' ~ ' + str(channel2g_rangeb)  +   '  Throughput Average Mbps'+"\n" +"\n")      
 
    list_Throughput = []
    
    print channel_range_text
    
    
    band_width = ['1','3']
    
    
    for u in band_width:    
     for j in channel_range_text:  
        
        print u
              
        file = open(save_result,'a') 
            
        try :
             tn = telnetlib.Telnet(str(DUT_IP),"23") 
             time.sleep(3)        
                
        
             content = tn.read_very_eager()
             print content
             print("Auto login...")
        
             if 'login' in content:
                  
                print("Login to account...")
                
                tn.write(str(Account)+"\r\n")
                time.sleep(1)
                content = tn.read_very_eager()
                
                print content
        
                print("Login to password...")
                tn.write(str(Password)+"\r\n")
                time.sleep(2)
                content = tn.read_very_eager()
                
                print content
                
                time.sleep(2)
                
               
        
             else :
                
                print 'Telnet connect fail !!!'
                pass 
             
             
             
             
             time.sleep(10)
             tn.write('nvram set wl0_ssid='+str(ssid2g)+"\r\n")
             time.sleep(2)   
             tn.write('nvram set wl_ssid='+str(ssid2g)+"\r\n")
             time.sleep(2)   
             tn.write('nvram set wl0_bw_cap='+str(u)+"\r\n")
             time.sleep(2) 
             if '1' in u  :
                 tn.write('nvram set wl0_chanspec='+str(j)+"\r\n")
                 time.sleep(2)  
             else :
                 tn.write('nvram set wl0_chanspec='+str(j)+'l'+"\r\n")
                 time.sleep(2) 
                     
             
             
             if j == '10' or j == '11' or j=='12' or j=='13' :
                 tn.write('nvram set wl0_chanspec='+str(j)+'u'+"\r\n")
                 time.sleep(2) 
             else :
                 pass
      
             tn.write('nvram set wl0_contry_code=JP'+"\r\n")
             time.sleep(2) 
             tn.write('nvram set wl0_contry_rev=0'+"\r\n")
             time.sleep(2) 
#              tn.write('nvram set wl0_akm='+ str(Authentication2g)+"\r\n")
#              time.sleep(2) 
#              tn.write('nvram set wl0_auth_mode_x='+ str(Authentication2g)+"\r\n")
#              time.sleep(2) 
#              tn.write('nvram set wl0_auth_mode='+ str(Auth_mode2g)+"\r\n")
#              time.sleep(2) 
#              tn.write('nvram set wl0_crypto='+ str(Encryption2g)+"\r\n")
#              time.sleep(2) 
#              tn.write('nvram set wl0_wpa_psk='+ str(PresharedKey2g)+"\r\n")
#              time.sleep(2)                                      
             tn.write('wlconf eth1 down'+"\r\n")
             time.sleep(2) 
             tn.write('wlconf eth1 up'+"\r\n")
             time.sleep(2) 
             tn.write('wlconf eth1 start'+"\r\n")
             time.sleep(2) 
             tn.write('wl status'+"\r\n")
             time.sleep(2) 
             tn.write('nvram get wl0_chanspec'+"\r\n")
             time.sleep(2) 
#              tn.write('wl -i eth1 sta_info 74-DA-38-5E-A2-90')
#              time.sleep(2) 
             content = tn.read_very_eager()
             print content
               
             time.sleep(2) 
               
             print 'Channel ' + str(j)
             time.sleep(2) 
             
        except :
             pass
         
   
             
        time.sleep(int(timesleep))
         
        cmd3 = 'netsh wlan disconnect'
        print cmd3
        os.system(cmd3)  
         
        time.sleep(5)
         
        cmd3 = 'netsh wlan connect name='+str(ssid2g)+ ' ssid='+ str(ssid2g)
        print cmd3
        pingPopen = subprocess.Popen(args=cmd3, shell=True, stdout=subprocess.PIPE)
        pingstring = pingPopen.stdout.read()
        print pingstring 
         
        time.sleep(20)   
         
         
        if 'not' in pingstring : 
             
                cmd3 = 'netsh interface set interface '+str(WLAN_name)+ ' disable'
                print cmd3
                os.system(cmd3)  
                
                time.sleep(3)
                
                cmd3 = 'netsh interface set interface '+str(WLAN_name)+ ' enable'
                print cmd3
                os.system(cmd3)  
                
                time.sleep(3)
                
             
                       
                cmd3 = 'netsh wlan connect name='+str(ssid2g)+ ' ssid='+ str(ssid2g)
                print cmd3
                os.system(cmd3)  
                time.sleep(int(timesleep))
                
        else :
                 
                 pass   
             
        try :    
                 tn = telnetlib.Telnet(str(DUT_IP),"23") 
                 time.sleep(3)        
                
        
                 content = tn.read_very_eager()
                 print content
                 print("Auto login...")
        
                 if 'login' in content:
                  
                    print("Login to account...")
                    
                    tn.write(str(Account)+"\r\n")
                    time.sleep(1)
                    content = tn.read_very_eager()
                    
                    print content
            
                    print("Login to password...")
                    tn.write(str(Password)+"\r\n")
                    time.sleep(2)
                    content = tn.read_very_eager()
                    
                    print content
                    
                    time.sleep(2)
                
               
        
                 else :
                
                    print 'Telnet connect fail !!!'
                    pass      
             
        except :
            
            pass 


         
         
        for i in range(1 , 5 , 1):  
         
         time.sleep(5) 
         
         test_script = conf.get ('Test_script','script'+str(i))
#          file.write("\n"+"\n")
#          file.write(str(test_script)+ "\n"+"\n") 
       
       
       
         print '===== 2.4G '+'Channel ' + str(j) + ' script ' + str(test_script) + ' ======='
         
         

         

         try :
          if 'root' in content :
                       
             try :
                 
   
                 time.sleep(5)
                 print '========= Get RSSI value ========='                 
                 time.sleep(5)
                 cmd = 'wl -i eth1 sta_info '+str(MAC)+' | grep average'
                 print cmd
                 time.sleep(3)
                 cmd3 = tn.write(str(cmd)+"\r\n")
                                
                 time.sleep(5)
                 
                 pingstring = tn.read_very_eager()
                 
                 time.sleep(5)
                 
                 print pingstring
   
                 
     
                 time.sleep(3)
                 pingstring = re.findall('[0-9]{1,}',pingstring)
                 time.sleep(3)
                 print pingstring
                 
             
             except :
                 pass
             
             try :
                 RSSI = '-'+pingstring[-5] 
                 
                 print RSSI
             except :
                 pass    

#              if str(Authentication2g) in str(pingstring6) is True  :  
             if 1  :
#              if str(Authentication2g) == str(Authentication2g) :
                 
                 print 'Get RSSI pass!!!'
             
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
                 except:                    
                     pass    
                 
                 format_value = float(format_value)
                             
                 print format_value
                             
                 format_value = round(format_value)
                 
                 format_value = int(format_value)
                             
                 print format_value   
                 
                 file = open(save_result,'a') 
    
                 file.write(' Channel ' + str(j) + '   Throughtput = ' +str(format_value) +'    RSSI = '+str(RSSI)+'    BW '+str(int(u)+1) +'0'+'      script ' + str(test_script)+"\n") 
     
                 
                 try :
                  driver.quit()
                 except:
                  pass   
                     
         except :
                 
                 file.write(' Channel '+str(j)+'   Throughtput & RSSI  ' +'   script ' + str(test_script) + '     Error!!! ' +"\n")
                 try :
                  driver.quit()   
                 except:
                  pass   
                 
                 pass   
                 
        
                
                 


#          list_Throughput = []
#          else :
#            pass   
               
           
         
         try :   
                  for filename in os.listdir(chariot_path):
                    
                    
                    if filename.endswith('Open'+'.html'): 
                         pass  
                    elif filename.endswith('Open'+'_resp_time.gif'): 
                         pass
                     
                    elif filename.endswith('Open'+'_throughput.gif'): 
                         pass
                     
                    elif filename.endswith('Open'+'_trans_rate.gif'): 
                         pass 
                     
                      
                    elif filename.endswith("P.html"): 
                         os.chdir(chariot_path)
                         os.rename(filename,str(test_script)+'Channel '+str(j)+'   '+ '2.4G BGN' +'    BW '+str(int(u)+1) +'   '+ 'Open'+'.html')
                      
                    elif filename.endswith("P.gif"):
                             os.chdir(chariot_path)
                             os.rename(filename,str(test_script)+'Channel '+str(j)+'   '+ '2.4G BGN'+'    BW '+str(int(u)+1) + '   '+ 'Open'+'_resp_time.gif')
                            
                    elif filename.endswith("P.gif"):
                             os.chdir(chariot_path)
                             os.rename(filename,str(test_script)+'Channel '+str(j)+'   '+ '2.4G BGN' +'    BW '+str(int(u)+1) + '   '+'Open'+'_throughput.gif')
                          
                    elif filename.endswith("P.gif"):
                             os.chdir(chariot_path)
                             os.rename(filename,str(test_script)+'Channel '+str(j)+'   '+ '2.4G BGN' +'    BW '+str(int(u)+1) + '   '+ 'Open'+'_trans_rate.gif')
                           
                             
                     
                 
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
  
        
        
#     time.sleep(7)
#     
#     cmd3 = 'netsh wlan delete profile name='+str(ssid2g)
#     print cmd3
#     os.system(cmd3) 