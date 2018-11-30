from selenium import webdriver

class send:
    def __init__(self):
        self.driver_dir='/home/sjo506/chromedriver'
        # 드라이버의 위치
        self.find_army_url="http://www.katc.mil.kr/katc/community/children.jsp"
        #내자녀 찾기 주소
        self.driver=webdriver.Chrome(self.driver_dir)
        self.driver.implicitly_wait(3)
        self.process_find_army()

    def process_find_army(self):
        self.driver.get(self.find_army_url)
        self.driver.find_element_by_name('search_val1').send_keys('20180910')
        self.driver.find_element_by_name('birthDay').send_keys('19980715')
        self.driver.find_element_by_name('search_val3').send_keys('신정우\n')



a=send()