# Importing the necessary libraries
import selenium
from selenium import webdriver as wb
import pandas as pd
import time
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Chaning the working directory to the path where the chromedriver is saved & setting up the chrome driver
import time
start_time = time.time()
#%cd "C:\Users\v-aniuppu\Documents\Naukri Automation"
#%cd "C:\Users\ROSHAN\Documents\Naukri Automation"
driver = wb.Chrome(r"chromedriver.exe")
Skillset = ['fshgfhs']
Skillset = [x.lower() for x in Skillset]
LL = 7
UL = 15
location = 'Hyderabad'
location = location.lower().replace(" ","-")
role = 'Data Analyst'
#role = 'Manual Testing'
role = role.lower().replace(" ","-")
driver.get("https://www.naukri.com/")
driver.find_element_by_xpath('//*[@id="login_Layer"]/div').click()
time.sleep(5)

driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div/form/div[2]/input').send_keys('anil4274ai@gmail.com')
driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div/form/div[3]/input').send_keys('Gax@2735')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div/form/div[6]/button').click()
time.sleep(5)
app = pd.DataFrame()

for i in range(1,6):
    try:
        driver.get('https://www.naukri.com/'+role+'-jobs-in-'+location+'-'+str(i)+'?experience=3')
    except:
        driver.get('https://www.naukri.com/'+role+'-jobs-in-'+location+'?experience=3')

    for i in range(1,20):
        try:
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[3]/div[2]/section[2]/div[2]/article['+str(i)+']/div[1]/div[1]/a'))).click()
        except:
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[3]/div[2]/section[2]/div[2]/article['+str(i)+']/div[1]/div/a'))).click()
        driver.switch_to.window(driver.window_handles[1])
        url = driver.current_url
        driver.get(url)
        time.sleep(5)
        try:
            test = driver.find_element_by_xpath('//*[@id="root"]/main/div[2]/div[2]/section[2]')
            if all(word not in test.text.lower() for word in Skillset):
                Title = driver.find_element_by_xpath('//*[@id="root"]/main/div[2]/div[2]/section[1]/div[1]/div[1]/header/h1')
                Title = Title.text
                Title = pd.Series(Title)
                Company = driver.find_element_by_xpath('//*[@id="root"]/main/div[2]/div[2]/section[1]/div[1]/div[1]/div/a[1]')
                Company = Company.text
                Company = pd.Series(Company)
                loc = driver.find_element_by_xpath('//*[@id="root"]/main/div[2]/div[2]/section[1]/div[1]/div[2]/div[3]/span/a')
                loc = loc.text
                loc = pd.Series(loc)
                df = pd.DataFrame({'Title':Title,'Company':Company,'Location':loc})
                app = app.append(df)
                if driver.find_element_by_xpath('//*[@id="root"]/main/div[2]/div[2]/section[1]/div[1]/div[3]/div/button[2]').text == 'APPLY':
                    driver.find_element_by_xpath('//*[@id="root"]/main/div[2]/div[2]/section[1]/div[1]/div[3]/div/button[2]').click()
                    time.sleep(2)
                    try:
                        aa = driver.find_element_by_xpath('//*[@id="qusFrm"]').get_attribute('childElementCount')
                        no_of_divs = int(aa)-1
                        if no_of_divs > 2:
                            driver.close()
                            driver.switch_to.window(driver.window_handles[0])
                        #else:
                    except:
                        try:
                            aa = driver.find_element_by_xpath('//*[@id="qusFrm"]').get_attribute('childElementCount')
                            no_of_divs = int(aa)-1
                            if no_of_divs == 1:
                                driver.find_element_by_xpath('//*[@id="qusFrm"]/div[1]/ul/li/input').click()
                                time.sleep(3)
                                driver.find_element_by_xpath('//*[@id="qusSubmit"]').click()
                                time.sleep(3)
                                driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div[11]/a').click()
                                time.sleep(3)
                                driver.close()
                                driver.switch_to.window(driver.window_handles[0])
                        except:
                            aa = driver.find_element_by_xpath('//*[@id="qusFrm"]').get_attribute('childElementCount')
                            no_of_divs = int(aa)
                            if no_of_divs == 1:
                                driver.find_element_by_xpath('//*[@id="qusFrm"]/div[1]/ul/li/input').click()
                                time.sleep(3)
                                driver.find_element_by_xpath('//*[@id="qusSubmit"]').click()
                                time.sleep(3)
                                driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div[11]/a').click()
                                time.sleep(3)
                                driver.close()
                                driver.switch_to.window(driver.window_handles[0])

                else:
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
            else:
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
        except:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
app