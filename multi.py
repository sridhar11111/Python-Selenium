from selenium import webdriver
from win10toast import ToastNotifier
from keyboard import press
import smtplib
from selenium.webdriver.common.keys import Keys
import time

pas = "akhand@123"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("akhandparadi146@gmail.com", pas)
msz = "Betaa Tmhari Ganaaand fategi abhi . ise rokne k liye call on 7355481151"
m2 = "ritwikmohan176@gmail.com"
i = 0
while True:
    server.sendmail("akhandparadi146@gmail.com", "email.shashwattiwari@gmail.com", msz)
    server.sendmail("akhandparadi146@gmail.com", "email.shashwattiwari@gmail.com", m2)
    print(i)
    i = i+1
server.quit()
# phone = "Redmi Note 5 pro Amazon"
# driver = webdriver.Chrome(executable_path="C:\seleniumdrivers\chromedriver.exe")
# driver.get("https://www.google.com/")
# #//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input
# sri = driver.find_element_by_xpath("//input[@name='q']")
# sri.send_keys(phone)
# press('enter')
# time.sleep(10)
# baj = driver.find_element_by_xpath("//*[@id='plahover0']")
# press('enter')
#
# driver.find_element_by_xpath("//*[@id='nav-search']/form/div[2]/div/input").click()
# driver.find_element_by_xpath("//*[@id='vplahcl0']/div[3]/div[1]/span")
# driver.get("https://www.amazon.in/Samsung-Galaxy-M30-Gradation-Blue/dp/B07HGJJ58K/ref=sr_1_1_sspa?keywords=samsung+m30&qid=1581852620&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEySEk4TzQ3U1lZQ0RDJmVuY3J5cHRlZElkPUEwNTk0Mzk3MllQUUNSQkxRWElPMCZlbmNyeXB0ZWRBZElkPUExMDIyNTA3MTcwREpaNEFVRzAwMiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=")
# price = driver.find_element_by_xpath("//*[@id='priceblock_ourprice']").text
# p2 = driver.find_element_by_class_name("a-offscreen").text
# print(p2)
# mn = 10000000
# driver.get("https://www.flipkart.com/samsung-galaxy-m30s-black-64-gb/p/itm918b2523e0fb7?pid=MOBFK9AVSTDSDMW6&lid=LSTMOBFK9AVSTDSDMW6H7554H&marketplace=FLIPKART&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_0_18_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_0_18_na_na_na&fm=SEARCH&iid=b48beeb6-c842-46e6-8aee-36b99133ff58.MOBFK9AVSTDSDMW6.SEARCH&ppt=sp&ppn=sp&ssid=i6gr2gj1dc0000001582299087945&qH=3409621f010fad68")
# pr_fp = driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]").text
# print(pr_fp)
# price = price.replace(',', '')
# price = price.replace('₹', '')
# price = price.replace('.00', '')
# price = int(price)
# pr_fp = pr_fp.replace(',', '')
# pr_fp = pr_fp.replace('₹', '')
# pr_fp = pr_fp.replace('.00', '')
# pr_fp = int(pr_fp)
#
# if mn > price or mn > pr_fp:
#     if price < pr_fp :
#         hr = ToastNotifier()
#         hr.show_toast("Amazon Best", "Less prices than flipkart dropped to " +"https://www.amazon.in/Samsung-Galaxy-M30-Gradation-Blue/dp/B07HGJJ58K/ref=sr_1_1_sspa?keywords=samsung+m30&qid=1581852620&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEySEk4TzQ3U1lZQ0RDJmVuY3J5cHRlZElkPUEwNTk0Mzk3MllQUUNSQkxRWElPMCZlbmNyeXB0ZWRBZElkPUExMDIyNTA3MTcwREpaNEFVRzAwMiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="+str(price), duration=20)
#     else:
#         hr = ToastNotifier()
#         hr.show_toast("Go Go FLipkart ", "Less prices than Amazon dropped to " + "https://www.amazon.in/Samsung-Galaxy-M30-Gradation-Blue/dp/B07HGJJ58K/ref=sr_1_1_sspa?keywords=samsung+m30&qid=1581852620&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEySEk4TzQ3U1lZQ0RDJmVuY3J5cHRlZElkPUEwNTk0Mzk3MllQUUNSQkxRWElPMCZlbmNyeXB0ZWRBZElkPUExMDIyNTA3MTcwREpaNEFVRzAwMiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="+str(pr_fp), duration=20)
#
#
#
#     # driver.get("http://www.facebook.com/"
#     # driver.get("http://www.amazon.com/")
#     # driver.get("http://www.flipkart.com/")
#     # driver.get("http://www.snapdeal.com/")
#
#
# print(driver.title)
# driver.close()
