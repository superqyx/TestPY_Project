import selenium
import selenium.webdriver

browser = selenium.webdriver.Chrome()
browser.get("http://www.baidu.com")
browser.get_screenshot_as_file("baidu.png")

def func(self):
    print("hello world")

Foo = type("Foo",(object,),{'func':func})