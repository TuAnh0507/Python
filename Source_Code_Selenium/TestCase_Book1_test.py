import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import page
import time

url = 'https://www.expedia.com/'

class ExpediaTestCase(unittest.TestCase):
	def setUp(self):
		print("Start Test")
		self.browser = webdriver.Chrome(ChromeDriverManager().install())
		self.timeout = 40
	def testPage(self):
		self.browser.get(url)
		self.browser.maximize_window()
		print('Title:', self.browser.title)
		print(self.browser.current_url)
		print('=======================')
		time.sleep(2)

		ele = self.browser.find_element_by_xpath("//div[contains(text(),'More travel')]")
		ele.click()
		time.sleep(2)
		link = self.browser.find_element_by_link_text('Flights')
		link.click()
		time.sleep(2)


		input_leaving = self.browser.find_element_by_xpath("//button[contains(@aria-label,'Leaving from')]")
		input_going = self.browser.find_element_by_xpath("//button[contains(@aria-label,'Going to')]")
		input_departing = self.browser.find_element_by_id("d1-btn")
		input_leaving.send_keys("Hanoi")
		time.sleep(2)
		self.browser.find_element_by_xpath("//strong[contains(text(), 'Hanoi (HAN - Noi Bai Intl.)')]").click()
		input_going.send_keys("Ho Chi Minh")
		time.sleep(2)
		self.browser.find_element_by_xpath("//strong[contains(text(), 'Ho Chi Minh City (SGN - Tan Son Nhat Intl.)')]").click()
		time.sleep(2)


		input_departing.click()
		time.sleep(2)
		#self.browser.find_element_by_xpath("//button[contains(@data-stid,'date-picker-paging')]").click()
		#time.sleep(2)
		self.browser.find_element_by_xpath("//button[contains(@data-day,'6')]").click()
		time.sleep(2)
		self.browser.find_element_by_xpath("//button[contains(@data-stid,'apply-date-picker')]").click()
		time.sleep(5)

	
		search = self.browser.find_element_by_xpath("//*[@id='wizard-flight-pwa-1']/div[3]/div/button").click()
		time.sleep(2)

		#element=driver.find_element_by_id("listings-sort")
		#drp=Select(driver.find_element_by_id("listings-sort"))
		#drp.select_by_value("PRICE_DECREASING")

		print('Title:', self.browser.title)
		self.browser.find_element_by_xpath("//*[@id='app-layer-base']/div[2]/div[3]/div/section/main/div[1]/div").click()
		time.sleep(5)

		table = self.browser.find_element_by_tag_name("table")
		#header = table.find_elements_by_tag_name("th")
		#body = table.find_element_by_tag_name("tbody")
		#rows = body.find_elements_by_tag_name("tr")
		#cells = body.find_elements_by_tag_name("td")
		#print(len(rows))

		print(table.text)
		print('========================')

		if 'Sep 6' in (table.text):
			contents = self.browser.find_elements_by_tag_name("li")
			for content in contents:
				print(content.text)
		else:
			print("Not find flight")
		

		print('=========================')
		print('Finish test')

	def tearDown(self):
		self.browser.quit()

if __name__ == '__main__':
	unittest.main()