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
# from win32gui import GetWindowText, GetForegroundWindow
from subprocess import Popen,PIPE
# from Throughput.Throughput_auto_test_2g import list_Throughput




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




def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    






def Encryption_Throughput(EncryptionType2g_id= '',EncryptionType2g = '',Encryption= '',Authentication2g_id ='', Encryption2g_id = '' , KeyFormat2g_id = '' , PresharedKey2g_id = '' ,Account_password = '' ,DUT_IP = '',ssid='',test_script='',Authentication2g ='', Encryption2g = '' , KeyFormat2g = '' , PresharedKey2g = '' ,BW_MODE= '' , BW_width=''):
    
    reload(sys)
#     sys.setdefaultencoding('utf8')
         
    conf = RawConfigParser()
    conf.read('config.ini')
    
    

     
    
    
    DUT_IP = DUT_IP 
    
    Account_password = Account_password
    

    
    
    DST = 'http://' + Account_password + DUT_IP
    
    Basic2g = 'http://' + Account_password + DUT_IP + str(Basic2g_link)
    
    Basic5g = 'http://' + Account_password + DUT_IP + str(Basic5g_link)
    
    entry2g = 'http://' + Account_password + DUT_IP + str(entry2g_link)
    
    entry5g = 'http://' + Account_password + DUT_IP + str(entry5g_link)
    

    


    
    Authentication2g = Authentication2g
    
    Encryption2g = Encryption2g     
    
    KeyFormat2g = KeyFormat2g 
    
    PresharedKey2g = PresharedKey2g 
    
    
    Authentication2g_id = Authentication2g_id
    
    Encryption2g_id = Encryption2g_id     
    
    KeyFormat2g_id = KeyFormat2g_id 
    
    PresharedKey2g_id = PresharedKey2g_id 
    
    
 
    
    EncryptionType2g = EncryptionType2g 
    
    
    
    BW_MODE = BW_MODE
    
    BW_width = BW_width   
    
    test_script = test_script   
    
    ssid2g = ssid
    
    Encryption = Encryption


    
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
        
        
            
#     if Authentication2g or Encryption2g  == 'Disable' :
#           print 'Yes ! disable !'
#           Authentication2g = Authentication2g.replace('Disable','None')
#           Encryption2g = Encryption2g.replace('Disable','None')
#           print  Authentication2g
#           print  Encryption2g
#           
#     else :
#         
#         pass 
    
    securitys = ["Open","WEP","WPA"]
    
    names = ["0","1","2"]      
    
    
    list_security = [] 
    
    for name, security in zip(names,securitys):
        
        print name,security
        list_security.append(str(name+security))
    
    print list_security
     
    print  Authentication2g
    
    print  Encryption2g    
    
    try :
     for x in list_security :
        
        if str(Authentication2g) in str(x) :
            
            print x
            
            u = x
    
     print str(u) 
    
    except :
     pass   
        

  
    time.sleep(3)

    
    
    
    
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
         
 
    
    print channel_range_text
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

        
    for j in channel_range_text: 
#         
         time.sleep(3) 
         
         print j
               
         file = open(save_result,'a')  
         
                        
         driver = webdriver.Chrome(chrome_path) 
              
       
         time.sleep(5)
               
         driver.get(Basic2g)
          
   
         time.sleep(4)
              
         try :
              
          driver.find_element_by_name(str(SSID_name)).clear()
          time.sleep(4)
          driver.find_element_by_name(str(SSID_name)).send_keys(str(ssid2g))
           
          time.sleep(4)
           
         except:
           pass   
 
         try :
          
          Select(driver.find_element_by_name(str(Band_name))).select_by_visible_text(str(BW_MODE))
           
           
          time.sleep(2)
          
         except:
          pass     
 
         try :
          
          Select(driver.find_element_by_name(str(Channel_ID))).select_by_value(str(j))
           
          time.sleep(2)
          
         except :
          pass    
 
         try :
          
             chan_band_width = driver.find_element_by_name(str(BW_name))
              
             print str(format(chan_band_width.text))
         
             chan_band_width = re.findall('\d{,2}\s[a-zA-Z]{,3}',str(format(chan_band_width.text)))
               
             print chan_band_width
              
             print chan_band_width[1]
              
             if '40' in str(BW_width):
               
              try :
               Select(driver.find_element_by_name(str(BW_name))).select_by_value('HT40')   
              except :
               pass   
              try :
               Select(driver.find_element_by_name(str(BW_name))).select_by_value('VHT40')   
              except :
               pass 
              
             elif '20' in str(BW_width):
              
              try :
               Select(driver.find_element_by_name(str(BW_name))).select_by_value('HT20')   
              except :
               pass   
            
              try :
               Select(driver.find_element_by_name(str(BW_name))).select_by_value('VHT20')   
              except :
               pass  
            
              try :
               Select(driver.find_element_by_name(str(BW_name))).select_by_value('20')   
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
 
