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
    
    Bridge_IP = conf.get ('Bridge_ip','Bridge_IP')
    
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
    
    Bridege_link = conf.get ('Bridge_link','Bridge_mode')
    
    
    
    
    Basic2g = 'http://' + Account_password + DUT_IP + str(Basic2g_link)
    
    Basic5g = 'http://' + Account_password + DUT_IP + str(Basic5g_link)
    
    entry2g = 'http://' + Account_password + DUT_IP + str(entry2g_link)
    
    entry5g = 'http://' + Account_password + DUT_IP + str(entry5g_link)
    
    BridegeMode = 'http://' + Account_password + Bridge_IP + str(Bridege_link)
    
    
    Channel_ID = conf.get ('Channel_ID','channel5g')
    
    
    Appy_ID_1 = conf.get ('Appy_ID','apply1_5g')

    Appy_ID_2 = conf.get ('Appy_ID','apply2_5g')
    
    
    ssid2g = conf.get ('SSID','SSID1')
    
    ssid5g =  conf.get ('SSID','SSID2')
    
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
    
    Time = conf.get('Test_script','Time') 
    
    time_bridge = conf.get('Bridge_ip','time')
    
    scan_path = conf.get('Bridge_ip','scan_path')
    
    Rescan_path = conf.get('Bridge_ip','Rescan_path')

    Add_path = conf.get('Bridge_ip','Add_path')

    Enable_path = conf.get('Bridge_ip','Enable_path')

    Channel_ID = conf.get ('Channel_ID','channel5g')
    
    
    Appy_ID_1 = conf.get ('Appy_ID','apply1_5g')

    Appy_ID_2 = conf.get ('Appy_ID','apply2_5g')
        
    SSID_name = conf.get ('SSID5g','SSID_name')       
    
    Band_name = conf.get ('Band_width','BW_5G_ID')
    
    BW_name = conf.get('Band_width','Band_Width_5G_ID')
    
    WLAN_name = conf.get ('WLAN','name')
    
    Time = conf.get('Security_Test_script','Time')
    
    
    
    
    
    
    
    wifi_enable = 'http://' + Account_password + DUT_IP + '/index3.asp'
    
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
    
    
    if ',' in channel_range :
    
        channel_range_text = re.split(',',str(channel_range))
        
        print channel_range_text
        
#         print channel_range_text.sort(key=int)
#         
#         channel_range_list = channel_range_text.sort(key=int)
#         
#         print channel_range_list
#         
    elif '~' in channel_range :
        
        channel_range_text = re.split('~',str(channel_range))
        
        print channel_range_text
        
        print range(int(channel_range_text[0]), int(channel_range_text[1])+1)
        
        channel_range_text = range(int(channel_range_text[0]), int(channel_range_text[1])+1)
        
        print channel_range_text
        
    else :
        
        channel_range_text = [channel_range] 
         
        print  channel_range_text
        
    
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
        
        
        
        
        
    try :
            for filename in os.listdir(chariot_path):
