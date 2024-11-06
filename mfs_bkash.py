# This code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client

import pandas as pd
import time
import subprocess
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# from appium.webdriver.appium_service import AppiumService
# AppiumService().start(args=['--port', '4724'])

# For W3C actions
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions import interaction
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
# from selenium.webdriver.common.actions.pointer_input import PointerInput

### appium common issue debugging ###

## for session unidentified issue run the below command from adb shell or uninstall the apps directly from handset
# adb uninstall io.appium.uiautomator2.server
# adb uninstall io.appium.uiautomator2.server.test
# adb uninstall io.appium.unlock
# adb uninstall io.appium.settings

## for socket hang up issue
# restart handset
# restart server (cmd>appium -p 4724)

## to stop server 
# taskkill /F /IM node.exe

start_time = time.time()

appium_process = subprocess.Popen(['C:\\Users\\gp1\\appium_server.bat'],creationflags=subprocess.CREATE_NEW_CONSOLE) ## starting appium server

time.sleep(25)

file_directory = 'C:\\Users\\gp1\\Documents\\report\\'

options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:automationName": "UIAutomator2",
    "appium:deviceName": "oneplus",
    "appium:platformVersion": "12",
    # "appium:deviceId": "192.168.0.106:5555",  # for adb over wifi only
    "appium:app": "C:\\Users\\gp1\\Documents\\bKash_base.apk",
    "appium:skipServerInstallation": True,
    "appium:noReset": True,  ## alternate is: dontStopAppOnReset 
    "appium:forceAppLaunch": True,
    "appium:printPageSourceOnFindFailure": True,
    "appium:newCommandTimeout": "86000",
    "appium:adbExecTimeout": "21000",
    # "appium:appPackage": "com.portonics.mygp",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4724", options=options)

driver.implicitly_wait(7)
# time.sleep(7)

# driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="|\nEnter bKash PIN").click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="5").click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="0").click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="4").click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="1").click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="9").click()

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Mobile Recharge").click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="sifat morshed\n01711086742").click()
# driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.ImageView\").instance(0)").click()
# driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Internet\nTab 2 of 6").click()

for n in range(0,1):

    if n == 0:
        operator = 'Airtel'
    if n == 1:
        operator = 'Banglalink'
    if n == 2:
        operator = 'GP'
    if n == 3:
        operator = 'Robi'
    if n == 4:
        operator = 'Skitto'
    if n == 5:
        operator = 'Teletalk'

    print(operator)
    
    driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.ImageView\").instance("+str(n)+")").click()

    # driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value = "new UiScrollable(new UiSelector()).setSwipeDeadZonePercentage(0.3).scrollIntoView(new UiSelector().text(\"xyz\"))")  ## vertical scroll till text found
    # driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value ='new UiScrollable(new UiSelector()).setSwipeDeadZonePercentage(0.3).setAsHorizontalList().scrollIntoView(new UiSelector().text("xyz"))') ## horizontal scroll till text found

    driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value="new UiScrollable(new UiSelector()).setSwipeDeadZonePercentage(0.2).setAsHorizontalList().scrollForward()") #horizontal scroll once
    
    selected_tab = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value="new UiSelector().selected(true)").tag_name

    descriptions,offer_text,no_offer_text,offer_price = [],[],[],[]
    tab_name,tab_name_report = [],[]
    len_descriptions = [0,0] ## to avoid list out of range exception on if conditions

    tab_index = 0 ## tab index counter

    while True:

        elements = driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR,value ='new UiSelector().descriptionMatches(".+")') 	

        for element in elements: ## fetching all offer details with price from UI
            desc = element.get_attribute("content-desc")  ## contentDescription
        
            if desc not in descriptions:
                descriptions.append(desc)
                offer_text.append(desc)
                offer_price.append(desc)

        len_descriptions.append(len(descriptions))
        print(len_descriptions)

        if selected_tab not in tab_name:
                
            tab_name.append(selected_tab)

        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value = "new UiScrollable(new UiSelector()).setSwipeDeadZonePercentage(0.3).scrollForward()") ## general vertical scroll

        if len_descriptions[-1] == len_descriptions[-2]:

            driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value="new UiScrollable(new UiSelector()).setSwipeDeadZonePercentage(0.2).setAsHorizontalList().scrollForward()") ## horizontal vertical scroll
            selected_tab = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value="new UiSelector().selected(true)").tag_name
            print('tab_name:' + str(tab_name))
            print('Switching Tab')

            offer_text = [i for i in offer_text if '৳' not in i]

            no_offer_text = [i for i in offer_text if not any(char.isdigit() for char in i)]

            offer_price = [i for i in offer_price if '৳' in i]

            if len(no_offer_text) == 1:

                offer_price.append('NA৳')  ## don't remove ৳ sign. otherwise no element will append due to previous line logic

            if len(tab_name) == 1:
        
                offer_text =offer_text[offer_text.index('Important Information')+1:]    
                for i in range(0,len(offer_text)): ## getting tab name to show in dataframe 
                    tab_name_report.append(tab_name[tab_index])

            else:
                for i in range(0,len(offer_text)): ## getting tab name to show in dataframe 
                    tab_name_report.append(tab_name[tab_index])

            offer_text = [] ## resting offer
            tab_index +=1

        if len_descriptions[-3] == len_descriptions[-1]:
            print('Switching operator')
            break

    driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.ImageView\").instance(2)").click()

    print('tab_name_report: ' + str(tab_name_report))

    descriptions = descriptions[descriptions.index('Important Information')+1:]       ## to exclude tab names
    descriptions = [i.replace('\n',' ').replace('Cashback Offer ','').replace('Exclusive Deal ','').replace('Best Offer ','').replace('Popular Offer ','').replace('Super Offer ','').replace('Most Popular ','').replace('Play Pack ','').replace('New Offer ','').replace('Special Offer ','') for i in descriptions]      ## to exclude extra words and \n

    offer_list = [i for i in descriptions if '৳' not in i]         ## to exclude price
    # offer = [i for i in offer if any(char.isdigit() for char in i)]        ## to exclude string descriptionske 'Sorry, currently there are no offers!
    # offer_string = [i for i in offer if not any(char.isdigit() for char in i)] 
    print('\n' + str(offer_list))

    # price = [i for i in descriptions if '৳' in i]
    offer_price = [i.replace('৳','') for i in offer_price]
    print('\n' + str(offer_price))

    tab_list = []
    for i in tab_name_report:
        i = i.split('\n')[0]
        tab_list.append(i)

    df = pd.DataFrame({'Operator':operator,'Offer':offer_list,'Price':offer_price,'Type':tab_list})
    print(df)
    df.to_csv(file_directory + 'bkash_'+operator+'.csv',index = False)

# appium_process.kill()
driver.quit()

print(time.time()-start_time)
exit()