#          try : 
#              
#               el = driver.find_element_by_xpath(str(Appy_ID_2))
#         
#               webdriver.ActionChains(driver).move_to_element(el).click(el).perform() 
#               
#           
#              
#          except :
#               pass    
#              
#          time.sleep(int(timesleep))
#          
#          driver.close()
# 
#          driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe") 
#          
#          time.sleep(5) 
#          
#          driver.get(DST)
#         
#          time.sleep(7)
          
         time.sleep(int(timesleep))
           
         driver.close()
  
         driver = webdriver.Chrome(chrome_path) 
           
         time.sleep(5) 
           
         driver.get(entry2g)
          
         time.sleep(7)
 
 
 
  
    
          
         print  Authentication2g   
          
         print Encryption2g
          
         try: 
          
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
              
              
             Encryptionmode2g = conf.get('Encryption_Throughput_2g','WPA_Encryptionmode')
              
             driver.find_element_by_xpath(str(Encryptionmode2g)).click()
                         
             time.sleep(1)
         except :
             pass
          
          
          
          
 
         try :
             driver.find_element_by_xpath(str(EncryptionType2g)).click()
                             
             time.sleep(1)
         except :
             pass
          
          
          
         try :
              
              
             Select(driver.find_element_by_name(str(Encryption2g_id))).select_by_value(str(Encryption2g))
         
                         
             time.sleep(1)
         except :
              
             pass
          
           
          
         try :    
                     
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
         
         
         driver = webdriver.Chrome(chrome_path) 
           
           
         driver.get(BridegeMode)
           
         time.sleep(40)
           
         try :
         
             for p in range(1,25,1):
                 
               
                 i = driver.find_element_by_xpath("//*[@id='table_11g']/tbody/tr["+str(p)+"]/td[3]")
                                                  
                                                  
                 print format(i.text)   
                 
                 g = format(i.text) 
                 
                             
                 
                 if g == str(ssid2g) :
                     
                     print 'find !!!'
                     
                     print p
                     
                     
                     driver.find_element_by_xpath("//*[@id='table_11g']/tbody/tr["+str(p)+"]/td[1]/input").click()
                     
                     time.sleep(5)
                     
              
                     
                     break
                     
                 else :
                     
                     print 'Not find !!!!'
                     
                     pass    
         
         except :
             
             pass
                 
         try :
         
             driver.find_element_by_xpath("//*[@id='next_but']/td/img[2]").click()  
                     
             time.sleep(5)  
             
         except :
             
             pass
               
         
         try :
         
         
             WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                           'Timed out waiting for PA creation ' + 
                                           'confirmation popup to appear.')
        
             alert = driver.switch_to_alert()
             alert_text = alert.text
             print alert.text
             
             h = alert.text
             
         except :
             
             pass    
         
         time.sleep(5)
         
         try :
         
             if h == 'Please select one entry to connect!' :
                 
                 print 'Repeat scan !!!'
                 
                 driver.close()
                 
                 driver = webdriver.Chrome(chrome_path) 
                   
                   
                 driver.get(BridegeMode)
                   
                 time.sleep(40)
                 
           
                 
                 for p in range(1,25,1):
                     
        
                   
                     i = driver.find_element_by_xpath("//*[@id='table_11g']/tbody/tr["+str(p)+"]/td[3]")
                                                
                     print format(i.text)   
                     
                     g = format(i.text) 
                     
                                 
                     
                     if g == str(ssid2g) :
                         
                         print 'find !!!'
                         
                         print p
                         
                 
                         
                         driver.find_element_by_xpath("//*[@id='table_11g']/tbody/tr["+str(p)+"]/td[1]/input").click()
                         
                         time.sleep(5)
                         
                  
                         
                         break
                         
                     else :
                         
                         print 'Not find !!!!'
                         
                         pass    
                     
             else :
                 
                 print 'scan pass !!'
                 
                 pass    
         
         except :
             
             pass
         
         
             
         try :
         
             driver.find_element_by_xpath("//*[@id='next_but']/td/img[2]").click()  
                     
             time.sleep(5)    
         
         except :
             
             pass
         
         
         try :
         
             driver.find_element_by_xpath("//*[@id='wepkey1_tr']/td/input").send_keys(str(PresharedKey2g)) 
                     
             time.sleep(5)    
         
         except :
             
             pass
         
         
         
         try :
         
             driver.find_element_by_xpath("//*[@id='pskValue_tr']/td/input").send_keys(str(PresharedKey2g)) 
                     
             time.sleep(5)    
         
         except :
             
             pass
         
         
         
         
         try :
         
             driver.find_element_by_xpath("//*[@id='password_btn']/tbody/tr/td/input").click()  
                     
             time.sleep(5)    
         
         except :
             
             pass
         
         
         try :
         
             driver.find_element_by_xpath("//*[@id='password_btn']/tbody/tr/td/input").click()  
                     
             time.sleep(5)    
         
         except :
             
             pass
         
         
         
         
#          try :
#          
#              driver.find_element_by_xpath("//*[@id='pskValue_tr']/td/input").send_keys(str(PresharedKey2g)) 
#                      
#              time.sleep(5)    
#          
#          except :
#              
#              pass
#          
#          
#          
#          
#          try :
#          
#              driver.find_element_by_xpath("//*[@id='password_btn']/tbody/tr/td/input").click()  
#                      
#              time.sleep(5)    
#          
#          except :
#              
#              pass
         
         
         
         
         
         
         print 'Connect successfully !!!'
         
         
         time.sleep(80)
         
         driver.close()
         
         time.sleep(3)
         
         driver = webdriver.Chrome(chrome_path) 
              
         
         time.sleep(3)
               
         driver.get(DST+"/logout.html")
         
         time.sleep(3)
         
         driver.close()
 
         
         
         
         
         
         
         