#                 print filename
#                 match_name = re.findall('\d[TR]{,1}[Xx]{,1}',filename) 
#                 print match_name
                if filename.endswith(".html") or filename.endswith(".gif") : 
                   print filename
                   os.remove(chariot_path+'\\'+filename)
                    
    except :
         
            pass   
     
     
    file = open(save_result,'a') 
     
    file.write('Start time :      '+str(datetime.now())+"\n"+"\n")
        
    file.write(str(model_name)+'  '+ str(model_fw)+"\n"+"\n")
     
    file.write('Channel and Bandwidth Throughput'+"\n"+"\n")
              
    file.write('          5G AC 5M BW=80 WPA2-AES'+"\n" +"\n"+"\n")
     
    channel5g_a = conf.get ('Channel','channel5g_rangea')
 
    channel5g_b = conf.get ('Channel','channel5g_rangeb')
     
          
    file.write('Channel'+' ' + str(channel5g_a) + ' ~ ' + str(channel5g_b)  +   '  Throughput Average Mbps'+"\n" +"\n")    


    time.sleep(5)
    
    driver = webdriver.Chrome(chrome_path)
            
    driver.get(Basic5g)
       
    
    time.sleep(4)
    
  
           
    try :
           
       driver.find_element_by_name(str(SSID_name)).clear()
       time.sleep(4)
       driver.find_element_by_name(str(SSID_name)).send_keys(str(ssid5g))
        
       time.sleep(4)
        
    except:
        pass   
    
    try :
        
       BW_MODE = conf.get('Band_width','5G_Mode3') 
       
       Select(driver.find_element_by_name(str(Band_name))).select_by_visible_text(str(BW_MODE))
        
        
       time.sleep(2)
       
    except:
       pass     
    

    
    try :
          BW_width = conf.get('Band_width','5G_BW3')
       
          chan_band_width = driver.find_element_by_name(str(BW_name))
           
          print str(format(chan_band_width.text))
      
          chan_band_width = re.findall('\d{,2}\s[a-zA-Z]{,3}',str(format(chan_band_width.text)))
            
          print chan_band_width
           
          print chan_band_width[1]
           
          if '80' in str(BW_width):
            
           try :
            Select(driver.find_element_by_name(str(BW_name))).select_by_value('7')   
           except :
            pass   
     
            
          else :  
           Select(driver.find_element_by_name(str(BW_name))).select_by_visible_text(str(BW_width))
       
    except :
          pass
              
    try : 
          el = driver.find_element_by_xpath(str(Appy_ID_1))
          
          webdriver.ActionChains(driver).move_to_element(el).click(el).perform() 
           
          time.sleep(3)
           
    except :
          pass    
    
 
    time.sleep(int(timesleep))
        
    driver.close()
    
    driver = webdriver.Chrome(chrome_path) 
        
    time.sleep(5) 
        
    driver.get(entry5g)
       
    time.sleep(5)
    

       
    try: 
        
       Authentication2g_id = conf.get ('Encryption_Throughput_5g','WPA_Mode') 
       
       Authentication2g = conf.get ('Encryption_Throughput_5g','Authentication5')
       
       Select(driver.find_element_by_name(str(Authentication2g_id))).select_by_value(str(Authentication2g))
              
       time.sleep(1)
       
    except:
       pass
       
    try:
    
                     WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                                    'Timed out waiting for PA creation ' + 
                                                    'confirmation popup to appear.')
                  
                     alert = driver.switch_to_alert()
                     alert_text = alert.text
                     print alert.text
                     alert.accept()
                 
                 #    print alert.text
                     print "alert accepted"
                     pass
    except :
                     print "no alert"
                     pass 
              
      
      
      
    try :    
           
           
          Encryptionmode2g = conf.get('Encryption_Throughput_5g','WPA_Encryptionmode')
           
          driver.find_element_by_xpath(str(Encryptionmode2g)).click()
                      
          time.sleep(1)
    except :
          pass
       
       
       
       
    
    try :
        
          EncryptionType2g = conf.get('Encryption_Throughput_5g','WPA_EncryptionType')
        
          driver.find_element_by_xpath(str(EncryptionType2g)).click()
                          
          time.sleep(1)
    except :
          pass
       
       
       
    try :
          
          Encryption2g_id = conf.get ('Encryption_Throughput_5g','WPA_Encryptionmode')
          
          Encryption2g = conf.get ('Encryption_Throughput_5g','Encryption5')
           
           
          Select(driver.find_element_by_name(str(Encryption2g_id))).select_by_value(str(Encryption2g))
      
                      
          time.sleep(1)
    except :
           
          pass
       
        
       
    try :    
        
          KeyFormat2g_id = conf.get ('Encryption_Throughput_5g','WPA_psk')
          
          KeyFormat2g = conf.get ('Encryption_Throughput_5g','Key Format5')
                  
          Select(driver.find_element_by_name(str(KeyFormat2g_id))).select_by_value(str(KeyFormat2g))
          time.sleep(1)
    except :
          pass
                  
          
    
       
           
    try:
    
                     WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                                    'Timed out waiting for PA creation ' + 
                                                    'confirmation popup to appear.')
                  
                     alert = driver.switch_to_alert()
                     alert_text = alert.text
                     print alert.text
                     alert.accept()
                 
                 #    print alert.text
                     print "alert accepted"
                     pass
    except :
                     print "no alert"
                     pass 
           
    try :   
          
          PresharedKey2g_id = conf.get ('Encryption_Throughput_5g','WPA_key')
          
          PresharedKey2g = conf.get ('Encryption_Throughput_5g','Pre-shared Key5')
        
        
                
          driver.find_element_by_name(str(PresharedKey2g_id)).clear()
                  
          time.sleep(1)
                  
          driver.find_element_by_name(str(PresharedKey2g_id)).send_keys(str(PresharedKey2g))
                  
          time.sleep(1)
     
    except :
           
          pass
    
    
           
    time.sleep(5)
           
    
       
       
    try :   
            
          el = driver.find_element_by_xpath(str(Appy_ID_1))
          
          webdriver.ActionChains(driver).move_to_element(el).click(el).perform() 
           
          time.sleep(3)
           
    except :
          pass   
       
       
       
    try:
    
                     WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                                    'Timed out waiting for PA creation ' + 
                                                    'confirmation popup to appear.')
                  
                     alert = driver.switch_to_alert()
                     alert_text = alert.text
                     print alert.text
                     alert.accept()
                 
                 #    print alert.text
                     print "alert accepted"
                     pass
    except :
                     print "no alert"
                     pass 
            
    
        
        
        
        
    time.sleep(int(timesleep)) 
        
    driver.close()
      
      
