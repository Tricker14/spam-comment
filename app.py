from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, UnexpectedAlertPresentException, ElementClickInterceptedException, TimeoutException, WebDriverException

class App:
    def __init__(self):
        
        self.urls = [
            "http://aikenlandscaping.com/009-2/",
            "http://fit.trianh.edu.vn/phong-thi-nghiem-an-toan-thong-tin/",  
            "https://www.golfonline.sk/odborne-clanky/greenkeeping/plesen-snezna-a-plesen-snezna-siva/", 
            "https://mru.home.pl/produkt/afriso-tm8-ir/#reviews",
            "https://www.fivereasonssports.com/news/4-types-of-candy-most-adults-will-like/",
            "https://www.lizsteel.com/a-new-favourite-teapot-to-sketch/",
            "https://www.neobienetre.fr/forum-bien-etre-medecines-douces-developpement-personnel/topic/play-game-for-fun/",
            "https://bulevard.bg/interviews/ivaylo-zahariev-v-ekskluzivno-intervyu-19.html",

        ]
        
        self.selectors = {
            "author": [
                "input[type='text'][name*='author' i]",
                "input[type='text'][name*='name' i]", 
                "input[name*='name' i]",
                "input[id*='name' i]",
                "input[type='text']"],
            "email": [
                "input[type='text'][name*='mail' i]", 
                "input[name*='mail' i]", 
                "input[id*='mail' i]",
                "input[type='email']"],
            "phone": [
                "input[type='text'][name*='url' i]",  
                "input[name*='url' i]",
                "input[type='text']"],
            "website": [
                "input[type='text'][name*='url' i]",  
                "input[name*='url' i]",
                "input[type='text']"],
            "comment": [
                "textarea[name*='comment' i]", 
                "input[type='text'][name*='comment' i]",  
                "input[name*='comment' i]",
                "textarea",
                "input[type='text']"],
            "submit": [
                "input[type='submit'][name*='submit' i]", 
                "input[type='submit']", 
                "input[name*='submit' i]",
                "span"],
        }

        # Initialize the Chrome WebDriver 
        self.start_driver()
        self.total = 0
        self.passed = 0

    def start_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.sensors": 2})
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--accept_insecure_certs")
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--allow-insecure-localhost")
        chrome_options.add_argument("--ignore-certificate-errors")

        self.driver = webdriver.Chrome(options=chrome_options)

    def restart_driver(self):
        self.driver.quit()
        self.start_driver()

    def run(self):
        try:
            for url in self.urls:
                self.total += 1
                print("passed ", self.passed, "/", self.total)
                try:
                    # Open the website
                    self.driver.get(url)

                    WebDriverWait(self.driver, 1)

                    # Check if CAPTCHA is present (example: looking for a CAPTCHA element)
                    if self.is_captcha_present():
                        print("CHECK URL ", url)
                        continue

                    try:
                        # Find the comment form elements using selectors
                        name_field = self.find_element_by_any_selector(self.selectors["author"])
                        email_field = self.find_element_by_any_selector(self.selectors["email"])
                        phone_field = self.find_element_by_any_selector(self.selectors["phone"])
                        comment_box = self.find_element_by_any_selector(self.selectors["comment"])
                        submit_button = self.find_element_by_any_selector(self.selectors["submit"])

                        if not all([comment_box, name_field, email_field, phone_field, submit_button]):
                            print("nothing")
                            continue
                        else:
                            if name_field:
                                name_field.send_keys("Nhu")
                            if email_field:
                                email_field.send_keys("nhu@shemail.com")
                            if phone_field:
                                phone_field.send_keys("0398748129")
                            if comment_box:
                                comment_box.send_keys("Hello world.")
                        
                            # Submit the comment
                            if submit_button:
                                submit_button.click()
                    except ElementClickInterceptedException as e:
                        print(f"Cant click submit button {url}: {e}")
                        continue

                    except ElementNotInteractableException as e:
                        print(f"Failed to interact with element on {url}: {e}")
                        continue

                    except WebDriverException as e:
                        print(f"Connection timeout {url}: {e}")
                        continue

                except (TimeoutException) as e:
                    print(f"Page load failed on URL {url}: {e}")
                    continue
                except UnexpectedAlertPresentException:
                    print(f"Unexpected alert encountered on URL {url}")
                    continue
                except WebDriverException as e:
                    print(f"Connection timeout {url}: {e}")
                    continue
                print(f"PASSED {url}")
                self.passed += 1

        finally:
            # Close the browser session
            print("finished ", self.passed)
            self.driver.quit()

    def find_element_by_any_selector(self, selectors):
        for selector in selectors:
            try:
                element = self.driver.find_element(By.CSS_SELECTOR, selector)
                if element and element.is_displayed() and element.is_enabled():
                    return element
            except Exception as e:
                print(f"Failed to find element with selector {selector}: {e}")

    def is_captcha_present(self):
        try:
            # Example: Check for CAPTCHA element presence by some unique identifier
            captcha_element = self.driver.find_element(By.ID, "captcha-element-id")
            return True
        except NoSuchElementException:
            return False



if __name__ == "__main__":
    App().run()