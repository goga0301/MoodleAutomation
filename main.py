from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
from os import listdir
from os.path import isfile, join

PATH = r"C:\Program Files\chromedriver.exe"


def makedir(name):
    filepath = f"C:/Users/GOGA/Desktop/Java/{name}"

    try:
        os.mkdir(filepath)
    except OSError:
        print("Creation of the directory %s failed" % filepath)

    else:
        print("Successfully created the directory %s " % filepath)


def movefile(filepath):

    mypath = r"C:\Users\GOGA\Desktop\Java"

    files = [f for f in listdir(mypath) if isfile(
        join(mypath, f))]

    for file in checkfile(mypath):
        os.replace(f"C:/Users/GOGA/Desktop/Java/{file}",
                   "C:/Users/GOGA/Desktop/Java/{}/{}".format(filepath, file))


def checkfile(path):
    mypath = r"C:\Users\GOGA\Desktop\Java"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    for file in onlyfiles:

        if ".zip" in file or ".pptx" in file or ".pdf" in file or ".rar" in file:
            print(f"True {file}")
            boolean = True
        else:

            onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
            print(f"False {file}")
            sleep(2)
            return checkfile(mypath)
    return onlyfiles


download_dir = r"C:\Users\GOGA\Desktop\Java"
chrome_options = webdriver.ChromeOptions()
preferences = {"download.default_directory": download_dir,
               "directory_upgrade": True,
               "safebrowsing.enabled": True}
chrome_options.add_experimental_option("prefs", preferences)
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=PATH)
driver.get("https://www.xn--rodeaj1ar.xn--node/moodle/login/index.php")
username = driver.find_element_by_id("username")
username.send_keys("goga200330023@gmail.com")
password = driver.find_element_by_id("password")
password.send_keys("Goga.2003.goga")
loginbt = driver.find_element_by_id("loginbtn")
loginbt.click()


course = driver.find_element_by_link_text(
    "პროგრამირების ენა Java (მეორე დონე) ბ.ჭელიძე")
course.click()


sections = driver.find_elements_by_class_name("section")
i = 1
mainurl = driver.current_url
while(i < len(sections)):
    filename = driver.find_elements_by_css_selector(".sectionname span")

    print(filename[i].text)
    makedir(filename[i].text)
    theory = driver.find_elements_by_css_selector(f"#section-{i} a")
    j = 0
    while(j < len(theory)):
        theory = driver.find_elements_by_css_selector(f"#section-{i} a")
        print(f"index -- {j}")
        theory[j].click()

        if driver.current_url[-4:] == ".sql":
            print("sql")
            j += 1
            driver.back()
            continue
        if(driver.current_url != mainurl):
            print("amocanebi")
            homeworks = driver.find_elements_by_css_selector(
                "#ygtvcontentel1 a")
            for a in homeworks:

                a.click()

            driver.back()
            filename = driver.find_elements_by_css_selector(
                ".sectionname span")
            movefile(filename[i].text)
        else:
            print("teoria")
            filename = driver.find_elements_by_css_selector(
                ".sectionname span")
            movefile(filename[i].text)
        j += 1

    i += 1
    sleep(3)
