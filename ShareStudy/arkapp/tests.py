from datetime import datetime
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Hosttest(TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.live_server_url = 'http://127.0.0.1:8000/'

    def tearDown(self):
        self.driver.quit()
        
    def test_01_login_page(self):
        driver = self.driver
        driver.get(self.live_server_url)
        driver.maximize_window()
        time.sleep(1)
        login=driver.find_element(By.CSS_SELECTOR,"a[href='login']")
        login.click()
        time.sleep(2)
        email=driver.find_element(By.CSS_SELECTOR,"input#email[type='text'][name='email'][required]")
        email.send_keys("subintom1111@gmail.com")
        password=driver.find_element(By.CSS_SELECTOR,"input#password[type='password'][name='password'][required]")
        password.send_keys("Subintom123@")
        time.sleep(2)
        submit=driver.find_element(By.CSS_SELECTOR,"button.submit-btn[type='submit']")
        submit.click()
        time.sleep(2)



        chatroom=driver.find_element(By.CSS_SELECTOR,"a[href='/chat/']")
        chatroom.click()
        time.sleep(2)
        roomtext=driver.find_element(By.CSS_SELECTOR,"input#input-message.form-control.type_msg[type='text']")
        roomtext.send_keys("Hello this is a Test Message")
        time.sleep(2)
        send=driver.find_element(By.CSS_SELECTOR,"button.btn.btn-secondary[type='submit']")
        send.click()
        time.sleep(2)


        # aptitude=driver.find_element(By.CSS_SELECTOR,"a[href='/exams/']")
        # aptitude.click()
        # time.sleep(2)
        # startexam=driver.find_element(By.CSS_SELECTOR,"button.start-exam-btn")
        # startexam.click()
        # time.sleep(2)
        # but1=driver.find_element(By.CSS_SELECTOR,"input[type='radio'][name='answer_36'][value=' 1/2 cup']")
        # but1.click()
        # but2=driver.find_element(By.CSS_SELECTOR,"input[type='radio'][name='answer_37'][value='$75']")
        # but2.click()
        # subm=driver.find_element(By.CSS_SELECTOR,"button#submitExam.submit-button[type='submit']")
        # subm.click()
        # time.sleep(2)


        # bookstore=driver.find_element(By.CSS_SELECTOR,"a[href='/view_product']")
        # bookstore.click()
        # time.sleep(2)
        # book=driver.find_element(By.CSS_SELECTOR,"button.green-button.buy-now-button[type='submit']")
        # book.click()
        # time.sleep(2)
        # form1=driver.find_element(By.CSS_SELECTOR,"input#name[type='text'][name='name'][required]")
        # form1.send_keys("Shibin")
        # form2=driver.find_element(By.CSS_SELECTOR,"input#mobile[type='text'][name='mobile'][required]")
        # form2.send_keys("9605350966")
        # form3=driver.find_element(By.CSS_SELECTOR,"input#pincode[type='text'][name='pincode'][required]")
        # form3.send_keys("689545")
        # form4=driver.find_element(By.CSS_SELECTOR,"input#locality[type='text'][name='locality'][required]")
        # form4.send_keys("Thadiyoor P O Thiruvalla")
        # form5=driver.find_element(By.CSS_SELECTOR,"textarea#address[name='address'][rows='4'][required]")
        # form5.send_keys("Kaniyarolil House Thadiyoor P O Thiruvalla")
        # form6=driver.find_element(By.CSS_SELECTOR,"input#city[type='text'][name='city'][required]")
        # form6.send_keys("Pathanamthitta")
        # form7=driver.find_element(By.CSS_SELECTOR,"select#state[name='state'][required] option[value='Assam']")
        # form7.click()
        # form8=driver.find_element(By.CSS_SELECTOR,"select#address-type[name='address-type'][required] option[value='home']")
        # form8.click()
        # sub=driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
        # sub.click()
        # time.sleep(2)
        # pay=driver.find_element(By.CSS_SELECTOR,"input[type='submit'].razorpay-payment-button[value='Pay with Razorpay']")
        # pay.click()
        # time.sleep(2)
        



        # bookstore=driver.find_element(By.CSS_SELECTOR,"a[href='/view_product']")
        # bookstore.click()
        # time.sleep(2)
        # form9=driver.find_element(By.CSS_SELECTOR,"select#price_filter[name='price_filter'] option[value='low_to_high']")
        # form9.click()
        # form10=driver.find_element(By.CSS_SELECTOR,"select#category_filter[name='category_filter'] option[value='Fiction']")
        # form10.click()
        # form11=driver.find_element(By.CSS_SELECTOR,"select#language_filter[name='language_filter'] option[value='English']")
        # form11.click()
        # sub=driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
        # sub.click()
        # time.sleep(2)


        
        
