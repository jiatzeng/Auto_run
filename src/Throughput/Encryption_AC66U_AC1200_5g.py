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


from VideoBridge import *
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
    sys.setdefaultencoding('utf8')
         
    conf = RawConfigParser()
    conf.read('config.ini')
    
       
    
    DUT_IP = conf.get ('ip','Dut_ip1')
    
    Account_password = conf.get ('Accountpassword','Account_password1')
     
    
    DST = 'http://' + Account_password + DUT_IP
    
    Basic2g_link = conf.get ('Basic_link','Basic2g')
    
    Basic5g_link = conf.get ('Basic_link','Basic5g')
    
    entry2g_link = conf.get ('Encryption_link','entry2g')
    
    entry5g_link = conf.get ('Encryption_link','entry5g')
    
    select_5g_id = conf.get ('Encryption_link','select_5g')
    
    
    save_profile = os.getcwd() + '//Profile'
    
    save_result = os.getcwd() +'//Result//Throughput5g.txt'
    
    chrome_path = os.getcwd() + '//chromedriver_win32//chromedriver.exe'
    
    chariot_path = os.getcwd() + '/Chariot_tst'
    
    
    
    Basic2g = 'http://' + Account_password + DUT_IP + str(Basic2g_link)
    
    Basic5g = 'http://' + Account_password + DUT_IP + str(Basic5g_link)
    
    entry2g = 'http://' + Account_password + DUT_IP + str(entry2g_link)
    
    entry5g = 'http://' + Account_password + DUT_IP + str(entry5g_link)
    
    
    Channel_ID = conf.get ('Channel_ID','channel5g')
    

    
    Appy_ID_1 = conf.get ('Appy_ID','apply1_5g')

    Appy_ID_2 = conf.get ('Appy_ID','apply2_5g')
    
    

    timesleep = conf.get ('5G_Time_sleep','sleep_time')
    
    channel2g_rangea = conf.get ('Security_Channel','channel2g_rangea')

    channel2g_rangeb = conf.get ('Security_Channel','channel2g_rangeb')

    channel5g_rangea = conf.get ('Security_Channel','channel5g_rangea')

    channel5g_rangeb = conf.get ('Security_Channel','channel5g_rangeb')
    

    
    model_name = conf.get('Model','name')
    
    model_fw = conf.get('Model','FW')
    
    channel_range = conf.get('Channel','channel5g')
    
    LAN_name = conf.get ('LAN','name')
    
    
    WLAN_name = conf.get ('WLAN','name')
    
    
    wifi_enable = 'http://' + Account_password + DUT_IP + '/index3.asp'
    
    
    DUT_IP = conf.get ('Telnet','Dut_ip')
        
    Account = conf.get ('Telnet','Account')
       
    Password = conf.get ('Telnet','password')
    
    
    ssid5g_1 = conf.get('SSID5g','SSID1')
    
    ssid5g_2 = conf.get('SSID5g','SSID5')
    
    MAC = conf.get('Telnet','MAC')
    
    
    BW_Mode = ['1','2'] 
    
    BW_bandwidth = ['1','3']
    
    Authentication5g_1 = ['','psk2']
    
    Authentication5g_2 = ['open','psk2']
    
    Encryption5g = ['none','none']
    
    Auth_mode5g = ['tkip+aes','aes']
    
    PresharedKey5g = ['12345678','12345678']
    
    ssid5g =[str(ssid5g_1),str(ssid5g_2)]
    
    
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
            for filename in os.listdir("D:\Profile"):
#                 print filename
#                 match_name = re.findall('\d[TR]{,1}[Xx]{,1}',filename) 
#                 print match_name
                os.chdir("D:\Profile")
                
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
            for filename in os.listdir("C:\Program Files\Ixia\IxChariot"):
