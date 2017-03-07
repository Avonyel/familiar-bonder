from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)

driver.implicitly_wait(30)

action_chains = ActionChains(driver)
wait = WebDriverWait(driver, 30)

username_input = "Avonyel"
password_input = os.environ["FR_PASS"]

familiar_array = [353, 356, 359, 375, 377, 379, 380, 381, 382, 403, 
                  404, 406, 407, 410, 411, 412, 413, 415, 416, 417, 
                  419, 420, 421, 422, 592, 593, 594, 595, 596, 597, 
                  598, 599, 600, 601, 607, 608, 612, 616, 617, 618, 
                  619, 621, 622, 623, 628, 629, 631, 632, 635, 638, 
                  639, 642, 643, 648, 649, 669, 725, 727, 747, 748, 
                  772, 785, 786, 799, 800, 803, 804, 819, 820, 883, 
                  884, 905, 987, 1034, 1101, 1144, 1149, 1173, 1221, 1222, 
                  1272, 1293, 1294, 1363, 1365, 1449, 1450, 1480, 1564, 1565, 
                  1672, 1673, 1795, 1796, 1929, 1930, 1968, 1969, 2072, 2073, 
                  2151, 2394, 2577, 2590, 2604, 2782, 2887, 2917, 3176, 3177, 
                  3643, 3782, 4001, 4347, 4348, 4349, 4350, 4355, 4356, 4678, 
                  4805, 4806, 4882, 4883, 4884, 4886, 4887, 4927, 5177, 5178, 
                  5196, 5197, 5511, 6073, 6332, 6333, 6334, 6336, 6339, 6715, 
                  7328, 7591, 7592, 7595, 7598, 7599, 7697, 7698, 7699, 7700, 
                  7701, 7702, 7703, 7704, 7705, 7883, 8319, 8320, 8400, 8968, 
                  9226, 9488, 9998, 10228, 10229, 10230, 10231, 10232, 10235, 10537, 
                  10666, 10874, 10884, 10885, 10886, 10887, 11147, 11148, 11219, 11525, 
                  11666, 11679, 11680, 11816, 11969, 12194, 12550, 13085, 13086, 13241, 
                  13422, 13423, 13424, 13425, 13426, 13427, 13428, 13429, 13430, 13431, 
                  13432, 13433, 13434, 13435, 14122, 14290, 14291, 14441, 14442, 14558, 
                  14570, 14677, 15130, 15131, 15275, 15276, 15277, 15278, 15279, 15280, 
                  15281, 15282, 15283, 15284, 15285, 15286, 15287, 15288, 15289, 15298, 
                  15592, 15593, 15875]
num_dragons = 42
num_familiars = 193
current_dragon = 0
current_familiar = 0

driver.get("http://www1.flightrising.com/")

start_login = driver.find_element_by_id("login-button")

action_chains.move_to_element(start_login).click(start_login).perform()

username = driver.find_element_by_id("uname")
password = driver.find_element_by_xpath("//input[@name='pword']")
login = driver.find_element_by_xpath("//input[@value='Login']")

username.send_keys(username_input)
password.send_keys(password_input)
action_chains.move_to_element(login).click(login).perform()
print "Logging in..."

wait.until(EC.text_to_be_present_in_element((By.XPATH, "//span[@id='namespan']//span"), "Avonyel"))

lair_link = driver.find_element_by_xpath("//a[@href='http://www1.flightrising.com/lair']")
action_chains.move_to_element(lair_link).click(lair_link).perform()
print "Entering lair page."

wait.until(EC.text_to_be_present_in_element((By.XPATH, "//span[@style='font-size:22px; text-align:left; color:#731d08; font-weight:bold; position:absolute; top:20px; left:52px;']"), "Avonyel's Dragons"))

dragon_link = driver.find_element_by_xpath("//img[@src='/rendern/avatars/11070/1106991.png?mtime=VAf0ewAAOcw']")
action_chains.move_to_element(dragon_link).click(dragon_link).perform()
print "Entering dragon page."

