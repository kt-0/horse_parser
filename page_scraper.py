
import os, PyPDF2, re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# NOTE: bypassing captchas
# https://stackoverflow.com/questions/33225947/can-a-website-detect-when-you-are-using-selenium-with-chromedriver

#from selenium.webdriver.chrome.options import Options
#chrome_options = Options()
#chrome_options.add_argument("--headless")
#chrome_options.binary_location = "/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary"
#driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),   chrome_options=chrome_options)
#driver = webdriver.Firefox(executable_path=os.path.abspath("geckodriver")) #for firefox
driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver")) #for chrome
base_url = "http://www.equibase.com/"
driver.get(base_url)

search_box = driver.find_element_by_id("searchInput")
if search_box.is_displayed():
  search_box.click()
  search_box.send_keys("american pharaoh")
  search_box.send_keys(Keys.RETURN)
  results_tab = driver.find_element_by_id("Hresults")
  results_tab.click()
  charts = driver.find_elements_by_class_name("chart")
  charts[0].click()
  driver.switch_to_window(driver.window_handles[1])
  download_button = driver.find_element_by_id("download")

pdfFileObj = open('amer_pharaoh.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
extracted_text = pageObj.extractText()
# r = re.compile(r'([a-zA-Z]+).(?<=\()\w+\,\w+(?=\))',re.M)
matches = re.findall(r"([a-zA-Z]+).(?<=\()\w+\,\w+(?=\))", extracted_text, re.M)