#          
#          driver.get(DST)    
# 
#          time.sleep(3)
#         
#          driver.find_element_by_link_text("More Settings").click()
#              
#          time.sleep(3)
#          driver.find_element_by_id("menu030000").click()
#              
#          time.sleep(3)                      
#          driver.find_element_by_css_selector("#sub030400 > a").click()
#                
#     
#          time.sleep(3)
#         
#         
#          if not driver.find_element_by_name("enabled").is_selected() :
#              
#             driver.find_element_by_name("enabled").click()
#          
#          else :
#             pass   
#      
#      
#         
#          try :
#         
#           driver.find_element_by_name("input").click()
#         
#           time.sleep(int(timesleep))
#          except :
#           pass  
#      
#         
#          driver.switch_to_window(driver.window_handles[-1])
#         
#          time.sleep(3)
#        
#         
#          driver.find_element_by_xpath("//*[@id='AddTbl']/tbody/tr[2]/td[1]/input").click()
#         
#          time.sleep(3)
#        
#      
#      
#         
#          driver.find_element_by_id("done").click()
#         
#          time.sleep(3)
#     
#         
#          driver.switch_to_window(driver.window_handles[0])
#         
#          time.sleep(3)
#         
#              
#         
#          try :
#               
#           SSID_name = conf.get('Bridge_ip','Bridge_SSID')
#               
#                  
#           driver.find_element_by_name(str(SSID_name)).clear()
#           time.sleep(2)
#           driver.find_element_by_name(str(SSID_name)).send_keys(str(ssid2g))
#               
#           time.sleep(2)
#       
#          except :
#           pass 
#       
#         
#         
#          try :
#               
#           Security = conf.get('Bridge_ip','Security')
#          
#           PresharedKey2g = conf.get('Encryption2g','Pre-shared Key5')
#               
#                  
#           driver.find_element_by_name(str(Security)).clear()
#           time.sleep(2)
#           driver.find_element_by_name(str(Security)).send_keys(str(PresharedKey2g))
#               
#           time.sleep(2)
#       
#          except :
#           pass 
#       
#       
#         
#       
#         
#          try :
#               
#           Bridge_Manual_IP = conf.get('Bridge_ip','Bridge_Manual_IP')
#               
#                  
#           driver.find_element_by_xpath(str(Bridge_Manual_IP)).click()
#     
#               
#           time.sleep(2)
#       
#          except :
#            pass  
#       
#       
#       
#       
#         
#          try :
#               
#           IP_name = conf.get('Bridge_ip','IP_name')
#           Bridge_IP = conf.get ('Bridge_ip','Bridge_IP')    
#                  
#           driver.find_element_by_name(str(IP_name)).clear()
#           time.sleep(2)
#           driver.find_element_by_name(str(IP_name)).send_keys(str(Bridge_IP))
#               
#           time.sleep(2)
#       
#          except :
#           pass 
#         
#       
#         
#          try :
#               
#           mask = conf.get('Bridge_ip','mask')
#          
#           mask_value = conf.get('Bridge_ip','mask_value')
#               
#                  
#           driver.find_element_by_name(str(mask)).clear()
#           time.sleep(2)
#           driver.find_element_by_name(str(mask)).send_keys(str(mask_value))
#               
#           time.sleep(2)
#       
#          except :
#           pass 
#           
#         
#         
#          try :
#               
#           Gateway = conf.get('Bridge_ip','Gateway')
#                  
#                  
#           driver.find_element_by_name(str(Gateway)).clear()
#           time.sleep(2)
#           driver.find_element_by_name(str(Gateway)).send_keys(str(DUT_IP))
#               
#           time.sleep(2)
#       
#          except :
#           pass 
#         
#         
#         
#          try :    
#             driver.switch_to_default_content()
#             time.sleep(3)
#             driver.find_element_by_css_selector("div.hover_icon_container > a > img").click()
#             time.sleep(3)
#             driver.find_element_by_css_selector("img").click()  
#             time.sleep(3)   
#                
#          except :
#              pass          
#                
#                
#                
#          time.sleep(int(timesleep)) 
# 
#          
#          
#          
#          
#       
#          
#              
         
               
     
         
         cmd2 = 'Ping ' + str(DUT_IP) +' -n 5' 
         print cmd2
         pingPopen = subprocess.Popen(args=cmd2, shell=True, stdout=subprocess.PIPE)
         pingstring = pingPopen.stdout.read()
         print pingstring 
         
         time.sleep(3)
       
         if 'Reply' and 'TTL' in pingstring :
           
          for i in range(1 , 4 , 1):  
         
             time.sleep(2) 
             
             
             print test_script
             
             if 'S'  in test_script :
              
              script_BA = ['TXRX_S','TX_S','RX_S']
          
              test_script = script_BA[i-1]
              
             elif 'L'  in test_script :
              
              script_BA = ['TXRX_L','TX_L','RX_L']
          
              test_script = script_BA[i-1] 
              
             
             elif 'H' in test_script :
                 
              script = ['TXRX_H','TX_H','RX_H']   
                 
              test_script = script[i-1]    
             
             else :
              
              script = ['TXRX_H','TX_H','RX_H']
                 
              test_script = script[i-1]    
                       
             try :
                 
             
                 
#                  file.write(str(BW_MODE) + ' BW='+str(BW_width)+ ' ' + str(Encryption)  + ' Channel' + str(channel2g_a)  +' '+str(test_script)+"\n")

                 
                 
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
                 time.sleep(5)
                 

                 
                         
                        
                 driver = webdriver.Chrome(chrome_path)  
                        
                 driver.get(chariot_path+'/'+str(test_script)+'.html')
                        
                 i = driver.find_element_by_xpath("/html/body/table[6]/tbody/tr[2]/td[2]")
                            
                 print format(i.text)
                 
                 
                 
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
                 
                 
                  