#                 print filename
#                 match_name = re.findall('\d[TR]{,1}[Xx]{,1}',filename) 
#                 print match_name
                if filename.endswith(".html") or filename.endswith(".gif") : 
                   print filename
                   os.remove('C:\\Program Files\\Ixia\\IxChariot\\'+filename)
                   
    except :
        
            pass   
        
        
        
        
    
    
    file = open('D:\Throughput5g.txt','a') 
    
    file.write('Start time :      '+str(datetime.now())+"\n"+"\n")
       
    file.write(str(model_name)+'  '+ str(model_fw)+"\n"+"\n")
    
    file.write('Encryption Throughput'+"\n"+"\n")
    
    file.write('        5G  5M Auto BW=20 1. None , TX , RX , TX+RX'+"\n" +"\n"+"\n")
    
    file.write('        5G  5M Auto BW=20 2. WPA2-AES , TX , RX , TX+RX'+"\n" +"\n"+"\n")
    
    file.write('        5G  5M Auto BW=40 1. None , TX , RX , TX+RX'+"\n" +"\n"+"\n")
    
    file.write('        5G  5M Auto BW=40 2. WPA2-AES , TX , RX , TX+RX'+"\n" +"\n"+"\n")
    
    
    channel5g_a = conf.get ('Channel','channel5g_rangea')

    channel5g_b = conf.get ('Channel','channel5g_rangeb')
    
         
    file.write('Channel'+' ' + str(channel5g_a) + ' ~ ' + str(channel5g_b)  +   '  Throughput Average Mbps'+"\n" +"\n")    
    
      
    
    list_Throughput = []
    
    
    print channel_range_text
    


        
    for i in range(1 , 4 , 1): 
        
        test_script = conf.get ('Test_script','script'+str(i))
        file.write("\n"+"\n")
        file.write(str(test_script)+ "\n"+"\n")
        
        for j in channel_range_text:   
          for u in range(0 , 2 , 1):   
              
             file = open('D:\Throughput5g.txt','a')
             
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
                   tn.write('nvram set wl1_ssid='+str(ssid5g[u])+"\r\n")
                   time.sleep(2)   
                   tn.write('nvram set wl_ssid='+str(ssid5g[u])+"\r\n")
                   time.sleep(2) 
#                    tn.write('nvram set wl1_bw='+str(BW_Mode[u])+"\r\n")
#                    time.sleep(2)                  
                   tn.write('nvram set wl1_bw_cap='+str(BW_bandwidth[u])+"\r\n")
                   time.sleep(2)
                   if '1' in str(BW_bandwidth[u]) :
                      tn.write('nvram set wl1_chanspec='+str(j)+"\r\n")
                      time.sleep(2) 
                        
                   else :  
                      tn.write('nvram set wl1_chanspec='+str(j)+'l'+"\r\n")
                      time.sleep(2)  
                       
                   tn.write('nvram set wl1_contry_code=SG'+"\r\n")
                   time.sleep(2) 
                   tn.write('nvram set wl1_contry_rev=10'+"\r\n")
                   time.sleep(2) 
                   tn.write('nvram set wl1_akm='+ str(Authentication5g_1[u])+"\r\n")
                   time.sleep(2) 
                   tn.write('nvram set wl1_auth_mode_x='+ str(Authentication5g_2[u])+"\r\n")
                   time.sleep(2) 
                   tn.write('nvram set wl1_auth_mode='+ str(Auth_mode5g[u])+"\r\n")
                   time.sleep(2) 
                   tn.write('nvram set wl1_crypto='+ str(Encryption5g[u])+"\r\n")
                   time.sleep(2) 
                   tn.write('nvram set wl1_wpa_psk='+ str(PresharedKey5g[u])+"\r\n")
                   time.sleep(2)                     
                   tn.write('wlconf eth2 down'+"\r\n")
                   time.sleep(2)                   
                   tn.write('wlconf eth2 up'+"\r\n")
                   time.sleep(2) 
                   tn.write('wlconf eth2 start'+"\r\n")
                   time.sleep(2) 

                   tn.write('wl -i eth2 status'+"\r\n")
                   time.sleep(2) 
                   tn.write('nvram get wl1_chanspec'+"\r\n")
                   time.sleep(2) 
                   content = tn.read_very_eager()
                   print content
                   time.sleep(2) 
                   tn.close()  
                   print 'Channel ' + str(j)
                   time.sleep(10) 
                   
                   driver = webdriver.Firefox()
                    
                   driver.get(entry5g)
                   
                   time.sleep(5) 
             
                   driver.find_element_by_xpath(str(select_5g_id)).click()
             
                   time.sleep(5)
             
                   driver.find_element_by_id(str(Appy_ID_1)).click()
             
                   time.sleep(int(timesleep)) 
                   
                   driver.close()
                   
                   
                   
