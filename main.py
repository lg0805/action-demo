from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# 配置 Chrome 选项
chrome_options = Options()
chrome_options.add_argument('--headless')  # 无头模式
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')

# 指定 ChromeDriver 的路径
chrome_service = ChromeService()

# 初始化 WebDriver
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

try:
    # 打开登录页面
    driver.get('https://w1.v2ai.top/auth/login')
    
    # 等待2秒钟
    time.sleep(2)
    
    # 找到 ID 为 email 的输入框，输入用户名
    email_input = driver.find_element(By.ID, 'email')
    email_input.send_keys('lg0805@foxmail.com')
    
    # 找到 ID 为 passwd 的输入框，输入密码
    password_input = driver.find_element(By.ID, 'passwd')
    password_input.send_keys('jp991029')
    
    # 找到 ID 为 login 的按钮，并单击
    login_button = driver.find_element(By.ID, 'login')
    login_button.click()
    
    # 等待5秒钟
    time.sleep(5)
    
    # 找到 ID 为 result_ok 的元素并单击
    result_ok_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'result_ok'))
    )
    result_ok_button.click()
    
    # 等待3秒钟
    time.sleep(3)
    
    # 找到类为 cb-lb 下的 input 标签并单击
    cb_lb_input = driver.find_element(By.CSS_SELECTOR, '.cb-lb input')
    cb_lb_input.click()
    
    # 等待1秒钟
    time.sleep(1)
    
    # 找到 ID 为 checkin 的按钮并单击
    checkin_button = driver.find_element(By.ID, 'checkin')
    checkin_button.click()
    
finally:
    # 关闭 WebDriver
    driver.quit()