#     driver = webdriver.Chrome(chrome_path) 
#         
#         
#     driver.get(BridegeMode)
#         
#     time.sleep(40)
#         
#     try :
#       
#           for p in range(1,25,1):
#               
#             
#               i = driver.find_element_by_xpath("//*[@id='table_11a']/tbody/tr["+str(p)+"]/td[3]")
#                                                
#                                                
#               print format(i.text)   
#               
#               g = format(i.text) 
#               
#                           
#               
#               if g == str(ssid5g) :
#                   
#                   print 'find !!!'
#                   
#                   print p
#                   
#                   
#                   driver.find_element_by_xpath("//*[@id='table_11a']/tbody/tr["+str(p)+"]/td[1]/input").click()
#                   
#                   time.sleep(5)
#                   
#            
#                   
#                   break
#                   
#               else :
#                   
#                   print 'Not find !!!!'
#                   
#                   pass    
#       
#     except :
#           
#           pass
#               
#     try :
#       
#           driver.find_element_by_xpath("//*[@id='next_but']/td/img[2]").click()  
#                   
#           time.sleep(5)  
#           
#     except :
#           
#           pass
#             
#       
#     try :
#       
#       
#           WebDriverWait(driver, 3).until(EC.alert_is_present(),
#                                         'Timed out waiting for PA creation ' + 
#                                         'confirmation popup to appear.')
#      
#           alert = driver.switch_to_alert()
#           alert_text = alert.text
#           print alert.text
#           
#           h = alert.text
#           
#     except :
#           
#           pass    
#       
#     time.sleep(5)
#       
#     try :
#       
#           if h == 'Please select one entry to connect!' :
#               
#               print 'Repeat scan !!!'
#               
#               driver.close()
#               
#               driver = webdriver.Chrome(chrome_path) 
#                 
#                 
#               driver.get(BridegeMode)
#                 
#               time.sleep(40)
#               
#         
#               
#               for p in range(1,25,1):
#                   
#      
#                 
#                   i = driver.find_element_by_xpath("//*[@id='table_11a']/tbody/tr["+str(p)+"]/td[3]")
#                                              
#                   print format(i.text)   
#                   
#                   g = format(i.text) 
#                   
#                               
#                   
#                   if g == str(ssid5g) :
#                       
#                       print 'find !!!'
#                       
#                       print p
#                       
#               
#                       
#                       driver.find_element_by_xpath("//*[@id='table_11a']/tbody/tr["+str(p)+"]/td[1]/input").click()
#                       
#                       time.sleep(5)
#                       
#                
#                       
#                       break
#                       
#                   else :
#                       
#                       print 'Not find !!!!'
#                       
#                       pass    
#                   
#           else :
#               
#               print 'scan pass !!'
#               
#               pass    
#       
#     except :
#           
#           pass
#       
#       
#           
#     try :
#       
#           driver.find_element_by_xpath("//*[@id='next_but']/td/img[2]").click()  
#                   
#           time.sleep(5)    
#       
#     except :
#           
#           pass
#       
#       
#     try :
#       
#           driver.find_element_by_xpath("//*[@id='wepkey1_5g_tr']/td/input").send_keys(str(PresharedKey2g)) 
#                   
#           time.sleep(5)    
#       
#     except :
#           
#           pass
#       
#       
#       
#     try :
#       
#           driver.find_element_by_xpath("//*[@id='pskValue_5g_tr']/td/input").send_keys(str(PresharedKey2g)) 
#                   
#           time.sleep(5)    
#       
#     except :
#           
#           pass
#       
#       
#       
#       
#     try :
#       
#           driver.find_element_by_xpath("//*[@id='password_btn']/tbody/tr/td/input").click()  
#                   
#           time.sleep(5)    
#       
#     except :
#           
#           pass
#       
#       
#     try :
#       
#           driver.find_element_by_xpath("//*[@id='password_btn']/tbody/tr/td/input").click()  
#                   
#           time.sleep(5)    
#       
#     except :
#           
#           pass
#       
#       
# 
#       
#     print 'Connect successfully !!!'
#       
#       
#     time.sleep(80)
#       
#     driver.close()
      
    time.sleep(3)
      
    driver = webdriver.Chrome(chrome_path) 
           
      
    time.sleep(3)
            
    driver.get(DST+"/logout.html")
      
    time.sleep(3)
      
    driver.close()




    

        
    for j in channel_range_text:   
        
        file = open(save_result,'a')
         
        driver = webdriver.Chrome(chrome_path) 
         
     
        time.sleep(3)
                        
          
        driver.get(Basic5g)
        
        time.sleep(3)
         
        try : 
            
             driver.find_element_by_link_text("More Settings").click()
                 
             time.sleep(3)
             driver.find_element_by_link_text("5GHz Wi-Fi Settings").click()
                 
             time.sleep(3)                     
             driver.find_element_by_link_text("Basic Settings").click()
         
        except :
             pass
                 
        time.sleep(3) 
        
        try :
         
            Select(driver.find_element_by_name(str(Channel_ID))).select_by_value(str(j))
        
        except :
            
            pass
         
        try:
  
                    WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                                   'Timed out waiting for PA creation ' + 
                                                   'confirmation popup to appear.')
                
                    alert = driver.switch_to_alert()
                    alert_text = alert.text
                    print alert.text
                    alert.accept()
               
                #    print alert.text
                    print "alert accepted"
                    pass
        except :
                    print "no alert"
                    pass 
         
        
        time.sleep(3)
        
        try :
        
            i = driver.find_element_by_name(str(BW_name))
        
            options = [x for x in i.find_elements_by_tag_name("option")] #this part is cool, because it searches the elements contained inside of select_box and then adds them to the list options if they have the tag name "options"
       
            print options[-1].get_attribute("value")
            
            u =  options[-1].get_attribute("value")
                
            Select(driver.find_element_by_name(str(BW_name))).select_by_value(u)   
        except :
            
            pass
             
             
                 