#                  file.write(str(format_value) +"\n")
      
                 file.write(str(format_value)+ '    ' + str(BW_MODE) + ' BW='+str(BW_width)+ ' ' + str(Encryption)  + ' Channel' + str(channel2g_a)  +' '+str(test_script)+"\n")
                 
                   
                 driver.close()
                 try :   
                  for filename in os.listdir(chariot_path):
                    
                    
                    if filename.endswith(str(Encryption)+'.html'): 
                         pass  
                    elif filename.endswith(str(Encryption)+'_resp_time.gif'): 
                         pass
                     
                    elif filename.endswith(str(Encryption)+'_throughput.gif'): 
                         pass
                     
                    elif filename.endswith(str(Encryption)+'_trans_rate.gif'): 
                         pass 
                     
                      
                    elif filename.endswith("S.html"): 
                         os.chdir(chariot_path)
                         os.rename(filename,str(test_script)+'Channel '+str(j)+'   '+ '2.4G BGN' +'    ' + str(BW_MODE)+ '   '+ str(Encryption)+'.html')
                      
                    elif filename.endswith("S_resp_time.gif"):
                             os.chdir(chariot_path)
                             os.rename(filename,str(test_script)+'Channel '+str(j)+'   '+ '2.4G BGN' + '    ' + str(BW_MODE)+'   '+ str(Encryption)+'_resp_time.gif')
                            
                    elif filename.endswith("S_throughput.gif"):
                             os.chdir(chariot_path)
                             os.rename(filename,str(test_script)+'Channel '+str(j)+'   '+ '2.4G BGN' + '    ' + str(BW_MODE)+ '   '+ str(Encryption)+'_throughput.gif')
                          
                    elif filename.endswith("S_trans_rate.gif"):
                             os.chdir(chariot_path)
                             os.rename(filename,str(test_script)+'Channel '+str(j)+'   '+ '2.4G BGN' + '    ' + str(BW_MODE)+ '   '+ str(Encryption)+'_trans_rate.gif')
                           
                             
                     
                 
                 except :
                     
                     pass
                 
                 
                 
                 
                 
                 try :   
                  for filename in os.listdir(chariot_path):
                    
                    
                    if filename.endswith(str(Encryption)+'.html'): 
                         pass  
                    elif filename.endswith(str(Encryption)+'_resp_time.gif'): 
                         pass
                     
                    elif filename.endswith(str(Encryption)+'_throughput.gif'): 
                         pass
                     
                    elif filename.endswith(str(Encryption)+'_trans_rate.gif'): 
                         pass 
                     
                      
                    elif filename.endswith("H.html"): 
                         os.chdir(chariot_path)
                         os.rename(filename,str(test_script)+'Channel '+str(j)+'   '+ '2.4G BGN' + '   '+ str(Encryption)+'.html')
                      
                    elif filename.endswith("H_resp_time.gif"):
                             os.chdir(chariot_path)
                             os.rename(filename,str(test_script)+'Channel '+str(j)+'   '+ '2.4G BGN' + '   '+ str(Encryption)+'_resp_time.gif')
                            
                    elif filename.endswith("H_throughput.gif"):
                             os.chdir(chariot_path)
                             os.rename(filename,str(test_script)+'Channel '+str(j)+'   '+ '2.4G BGN' + '   '+ str(Encryption)+'_throughput.gif')
                          
                    elif filename.endswith("H_trans_rate.gif"):
                             os.chdir(chariot_path)
                             os.rename(filename,str(test_script)+'Channel '+str(j)+'   '+ '2.4G BGN' + '   '+ str(Encryption)+'_trans_rate.gif')
                           
                             
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
                
                
                
                
                  except :
                     
                     pass   
                         
                 except :
                     
                     pass
       
                  
                 
             
             
             except :
                 print 'Channel or security is fail !!!!!'
                 file.write('Error'+ '    ' + str(BW_MODE) + ' BW='+str(BW_width)+ ' ' + str(Encryption)  + ' Channel' + str(channel2g_a)  +' '+str(test_script)+"\n")
  
                 list_Throughput.append('Error') 
                 try :
                  driver.close()
                 except :
                  pass    
                 pass
             
             
         
         else :
             file.write('Error'+ '    ' + str(BW_MODE) + ' BW='+str(BW_width)+ ' ' + str(Encryption)  + ' Channel' + str(channel2g_a)  +' '+str(test_script)+"\n")
  
             print 'Connect to Router fail !!!!!'
         
         
         
         
    print list_Throughput     
    

  
    
  
        
        
        
if __name__ == '__main__':
    
    
    
        encryptions = ["Open","WEP_64","WEP_128","WPA-Personal_TKIP","WPA2-Personal_AES"]
    
        reload(sys)