#                    tn.write('reboot'+"\r\n")
#                    time.sleep(int(timesleep)) 

             except:
                 pass
                        
             time.sleep(20)
             
             cmd3 = 'netsh wlan disconnect'
             print cmd3
             os.system(cmd3)  
             
             time.sleep(5)
             
             
                 
             cmd3 = 'netsh wlan connect name='+str(ssid5g[u])+ ' ssid='+ str(ssid5g[u])
             print cmd3
             pingPopen = subprocess.Popen(args=cmd3, shell=True, stdout=subprocess.PIPE)
             pingstring = pingPopen.stdout.read()
             print pingstring 
    
             time.sleep(int(timesleep))
             
             if 'not' in pingstring : 
                 
                
                cmd3 = 'netsh interface set interface '+str(WLAN_name)+ ' disable'
                print cmd3
                os.system(cmd3)  
                
                time.sleep(3)
                
                cmd3 = 'netsh interface set interface '+str(WLAN_name)+ ' enable'
                print cmd3
                os.system(cmd3)  
                
                time.sleep(3)
                  
                 
                 
                 
                 
                cmd3 = 'netsh wlan connect name='+str(ssid5g[u])+ ' ssid='+ str(ssid5g[u])
                print cmd3
                os.system(cmd3)  
                time.sleep(int(timesleep))
                
             else :
                 
                 pass   
                
             
             cmd2 = 'Ping ' + str(DUT_IP) +' -n 5' 
             print cmd2
             pingPopen = subprocess.Popen(args=cmd2, shell=True, stdout=subprocess.PIPE)
             pingstring = pingPopen.stdout.read()
             print pingstring 
             
    
             try :
              if 'Reply' and 'TTL=64' in pingstring :
                           
                 try :
                     print 'Check networkcard information....'
                     time.sleep(9)
                     cmd = 'netsh wlan show interfaces'
                     print cmd
                     pingPopen = subprocess.Popen(args= cmd, shell=True, stdout=subprocess.PIPE)
                     pingstring = pingPopen.stdout.read()
                     print pingstring
                     time.sleep(9)
                     cmd = 'netsh wlan show interfaces'
                     print cmd
                     pingPopen = subprocess.Popen(args= cmd, shell=True, stdout=subprocess.PIPE)
                     pingstring = pingPopen.stdout.read()
                     print pingstring
                     
                     pingstring = re.split('\n',pingstring)
                     
                     pingstring1 = [x for x in pingstring if 'Channel' in x]
                     
                     pingstring1 = re.findall('[0-9]{1,}',pingstring1[0])
                     
                     print pingstring1
                     
                     pingstring2 = [x for x in pingstring if 'Cipher' in x]
                     
                     pingstring2 = re.findall('[:]{1}\s{1}[a-zA-Z]{,6}',pingstring2[0])
                     
                     print pingstring2
                     
                     pingstring3 = [x for x in pingstring if 'Authentication' in x]
                     
                     print pingstring3
                     
                     pingstring4 = re.findall('[:]{1}\s{1}[a-zA-Z]{,6}',pingstring3[0])
                     
                     print pingstring4
                     
                     pingstring5 = str(pingstring2[0])+str(pingstring4[0])
                     
                     print pingstring5
                     
                 
                 except :
                     pass
                 
                 print j
                 
                 print pingstring1[0]
                 
                 print str(Authentication5g_2[u]).upper()
                 
                 print str(Encryption5g).upper()
                 
                 print pingstring5
                 
                 print str(Authentication5g_2[u]).capitalize()
                 
                 print str(Encryption5g).capitalize()
                 
                 print str(Authentication5g_2[u]).lower()
                 
                 print str(Encryption5g).lower()
                 
                 
                 pingstring6 = str(ssid5g).upper()+str(ssid5g).lower()+str(Authentication5g_2[u]).upper() + str(Encryption5g[u]).upper() + str(Authentication5g_2[u]).lower() + str(Encryption5g[u]).lower() + str(Authentication5g_2[u]).capitalize() + str(Encryption5g[u]).capitalize()
                 
                 print pingstring6
                 
                 print str(Authentication5g_2[u])
                 
                 if str(Authentication5g_2[u]) in str(pingstring6)  :
                     
                     print 'yes'
                     
                 else :
                     
                     print 'No'    
                 
                 if str(j) == str(pingstring1[0])  :
                     
                     print 'yes'
                     
                 else :
                     
                     print 'No'   
    
    #              if str(Authentication2g) in str(pingstring6) is True  :  
                 if str(j) == str(pingstring1[0]) and str(Authentication5g_2[u]) in str(pingstring6) :