#              wait = WebDriverWait(driver, 5)
#              wait.until(EC.visibility_of_element_located((By.NAME, "B1")))
#                  
#                  
#              driver.find_element_by_name("B1").click()
             
        time.sleep(3)
             
        el = driver.find_element_by_xpath(str(Appy_ID_1))
    
        webdriver.ActionChains(driver).move_to_element(el).click(el).perform() 
          
         
        time.sleep(5)
         
         
        try : 
         
          el = driver.find_element_by_xpath(str(Appy_ID_2))
    
          webdriver.ActionChains(driver).move_to_element(el).click(el).perform() 
   
         
        except :
          pass   
      
        time.sleep(int(timesleep))
         
         
        time.sleep(3)
         
        driver.close()
         
         
        
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

         
          
   
        
        
        for i in range(1 , 4 , 1):
            
             time.sleep(5) 
        
             test_script = conf.get ('Test_script','script'+str(i))
              
             print '===== 5G '+'Channel ' + str(j) + ' script ' + str(test_script) + ' ======='
              
              
 
                
             
             cmd2 = 'Ping ' + str(DUT_IP) +' -n 5' 
             print cmd2
             pingPopen = subprocess.Popen(args=cmd2, shell=True, stdout=subprocess.PIPE)
             pingstring = pingPopen.stdout.read()
             print pingstring 
             
    
             
             if 'Reply' and 'TTL' in pingstring :
                           
                 
                     print 'Start throughput test !!!'
                     
                     
                     time.sleep(5)
                 
                            
                    
                     os.chdir(chariot_path)
                             
                              
                     print str(test_script)
                     print 'Please wait 1 min 30 secs ....'
                     cmd ='runtst -v '+ str(test_script)+'.tst' 
                     print cmd
                     pingPopen = subprocess.Popen(args= str(cmd), shell=True, stdout=subprocess.PIPE)
                     pingstring = pingPopen.stdout.read()
                     print pingstring
                             
                             
                         
                     cmd2 = 'fmttst '+ '-h ' + str(test_script)+'.tst ' + '> ' + str(test_script) +'.html' 
                     print cmd2
                     p=Popen(cmd2,shell=True,stdin=PIPE)
                     p.stdin.write("y\n")
                     time.sleep(1)
                     

                     try :        
                            
                         driver = webdriver.Chrome(chrome_path)  
                                
                         driver.get(chariot_path+'/'+str(test_script)+'.html')
                                
                         i = driver.find_element_by_xpath("/html/body/table[6]/tbody/tr[2]/td[2]")
                                    
                         print format(i.text)
                     
                     except :
                         
                         pass
                     
             
                     
                 
             else :
                     
                    print 'ping fail !!!!!'
                 
               
             
             
             
             
             
             try :
             
                 format_value = str(format(i.text))
                 
                 format_value =  format_value.replace(",","")
                 
                 format_value = float(format_value)
                             
                 print format_value
                             
                 format_value = round(format_value)
                 
                 format_value = int(format_value)
                             
                 print format_value   
                         
                         
                 file = open(save_result,'a') 
        
                 file.write(' Channel ' + str(j) + '  ' +str(format_value) +'      script ' + str(test_script)+"\n") 
                         
                         
                         
                 try :
                          driver.close()
                 except:
                          pass   
             except :
                 
                 file.write(' Channel '+str(j)+'  ' +'       script ' + str(test_script) + ' Error!!! ' +"\n")  
                 
                 try :
                  driver.close()
                 except:
                  pass   
                 pass   
                  


              
           
                
             try :   
                  for filename in os.listdir(chariot_path):
                    
                    
                    if filename.endswith('WPA2-AES'+'.html'): 
                         pass  
                    elif filename.endswith('WPA2-AES'+'_resp_time.gif'): 
                         pass
                     
                    elif filename.endswith('WPA2-AES'+'_throughput.gif'): 
                         pass
                     
                    elif filename.endswith('WPA2-AES'+'_trans_rate.gif'): 
                         pass 
                     
                      
                    elif filename.endswith("H.html"): 
                         os.chdir(chariot_path)
                         os.rename(filename,str(test_script)+'Channel '+str(j)+'   '+ '5G AC' + '   '+ 'WPA2-AES'+'.html')
                      
                    elif filename.endswith("H_resp_time.gif"):
                             os.chdir(chariot_path)
                             os.rename(filename,str(test_script)+'Channel '+str(j)+'   '+ '5G AC' + '   '+ 'WPA2-AES'+'_resp_time.gif')
                            
                    elif filename.endswith("H_throughput.gif"):
                             os.chdir(chariot_path)
                             os.rename(filename,str(test_script)+'Channel '+str(j)+'   '+ '5G AC' + '   '+'WPA2-AES'+'_throughput.gif')
                          
                    elif filename.endswith("H_trans_rate.gif"):
                             os.chdir(chariot_path)
                             os.rename(filename,str(test_script)+'Channel '+str(j)+'   '+ '5G AC' + '   '+ 'WPA2-AES'+'_trans_rate.gif')
                           
                             
                     
                 
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