#         sys.setdefaultencoding('utf8')
         
        conf = RawConfigParser()
        conf.read('config.ini')
        
        DUT_IP = conf.get ('ip','Dut_ip1')
        
        Account_password = conf.get ('Accountpassword','Account_password1')
       
        BW_mode1_2g = conf.get('Band_width','2.4G_Mode11')
        
        BW_mode2_2g = conf.get('Band_width','2.4G_Mode12')
        
        BW_mode3_2g = conf.get('Band_width','2.4G_Mode13')
        
        BW_mode1_5g = conf.get('Band_width','5G_Mode1')
        
        BW_mode2_5g = conf.get('Band_width','5G_Mode2')
        
        BW_mode3_5g = conf.get('Band_width','5G_Mode3')
    
        
        Bandwidth1_2g = conf.get('Band_width','2.4G_BW1')
        
        Bandwidth2_2g = conf.get('Band_width','2.4G_BW2')
    
        Bandwidth1_5g = conf.get('Band_width','5G_BW1')
        
        Bandwidth2_5g = conf.get('Band_width','5G_BW2')
        
        ssid2g_1 = conf.get ('SSID2g','SSID1')
    
        ssid2g_2 = conf.get ('SSID2g','SSID2')
    
        ssid2g_3 = conf.get ('SSID2g','SSID3')
    
        ssid2g_4 = conf.get ('SSID2g','SSID4')
    
        ssid2g_5 = conf.get ('SSID2g','SSID5')
        
        
        Authentication2g_1 = conf.get ('Encryption_Throughput_2g','Authentication1')

        Encryption2g_1 = conf.get ('Encryption_Throughput_2g','Encryption1')

        KeyFormat2g_1 = conf.get ('Encryption_Throughput_2g','Key Format1')

        PresharedKey2g_1 = conf.get ('Encryption_Throughput_2g','Pre-shared Key1')
        
        
        Authentication2g_1_id = conf.get ('Encryption_Throughput_2g','Disable_Mode')

        Encryption2g_1_id = conf.get ('Encryption_Throughput_2g','Disable_Mode')

        KeyFormat2g_1_id = conf.get ('Encryption_Throughput_2g','Disable_Mode')

        PresharedKey2g_1_id = conf.get ('Encryption_Throughput_2g','Disable_Mode')
        
        
        
 
        
        Authentication2g_2 = conf.get ('Encryption_Throughput_2g','Authentication2')

        Encryption2g_2 = conf.get ('Encryption_Throughput_2g','KeyLength2')

        KeyFormat2g_2 = conf.get ('Encryption_Throughput_2g','Key Format2')

        PresharedKey2g_2 = conf.get ('Encryption_Throughput_2g','Pre-shared Key2')
        
        
        Authentication2g_2_id = conf.get ('Encryption_Throughput_2g','WEP_Mode')

        Encryption2g_2_id = conf.get ('Encryption_Throughput_2g','WEP_Keylength')

        KeyFormat2g_2_id = conf.get ('Encryption_Throughput_2g','WEP_Keyformat')

        PresharedKey2g_2_id = conf.get ('Encryption_Throughput_2g','WEP_Preshared64key')
        
        
        
        Authentication2g_3 = conf.get ('Encryption_Throughput_2g','Authentication3')

        Encryption2g_3 = conf.get ('Encryption_Throughput_2g','KeyLength3')

        KeyFormat2g_3 = conf.get ('Encryption_Throughput_2g','Key Format3')

        PresharedKey2g_3 = conf.get ('Encryption_Throughput_2g','Pre-shared Key3')
        
        
        Authentication2g_3_id = conf.get ('Encryption_Throughput_2g','WEP_Mode')

        Encryption2g_3_id = conf.get ('Encryption_Throughput_2g','WEP_Keylength')

        KeyFormat2g_3_id = conf.get ('Encryption_Throughput_2g','WEP_Keyformat')

        PresharedKey2g_3_id = conf.get ('Encryption_Throughput_2g','WEP_Preshared128key')
        
        EncryptionType2g_3 = conf.get ('Encryption_Throughput_2g','Type3')
        
        
        
        
        
        Authentication2g_4 = conf.get ('Encryption_Throughput_2g','Authentication4')

        Encryption2g_4 = conf.get ('Encryption_Throughput_2g','Encryption4')

        KeyFormat2g_4 = conf.get ('Encryption_Throughput_2g','Key Format4')

        PresharedKey2g_4 = conf.get ('Encryption_Throughput_2g','Pre-shared Key4')
        
        EncryptionType2g_4 = conf.get ('Encryption_Throughput_2g','Type4')
        
        
        Authentication2g_4_id = conf.get ('Encryption_Throughput_2g','WPA_Mode')

        Encryption2g_4_id = conf.get ('Encryption_Throughput_2g','WPA_Encryptionmode')

        KeyFormat2g_4_id = conf.get ('Encryption_Throughput_2g','WPA_psk')

        PresharedKey2g_4_id = conf.get ('Encryption_Throughput_2g','WPA_key')
        
        EncryptionType2g_4_id = conf.get('Encryption_Throughput_2g','WPA_EncryptionType')

       
        
        
        
        Authentication2g_5 = conf.get ('Encryption_Throughput_2g','Authentication5')

        Encryption2g_5 = conf.get ('Encryption_Throughput_2g','Encryption5')

        KeyFormat2g_5 = conf.get ('Encryption_Throughput_2g','Key Format5')

        PresharedKey2g_5 = conf.get ('Encryption_Throughput_2g','Pre-shared Key5')
        
        EncryptionType2g_5 = conf.get ('Encryption_Throughput_2g','Type5')
        
        
        
        Authentication2g_5_id = conf.get ('Encryption_Throughput_2g','WPA_Mode')

        Encryption2g_5_id = conf.get ('Encryption_Throughput_2g','WPA_Encryptionmode')

        KeyFormat2g_5_id = conf.get ('Encryption_Throughput_2g','WPA_psk')

        PresharedKey2g_5_id = conf.get ('Encryption_Throughput_2g','WPA_key')
        
        EncryptionType2g_5_id = conf.get('Encryption_Throughput_2g','WPA_EncryptionType')
        
        
        
        
        model_name = conf.get('Model','name')
    
        model_fw = conf.get('Model','FW')
        
        timesleep = conf.get ('2.4G_Time_sleep','sleep_time')
        
        channel2g_rangea = conf.get ('Security_Channel','channel2g_rangea')
    
        channel2g_rangeb = conf.get ('Security_Channel','channel2g_rangeb')
    
        channel5g_rangea = conf.get ('Security_Channel','channel5g_rangea')
    
        channel5g_rangeb = conf.get ('Security_Channel','channel5g_rangeb')
        
            
        channel2g_a = conf.get ('Security_Channel','channel2g_rangea')

        channel2g_b = conf.get ('Security_Channel','channel2g_rangeb')
        
        
        model_name = conf.get('Model','name')
    
        model_fw = conf.get('Model','FW')
    
        channel_range = conf.get('Security_Channel','channel2g')
            
        LAN_name = conf.get ('LAN','name')    
        
        
        save_profile = os.getcwd() + '//Profile'
    
        save_result = os.getcwd() +'//Result//Throughput2g.txt'
        
        chrome_path = os.getcwd() + '//chromedriver_win32//chromedriver.exe'
        
        chariot_path = os.getcwd() + '/Chariot_tst'
        
        
       
        test_script1 = conf.get ('Security_Test_script','script1')
        test_script2 = conf.get ('Security_Test_script','script2')
        
        test_script3 = conf.get ('Security_Test_script','script3')
        
        test_script1_BA = conf.get ('Security_Test_script','script1_BA')
        test_script2_BA = conf.get ('Security_Test_script','script2_BA')
        
        test_script3_BA = conf.get ('Security_Test_script','script3_BA')
        
        
        
        
        Basic2g_link = conf.get ('Basic_link','Basic2g')
    
        Basic5g_link = conf.get ('Basic_link','Basic5g')
        
        entry2g_link = conf.get ('Encryption_link','entry2g')
        
        entry5g_link = conf.get ('Encryption_link','entry5g')
        
        
        
        
        Basic2g = 'http://' + Account_password + DUT_IP + str(Basic2g_link)
        
        Basic5g = 'http://' + Account_password + DUT_IP + str(Basic5g_link)
        
        entry2g = 'http://' + Account_password + DUT_IP + str(entry2g_link)
        
        entry5g = 'http://' + Account_password + DUT_IP + str(entry5g_link)
        
        
        Bridge_IP = conf.get ('Bridge_ip','Bridge_IP')
    
        Bridege_link = conf.get ('Bridge_link','Bridge_mode')
    
        BridegeMode = 'http://' + Account_password + Bridge_IP + str(Bridege_link)
            
            
        
        
        Channel_ID = conf.get ('Channel_ID','channel2g')
        
        
        Appy_ID_1 = conf.get ('Appy_ID','apply1_2g')
    
        Appy_ID_2 = conf.get ('Appy_ID','apply2_2g')
            
        SSID_name = conf.get ('SSID2g','SSID_name')       
        
        Band_name = conf.get ('Band_width','BW_2G_ID')
        
        BW_name = conf.get('Band_width','Band_Width_2G_ID')
        
        WLAN_name = conf.get ('WLAN','name')
        
        Time = conf.get('Security_Test_script','Time')
        
        
        
        file = open(save_result,'a') 
    
        file.write(str(model_name)+'  '+ str(model_fw)+"\n"+"\n")

        file.write('Encryption Throughput'+"\n"+"\n")

        file.write('Start time :      '+str(datetime.now())+"\n"+"\n") 
        

        file.write("\n"+"\n")
        
        file.close()
        
        
        list_Throughput = []
        
        
