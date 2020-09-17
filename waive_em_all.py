import time
import os

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.set_headless()
assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts, executable_path=r'/home/vagrant/.local/bin/geckodriver')
print('First get..')
browser.get('https://www.fantrax.com')
print('Sleeping 10s..')
time.sleep(10)

#print(browser.page_source)
username = os.environ['FANTRAX_U']
password = os.environ['FANTRAX_P']

login_btn = browser.find_element_by_xpath('//html/body/app-root/div/div[1]/navbar/desktop-nav/div/div/section[2]/div[1]/b')
print('Clicking login button')
login_btn.click()
login_form = browser.find_element_by_id('mat-input-0')
login_form.send_keys(username)
login_form = browser.find_element_by_id('mat-input-1')
login_form.send_keys(password)

submit_btn = browser.find_element_by_xpath('//html/body/app-root/div/div[1]/navbar/desktop-nav/div/div/section[2]/div[1]/div/nav-profile/div/div[3]/button')


submit_btn.click()
print('Logging in..')
print('Sleeping 10s..')
time.sleep(10)


print('Accessing commissioner options page..')
browser.get('https://www.fantrax.com/newui/fantasy/commissionerOptions.go?leagueId=orb7rdmfkdoj98r8')
print('Sleeping 10s..')
time.sleep(10)


waive_btn = browser.find_element_by_xpath('//html/body/section/div[4]/div[4]/div[4]/div[1]/div[4]/div/div/div[2]/div[2]/div[5]/div/div[1]/p/a')
waive_btn.click()

waive_confirm_btn = browser.find_element_by_xpath('//html/body/section/div[4]/div[1]/div[2]/div[4]/div[1]')
print('Confirming waive all players..')
waive_confirm_btn.click()
print('Sleeping 10s..')
time.sleep(10)

print(browser.page_source)

browser.close()
quit()

