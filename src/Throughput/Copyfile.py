# -*- coding: cp950 -*-
'''
Created on 2010/1/11

@author: Jocabion
'''

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
    
#     copyanything('D:\\Workspace\\VideoBridge\\src\\VideoBridge.py', 'C:\\Python26')
#     copyanything('D:\\Workspace\\VideoBridge\\src\\VideoBridgeGUI.py', 'C:\\Python26')
#     data_list=[]
#     with open("D:\Workspace\VideoBridge\src\VideoBridge.py", "r+") as f:
#              
#              data = f.readlines()
# 
#              for row in data :
# 
#               if "Band (2.4G) > Pass" in row :
#                   
#                   row = "                                          file.write('NMS settings > Access point > Radio Settings > Band (2.4G) > Pass' + '\n' + '  set' + str(bandG_before) + '  get' +str(bandG_after)) " +"\n"
#                   data_list.append(row)
#               
#               elif "Band (2.4G) > fail" in row :
#                   
#                   row = "                                          file.write('NMS settings > Access point > Radio Settings > Band (2.4G) > fail' + '\n' + '  set' + str(bandG_before) + '  get' +str(bandG_after)) " +"\n"
#                   data_list.append(row)
#               
#               
#               
#               
#               elif "Band (5G) > Pass" in row :
#             
# 
#               
#                  row = "                                           file.write('NMS settings > Access point > Radio Settings > Band (5G) > Pass' + ' ' + '  set' + str(bandA_before) + '  get' +str(bandA_after)) " +"\n" 
#                  data_list.append(row)
# 
#               elif "Band (5G) > fail" in row :
# 
#               
#                  row = "                                           file.write('NMS settings > Access point > Radio Settings > Band (5G) > fail' + ' ' + '  set' + str(bandA_before) + '  get' +str(bandA_after)) " +"\n" 
#                  data_list.append(row)
#               
#               elif "#" in row :
#               
#                  pass
#                  data_list.append(row)
#       
#                   
#                    
#               
#               else :
#                  data_list.append(row) 
#                         
# #                  print row
# #                  row = str(row).replace('VideoBridgeGUI','VideoBridge')
# #                  print row
#                     
#          
#        
#     with open("D:\Workspace\VideoBridge\src\VideoBridge.py", "w") as f:
#              f.writelines(data_list)
#                      
            
#              cmdrun = cmd.splitlines()
    pingPopen = subprocess.Popen(args='python setup.py py2exe', shell=True, stdout=subprocess.PIPE)
    pingstring = pingPopen.stdout.read()
    print pingstring 
#     distutils.dir_util.copy_tree('C:\\Users\\PA-Andy\\workspace\\VideoBridge\\src\\Throughput\\dist', 'F:\\Edimax Auto test\\program backup\\dist')         
#     wifi = Wireless('eth1')
#     print wifi.getEssid()
#     print wifi.getMode()
#     
#     c = wmi.WMI ()
#     
#    
#     for disk in c.Win32_LogicalDisk (DriveType=2):
#       print disk.Caption,  convertSize(float(disk.FreeSpace)) , convertSize(float(disk.Size))
                                     
                 
                 