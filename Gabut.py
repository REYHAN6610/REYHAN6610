from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# BY REYHAN6610
driver_path = "/usr/local/bin/chromedriver"  # Sesuaikan dengan path chromedriver Anda

phone_number = input("Masukkan nomor telepon dengan format internasional (misalnya +6281234567890): ")
message = input("Masukkan pesan yang ingin dikirim: ")

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')  
driver = webdriver.Chrome(executable_path=driver_path, options=options)
driver.get("https://web.whatsapp.com/")

time.sleep(20)  # Waktu untuk login, sesuaikan sesuai kebutuhan

# Cari kotak pencarian
search_box = driver.find_element_by_xpath("//div[@contenteditable='true']")
search_box.click()
search_box.send_keys(phone_number)
search_box.send_keys(Keys.ENTER)

time.sleep(10)  

for _ in range(100):
    
    message_box = driver.find_element_by_xpath("//div[@contenteditable='true' and @data-tab='6']")
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)
    time.sleep(1)  

time.sleep(5)
driver.quit()