#                  if str(Authentication5g) == str(Authentication5g) :
                     
                     print 'Channel and security is pass !!!!'
                 
                     print 'Start throughput test !!!'
                     
                     
                     time.sleep(5)
                 
                     cmd3 = 'netsh interface set interface '+str(LAN_name)+ ' disable'
                     print cmd3
                     os.system(cmd3)  
                 
                     time.sleep(15)
                     
                 
                                                   
                    
                     os.chdir("C:\Program Files\Ixia\IxChariot")
                             
                              
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
                     
                     cmd3 = 'netsh interface set interface '+str(LAN_name)+ ' enable'
                     print cmd3
                     os.system(cmd3)  
                 
                     time.sleep(20)   
                             
                            
                     driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")  
                            
                     driver.get('file:///C:/Program%20Files/Ixia/IxChariot/'+str(test_script)+'.html')
                            
                     i = driver.find_element_by_xpath("/html/body/table[6]/tbody/tr[2]/td[2]")
                                
                     print format(i.text)
             
                     format_value = float(format(i.text))
                     
                     print format_value
                     
                     format_value = int(format_value)
                     
                     print format_value   
                 
                 else :
                     
                    print 'Channel or security is fail !!!!!'
                 
             except :
             
                print 'Connect to Router fail !!!!!' 
    
                pass    
             
             
             
             
             
             try :
             
                 format_value = float(format(i.text))
                     
                 print format_value
                     
                 format_value = int(format_value)
                     
                 print format_value   
                 
                 file = open('D:\Throughput5g.txt','a') 

                 file.write(str(format_value) +"\n") 
                 try :
                  driver.quit()
                 except:
                  pass   
             except :
                 
                 file.write('Channel '+str(j)+' Error!!!' +"\n")  
                 
                 try :
                  driver.quit()
                 except:
                  pass   
                 pass   
                  


              
           
                
             try :
              for filename in os.listdir("C:\Program Files\Ixia\IxChariot"):
                if filename.endswith("X.html"): 
                     os.chdir("C:\Program Files\Ixia\IxChariot")
                     os.rename(filename,str(test_script)+'Channel '+str(j)+'   '+ '5G AC' + '   '+ 'WPA2-AES'+'.html')
                  
                elif filename.endswith("X_resp_time.gif"):
                     os.chdir("C:\Program Files\Ixia\IxChariot")
                     os.rename(filename,str(test_script)+'Channel '+str(j)+'   '+ '5G AC' + '   '+ 'WPA2-AES'+'_resp_time.gif')
                   
                elif filename.endswith("X_throughput.gif"):
                     os.chdir("C:\Program Files\Ixia\IxChariot")
                     os.rename(filename,str(test_script)+'Channel '+str(j)+'   '+ '5G AC' + '   '+ 'WPA2-AES'+'_throughput.gif')
                   
                elif filename.endswith("X_trans_rate.gif"):
                     os.chdir("C:\Program Files\Ixia\IxChariot")
                     os.rename(filename,str(test_script)+'Channel '+str(j)+'   '+ '5G AC' + '   '+ 'WPA2-AES'+'_trans_rate.gif')
                 
                    
                     
                elif filename.endswith("WPA2-AES.html"): 
                     pass
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
            
            
            
            if not os.path.exists("D:\\Report\\"+str(model_name)+' '+str(match_time)):
            
              os.makedirs("D:\\Report\\"+str(model_name)+' '+str(match_time))
            else :
                
              print 'Dir Already exist !!!'  
            
            
            for filename in os.listdir("C:\Program Files\Ixia\IxChariot"):
#                 print filename
#                 match_name = re.findall('\d[TR]{,1}[Xx]{,1}',filename) 
#                 print match_name
                if filename.endswith(".html") or filename.endswith(".gif"): 
                   print filename
                   shutil.move("C:\\Program Files\\Ixia\\IxChariot\\"+str(filename),"D:\\Report\\"+str(model_name)+' '+str(match_time)+"\\"+str(filename)) 

                   
                   
    except :
        
            pass  