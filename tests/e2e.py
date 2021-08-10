import sys
import urllib.request
from selenium import webdriver


def test_url(url):
    try:
        status_code = urllib.request.urlopen(url).getcode()
    except:
        status_code = 400
    return status_code


def test_scores_service(url):
    status_code = test_url(url)
    if status_code == 200:
        my_driver = webdriver.Chrome(executable_path="c:/chromedriver.exe")
        my_driver.get(url)
        my_score = int(my_driver.find_element_by_id("score").text)
        if 0 < my_score < 1001:
            return True
        return False
    return False


def main_function(url):
    if test_scores_service(url):
        sys.exit(0)
    else:
        sys.exit(-1)



url = " http://127.0.0.1:5000/"
main_function(url)
