from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# create a Firefox driver
driver = webdriver.Firefox()

driver.get("https://www.youtube.com")
# add YouTube cookies to the driver
driver.add_cookie({
    'name':
    'SID',
    'value':
    'VAj6iby5GwJv3Xczib4J4_CsDprMBZEja4_XkNM9YdNiTGc_o5_E7aPVv3O7Gc4jNgWpXA.'
})
driver.add_cookie({'name': 'HSID', 'value': 'AEcfEWcWRW8RhuLJR'})
driver.add_cookie({'name': 'SSID', 'value': 'A0DxW12IUH1L6T1mn'})
driver.add_cookie({
    'name': 'APISID',
    'value': 'AlyMkKiTKk1fWQr-/AttiWvazj0J59bGRM'
})
driver.add_cookie({
    'name': 'SAPISID',
    'value': 'V3oFl7dkMRPpeeAN/A3C6HC-dy_orGAY_9'
})
driver.add_cookie({
    'name':
    'LOGIN_INFO',
    'value':
    'AFmmF2swRgIhAOnSFKeonL3ANgoWtTGaw98-pZ04V0n-if-oS3zn-RYGAiEAplEdeyZNeZme6z5RPW_wQ5H5dVDjar1k90ikXxIdPi0:QUQ3MjNmeXZDNE42UGZuTE94UVpSMEl1bzktLUd0NHVQZm5hem1zWDJjRWQ1a1lMWlI2OU0yNGFuOThKOUdPS0ZwMnl3TXowandwamo2LTk3QUpqOUQxU1RCU2ZEcFVEZmtzSWdVMDhCWXB6QXlISmlRckNCLTJCbXF1eWktby01Zk5HSThjSlFIU3FHN1hJN2lneG1hanczeW1xYzczb1JR'
})

# navigate to YouTube
driver.get("https://www.youtube.com/playlist?list=LL")

# do something with the driver (e.g., access your YouTube account)
import time

vids = driver.find_element(
    By.XPATH,
    "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse[2]/ytd-playlist-header-renderer/div/div[2]/div[1]/div/div[1]/div[1]/ytd-playlist-byline-renderer/div/yt-formatted-string[1]/span[1]"
)


vids.get_attribute(name)
time.sleep(120)
# close the driver
driver.quit()
"asdasdad".encode().decode()
from undetected_chromedriver import Chrome, ChromiumOptions
