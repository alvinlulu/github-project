# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import base64
import requests
import json
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from selenium.webdriver.chrome.options import Options


info = '998,889'
ship = info.split(',')

if isinstance(ship, list):

    catch_num = []
    catch_uptime = []
    catch_status = []
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
     
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    browser.get('https://www.hct.com.tw/search/searchgoods_n.aspx')
    
     
    print ('search shipinfo...')
    time.sleep(10)
    for i in range(len(ship)):
        print (i)
        
        if i == 0 :
            shipnum = browser.find_element(By.NAME, 'ctl00$ContentFrame$txtpKey')
            shipnum.send_keys(str(ship[i]))
    
        else:
            shipnum = browser.find_element(By.NAME, 'ctl00$ContentFrame$txtpKey' + str(i+1))
            shipnum.send_keys(str(ship[i]))
            
            
    
    
    img_base64 = browser.execute_script("""
        var ele = arguments[0];
        var cnv = document.createElement('canvas');
        cnv.width = ele.width; cnv.height = ele.height;
        cnv.getContext('2d').drawImage(ele, 0, 0);
        return cnv.toDataURL('image/jpeg').substring(22);    
        """, browser.find_element(By.XPATH, '//*[@id="aspnetForm"]/article/div[4]/div[1]/div[2]/img')) #draw caption image
    
        
    #with open("captcha_login.png", 'wb') as image:
    #    image.write(base64.b64decode(img_base64)) # save image 
    #file = image.read
        
    #file = {'file': open('captcha_login.png', 'rb')}  #下載下來的一般驗證碼(Normal Captcha)圖片
    
    
    
    resp = requests.post("http://192.168.179.14:9898/ocr/b64/text", data=img_base64)
    code = json.loads(resp.content)
    chcode = browser.find_element(By.CLASS_NAME, 'chktxt')
    chcode.send_keys(str(code))
    chcode.send_keys('\ue007') # 按下Enter
    
    for i in range(len(ship)):
        catch_num.append(browser.find_element(By.ID, 'ctl00_ContentFrame_rtprt_ctl0' + str(i) + '_L_inv').text)
        catch_uptime.append(browser.find_element(By.ID, 'ctl00_ContentFrame_rtprt_ctl0' + str(i) + '_L_tim').text)
        catch_status.append(browser.find_element(By.ID, 'ctl00_ContentFrame_rtprt_ctl0' + str(i) + '_L_cls').text)
    
    #----add data----
    
    dfData = pd.DataFrame({
        'Ship_num':catch_num,
        'Update_time':catch_uptime,
        'Status':catch_status
        })
    JData =pd.DataFrame.to_json(dfData)


else:
    catch_num = []
    catch_uptime = []
    catch_status = []
    
    
     
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('https://www.hct.com.tw/search/searchgoods_n.aspx')
     
    print ('search shipinfo...')
    time.sleep(10)
    
    shipnum = browser.find_element(By.NAME, 'ctl00$ContentFrame$txtpKey')
    shipnum.send_keys(str(ship))
    
        
        
    img_base64 = browser.execute_script("""
        var ele = arguments[0];
        var cnv = document.createElement('canvas');
        cnv.width = ele.width; cnv.height = ele.height;
        cnv.getContext('2d').drawImage(ele, 0, 0);
        return cnv.toDataURL('image/jpeg').substring(22);    
        """, browser.find_element(By.XPATH, '//*[@id="aspnetForm"]/article/div[4]/div[1]/div[2]/img')) #draw caption image
    
        
    #with open("captcha_login.png", 'wb') as image:
    #    image.write(base64.b64decode(img_base64)) # save image 
    #file = image.read
        
    #file = {'file': open('captcha_login.png', 'rb')}  #下載下來的一般驗證碼(Normal Captcha)圖片
    
    
    
    resp = requests.post("http://192.168.50.223:9898/ocr/b64/text", data=img_base64)
    code = json.loads(resp.content)
    
    chcode = browser.find_element(By.CLASS_NAME, 'chktxt')
    chcode.send_keys(str(code))
    chcode.send_keys('\ue007') # 按下Enter
    time.sleep(10)

    for i in range(len(ship)):
        catch_num.append(browser.find_element(By.ID, 'ctl00_ContentFrame_rtprt_ctl0' + str(i) + '_L_inv').text)
        catch_uptime.append(browser.find_element(By.ID, 'ctl00_ContentFrame_rtprt_ctl0' + str(i) + '_L_tim').text)
        catch_status.append(browser.find_element(By.ID, 'ctl00_ContentFrame_rtprt_ctl0' + str(i) + '_L_cls').text)
    
    #----add data----
    
    dfData = pd.DataFrame({
        'Ship_num':catch_num,
        'Update_time':catch_uptime,
        'Status':catch_status
        })
    JData =pd.DataFrame.to_json(dfData)

    