wait.until(EC.text_to_be_present_in_element((By.XPATH, "//span[@style='font-size:22px; text-align:left; color:#731d08; font-weight:bold; position:absolute; top:20px; left:52px;']"), "Kirigiri"))

while current_dragon < num_dragons:
    time.sleep(5)

    try:
        bond_btn = driver.find_element_by_xpath("//img[@src='../images/layout/button_bond.png']")
        action_chains.move_to_element(bond_btn).click(bond_btn).perform()
    except:
        print "Bond button not found or familiar already bonded."

    time.sleep(5)

    try:
        okay_btn = driver.find_element_by_id("no")
        action_chains.move_to_element(okay_btn).click(okay_btn).perform()
    except:
        "No okay button found. That's okay though. Wait."

    time.sleep(5)

    next_dragon_btn = driver.find_element_by_id("buttonnext")
    action_chains.move_to_element(next_dragon_btn).click(next_dragon_btn).perform()

    current_dragon += 1

while current_familiar < num_familiars:
    print "Bonding with familiar #%d" % current_familiar

    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@src='http://flightrising.com/images/layout/button_change.png']")))

        change_fam_btn = driver.find_element_by_xpath("//img[@src='http://flightrising.com/images/layout/button_change.png']")
        action_chains.move_to_element(change_fam_btn).click(change_fam_btn).perform()
        print "Clicked the change familiar button."
        wait.until(EC.text_to_be_present_in_element((By.XPATH, "//span[@style='font-size:22px; text-align:left; color:#731d08; font-weight:bold; position:absolute; top:20px; left:52px;']"), "Choose Familiar"))
    except:
        print "Familiar not changing. Refreshing...\a"
        driver.get("http://flightrising.com/main.php?p=lair&id=25331&tab=dragon&did=1106991")
        continue

    while True:
        try:
            next_familiar = driver.find_element_by_xpath("//a[@rel='includes/itemajax.php?id=%d&tab=familiar']" % familiar_array[current_familiar])
            driver.execute_script("arguments[0].click()", next_familiar)
            print "Found familiar, hallelujah!"
        except:
            print "Could not find familiar #%d." % familiar_array[current_familiar]
    
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='familiar']/img[@src='/images/cms/familiar/art/%d.png']" % familiar_array[current_familiar])))
            break
        except:
            print "Familiar page hanging. Reloading.\a"
            driver.save_screenshot('familiar_problem.png')
            driver.find_element_by_tag_name("body").send_keys(Keys.F5)

    back_btn = driver.find_element_by_xpath("//img[@src='/images/layout/button_back.png']")
    action_chains.move_to_element(back_btn).click(back_btn).perform()
    print "Clicked back button."

    while True:
        try:
            wait.until(EC.text_to_be_present_in_element((By.XPATH, "//span[@style='font-size:22px; text-align:left; color:#731d08; font-weight:bold; position:absolute; top:20px; left:52px;']"), "Kirigiri"))
            break
        except:
            print "Not returning to dragon page. Refreshing..."
            driver.get("http://flightrising.com/main.php?p=lair&id=25331&tab=dragon&did=1106991")


    try:
        bond_btn = driver.find_element_by_xpath("//img[@src='../images/layout/button_bond.png']")
        action_chains.move_to_element(bond_btn).click(bond_btn).perform()
        print "Bonded."
        wait.until(EC.element_to_be_clickable((By.ID, "no")))
    except:
        print "Bond button not found or familiar already bonded."
        driver.save_screenshot('bonding_fail.png')

    try:
        okay_btn = driver.find_element_by_id("no")
        action_chains.move_to_element(okay_btn).click(okay_btn).perform()
        print "Hit okay."
        wait.until(EC.invisibility_of_element_located((By.ID, "bonding")))
    except:
        "No okay button found. That's okay though. Wait."

    current_familiar += 1

driver.quit()