#         try :
#             for filename in os.listdir(save_profile):
# #                 print filename
# #                 match_name = re.findall('\d[TR]{,1}[Xx]{,1}',filename) 
# #                 print match_name
#                 
#                 os.chdir(save_profile)
#                 if filename.endswith(".xml") : 
#                    print filename
#                    
#                    os.system('netsh wlan add profile filename='+filename)
#                    
#   
#                    
#         except :
#         
#             pass   
        
    
              
        Encryption_Throughput(Encryption= encryptions[0],Authentication2g_id =Authentication2g_1_id, Encryption2g_id = Encryption2g_1_id , KeyFormat2g_id = KeyFormat2g_1_id , PresharedKey2g_id = PresharedKey2g_1_id ,Account_password = Account_password , DUT_IP = DUT_IP , ssid=ssid2g_1,test_script = test_script1_BA,Authentication2g =Authentication2g_1, Encryption2g = Encryption2g_1 , KeyFormat2g = KeyFormat2g_1 , PresharedKey2g = PresharedKey2g_1 ,BW_MODE= BW_mode1_2g , BW_width=Bandwidth1_2g,EncryptionType2g_id= EncryptionType2g_4_id,EncryptionType2g =EncryptionType2g_4)
        Encryption_Throughput(Encryption= encryptions[1],Authentication2g_id =Authentication2g_2_id, Encryption2g_id = Encryption2g_2_id , KeyFormat2g_id = KeyFormat2g_2_id , PresharedKey2g_id = PresharedKey2g_2_id ,Account_password = Account_password , DUT_IP = DUT_IP , ssid=ssid2g_2,test_script = test_script1_BA,Authentication2g =Authentication2g_2, Encryption2g = Encryption2g_2 , KeyFormat2g = KeyFormat2g_2 , PresharedKey2g = PresharedKey2g_2 ,BW_MODE= BW_mode1_2g , BW_width=Bandwidth1_2g,EncryptionType2g_id= EncryptionType2g_4_id,EncryptionType2g =EncryptionType2g_3)
        Encryption_Throughput(Encryption= encryptions[2],Authentication2g_id =Authentication2g_3_id, Encryption2g_id = Encryption2g_3_id , KeyFormat2g_id = KeyFormat2g_3_id , PresharedKey2g_id = PresharedKey2g_3_id ,Account_password = Account_password , DUT_IP = DUT_IP , ssid=ssid2g_3,test_script = test_script1_BA,Authentication2g =Authentication2g_3, Encryption2g = Encryption2g_3 , KeyFormat2g = KeyFormat2g_3 , PresharedKey2g = PresharedKey2g_3 ,BW_MODE= BW_mode1_2g , BW_width=Bandwidth1_2g,EncryptionType2g_id= EncryptionType2g_4_id,EncryptionType2g =EncryptionType2g_3)
        Encryption_Throughput(Encryption= encryptions[3],Authentication2g_id =Authentication2g_4_id, Encryption2g_id = Encryption2g_4_id , KeyFormat2g_id = KeyFormat2g_4_id , PresharedKey2g_id = PresharedKey2g_4_id ,Account_password = Account_password , DUT_IP = DUT_IP , ssid=ssid2g_4,test_script = test_script1_BA,Authentication2g =Authentication2g_4, Encryption2g = Encryption2g_4 , KeyFormat2g = KeyFormat2g_4 , PresharedKey2g = PresharedKey2g_4 ,BW_MODE= BW_mode1_2g , BW_width=Bandwidth1_2g,EncryptionType2g_id= EncryptionType2g_4_id,EncryptionType2g =EncryptionType2g_4)
        Encryption_Throughput(Encryption= encryptions[4],Authentication2g_id =Authentication2g_5_id, Encryption2g_id = Encryption2g_5_id , KeyFormat2g_id = KeyFormat2g_5_id , PresharedKey2g_id = PresharedKey2g_5_id ,Account_password = Account_password , DUT_IP = DUT_IP , ssid=ssid2g_5,test_script = test_script1_BA,Authentication2g =Authentication2g_5, Encryption2g = Encryption2g_5 , KeyFormat2g = KeyFormat2g_5 , PresharedKey2g = PresharedKey2g_5 ,BW_MODE= BW_mode1_2g , BW_width=Bandwidth1_2g,EncryptionType2g_id= EncryptionType2g_5_id,EncryptionType2g =EncryptionType2g_5)
           
           
           
    
        list_Throughput = []
      
        Encryption_Throughput(Encryption= encryptions[0],Authentication2g_id =Authentication2g_1_id, Encryption2g_id = Encryption2g_1_id , KeyFormat2g_id = KeyFormat2g_1_id , PresharedKey2g_id = PresharedKey2g_1_id ,Account_password = Account_password , DUT_IP = DUT_IP , ssid=ssid2g_1,test_script = test_script1,Authentication2g =Authentication2g_1, Encryption2g = Encryption2g_1 , KeyFormat2g = KeyFormat2g_1 , PresharedKey2g = PresharedKey2g_1 ,BW_MODE= BW_mode2_2g , BW_width=Bandwidth1_2g,EncryptionType2g_id= EncryptionType2g_4_id,EncryptionType2g =EncryptionType2g_4)
        Encryption_Throughput(Encryption= encryptions[1],Authentication2g_id =Authentication2g_2_id, Encryption2g_id = Encryption2g_2_id , KeyFormat2g_id = KeyFormat2g_2_id , PresharedKey2g_id = PresharedKey2g_2_id ,Account_password = Account_password , DUT_IP = DUT_IP , ssid=ssid2g_2,test_script = test_script1_BA,Authentication2g =Authentication2g_2, Encryption2g = Encryption2g_2 , KeyFormat2g = KeyFormat2g_2 , PresharedKey2g = PresharedKey2g_2 ,BW_MODE= BW_mode2_2g , BW_width=Bandwidth1_2g,EncryptionType2g_id= EncryptionType2g_4_id,EncryptionType2g =EncryptionType2g_3)
        Encryption_Throughput(Encryption= encryptions[2],Authentication2g_id =Authentication2g_3_id, Encryption2g_id = Encryption2g_3_id , KeyFormat2g_id = KeyFormat2g_3_id , PresharedKey2g_id = PresharedKey2g_3_id ,Account_password = Account_password , DUT_IP = DUT_IP , ssid=ssid2g_3,test_script = test_script1_BA,Authentication2g =Authentication2g_3, Encryption2g = Encryption2g_3 , KeyFormat2g = KeyFormat2g_3 , PresharedKey2g = PresharedKey2g_3 ,BW_MODE= BW_mode2_2g , BW_width=Bandwidth1_2g,EncryptionType2g_id= EncryptionType2g_4_id,EncryptionType2g =EncryptionType2g_3)
        Encryption_Throughput(Encryption= encryptions[3],Authentication2g_id =Authentication2g_4_id, Encryption2g_id = Encryption2g_4_id , KeyFormat2g_id = KeyFormat2g_4_id , PresharedKey2g_id = PresharedKey2g_4_id ,Account_password = Account_password , DUT_IP = DUT_IP , ssid=ssid2g_4,test_script = test_script1_BA,Authentication2g =Authentication2g_4, Encryption2g = Encryption2g_4 , KeyFormat2g = KeyFormat2g_4 , PresharedKey2g = PresharedKey2g_4 ,BW_MODE= BW_mode2_2g , BW_width=Bandwidth1_2g,EncryptionType2g_id= EncryptionType2g_4_id,EncryptionType2g =EncryptionType2g_4)
        Encryption_Throughput(Encryption= encryptions[4],Authentication2g_id =Authentication2g_5_id, Encryption2g_id = Encryption2g_5_id , KeyFormat2g_id = KeyFormat2g_5_id , PresharedKey2g_id = PresharedKey2g_5_id ,Account_password = Account_password , DUT_IP = DUT_IP , ssid=ssid2g_5,test_script = test_script1,Authentication2g =Authentication2g_5, Encryption2g = Encryption2g_5 , KeyFormat2g = KeyFormat2g_5 , PresharedKey2g = PresharedKey2g_5 ,BW_MODE= BW_mode2_2g , BW_width=Bandwidth1_2g,EncryptionType2g_id= EncryptionType2g_4_id,EncryptionType2g =EncryptionType2g_5)
           

           
         
        list_Throughput = [] 
            
        
        Encryption_Throughput(Encryption= encryptions[0],Authentication2g_id =Authentication2g_1_id, Encryption2g_id = Encryption2g_1_id , KeyFormat2g_id = KeyFormat2g_1_id , PresharedKey2g_id = PresharedKey2g_1_id ,Account_password = Account_password , DUT_IP = DUT_IP , ssid=ssid2g_1,test_script = test_script1,Authentication2g =Authentication2g_1, Encryption2g = Encryption2g_1 , KeyFormat2g = KeyFormat2g_1 , PresharedKey2g = PresharedKey2g_1 ,BW_MODE= BW_mode3_2g , BW_width=Bandwidth1_2g,EncryptionType2g_id= EncryptionType2g_4_id,EncryptionType2g =EncryptionType2g_4)
        Encryption_Throughput(Encryption= encryptions[1],Authentication2g_id =Authentication2g_2_id, Encryption2g_id = Encryption2g_2_id , KeyFormat2g_id = KeyFormat2g_2_id , PresharedKey2g_id = PresharedKey2g_2_id ,Account_password = Account_password , DUT_IP = DUT_IP , ssid=ssid2g_2,test_script = test_script1,Authentication2g =Authentication2g_2, Encryption2g = Encryption2g_2 , KeyFormat2g = KeyFormat2g_2 , PresharedKey2g = PresharedKey2g_2 ,BW_MODE= BW_mode3_2g , BW_width=Bandwidth1_2g,EncryptionType2g_id= EncryptionType2g_4_id,EncryptionType2g =EncryptionType2g_3)
        Encryption_Throughput(Encryption= encryptions[2],Authentication2g_id =Authentication2g_3_id, Encryption2g_id = Encryption2g_3_id , KeyFormat2g_id = KeyFormat2g_3_id , PresharedKey2g_id = PresharedKey2g_3_id ,Account_password = Account_password , DUT_IP = DUT_IP , ssid=ssid2g_3,test_script = test_script1,Authentication2g =Authentication2g_3, Encryption2g = Encryption2g_3 , KeyFormat2g = KeyFormat2g_3 , PresharedKey2g = PresharedKey2g_3 ,BW_MODE= BW_mode3_2g , BW_width=Bandwidth1_2g,EncryptionType2g_id= EncryptionType2g_4_id,EncryptionType2g =EncryptionType2g_3)
        Encryption_Throughput(Encryption= encryptions[3],Authentication2g_id =Authentication2g_4_id, Encryption2g_id = Encryption2g_4_id , KeyFormat2g_id = KeyFormat2g_4_id , PresharedKey2g_id = PresharedKey2g_4_id ,Account_password = Account_password , DUT_IP = DUT_IP , ssid=ssid2g_4,test_script = test_script1,Authentication2g =Authentication2g_4, Encryption2g = Encryption2g_4 , KeyFormat2g = KeyFormat2g_4 , PresharedKey2g = PresharedKey2g_4 ,BW_MODE= BW_mode3_2g , BW_width=Bandwidth1_2g,EncryptionType2g_id= EncryptionType2g_4_id,EncryptionType2g =EncryptionType2g_4)
        Encryption_Throughput(Encryption= encryptions[4],Authentication2g_id =Authentication2g_5_id, Encryption2g_id = Encryption2g_5_id , KeyFormat2g_id = KeyFormat2g_5_id , PresharedKey2g_id = PresharedKey2g_5_id ,Account_password = Account_password , DUT_IP = DUT_IP , ssid=ssid2g_5,test_script = test_script1,Authentication2g =Authentication2g_5, Encryption2g = Encryption2g_5 , KeyFormat2g = KeyFormat2g_5 , PresharedKey2g = PresharedKey2g_5 ,BW_MODE= BW_mode3_2g , BW_width=Bandwidth1_2g,EncryptionType2g_id= EncryptionType2g_4_id,EncryptionType2g =EncryptionType2g_5)
         

                
       
        file = open(save_result,'a')  
       
        file.write("\n"+"\n")         
                
        file.write('End time :      '+str(datetime.now())+"\n"+"\n") 
        
        file.close()