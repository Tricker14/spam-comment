import tkinter as tk
from tkinter import scrolledtext, messagebox
from threading import Thread
from app import App
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, UnexpectedAlertPresentException, ElementClickInterceptedException, TimeoutException, WebDriverException

class URLScannerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Commenter")

        self.app = App()

        # URL input field
        self.url_label = tk.Label(root, text="Enter URLs (separated by new lines):")
        self.url_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        self.url_entry = scrolledtext.ScrolledText(root, width=60, height=10)
        self.url_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Add default URLs from the app
        self.url_entry.insert(tk.END, "\n".join(self.app.urls))

        # Start button
        self.start_button = tk.Button(root, text="Start", command=self.start_scanning)
        self.start_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="NSEW")

        # Progress labels
        self.progress_label = tk.Label(root, text="Progress: 0/0")
        self.progress_label.grid(row=3, column=0, padx=10, pady=10, sticky="W")

        self.success_label = tk.Label(root, text="Success: 0")
        self.success_label.grid(row=3, column=1, padx=10, pady=10, sticky="W")

        # Status display
        self.status_frame = tk.Frame(root)
        self.status_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.url_listbox = tk.Listbox(self.status_frame, width=60)
        self.url_listbox.grid(row=0, column=0, padx=10, pady=10)

        self.status_listbox = tk.Listbox(self.status_frame, width=40)
        self.status_listbox.grid(row=0, column=1, padx=10, pady=10)

        # Scrollbar for listboxes
        self.scrollbar = tk.Scrollbar(self.status_frame, orient="vertical", command=self.on_scroll)
        self.scrollbar.grid(row=0, column=2, sticky="ns")

        self.url_listbox.config(yscrollcommand=self.scrollbar.set)
        self.status_listbox.config(yscrollcommand=self.scrollbar.set)

    def on_scroll(self, *args):
        self.url_listbox.yview(*args)
        self.status_listbox.yview(*args)

    def start_scanning(self):
        urls = self.url_entry.get("1.0", tk.END).strip().split("\n")
        self.app.urls = urls

        self.total_urls = len(urls)
        self.scanned_urls = 0
        self.success_count = 0

        self.update_progress()
        self.update_status_listboxes(urls)

        # Start the scanning in a separate thread
        self.scan_thread = Thread(target=self.run_scanning)
        self.scan_thread.start()


    def run_scanning(self):
        try:
            for url in self.app.urls:
                self.scanned_urls += 1
                self.update_progress()
                print("\n\n")
                print("[PASSED]:\t\t", self.success_count, "/", self.total_urls)

                try:
                    # Process the URL
                    self.app.driver.get(url)
                    WebDriverWait(self.app.driver, 2)
                    print("[CURRENT]:\t\t", url)

                    if self.app.is_captcha_present():
                        self.update_status(url, "Failed (CAPTCHA)")
                        continue
                    # if len(self.app.find_form_elements(self.app.selectors["submit"])) > 1:
                    #     print("too many forms")
                    #     continue
                    try:
                        name_field = self.app.find_element_by_any_selector(self.app.selectors["author"])
                        email_field = self.app.find_element_by_any_selector(self.app.selectors["email"])
                        phone_field = self.app.find_element_by_any_selector(self.app.selectors["phone"])
                        website_field = self.app.find_element_by_any_selector(self.app.selectors["website"])
                        comment_box = self.app.find_element_by_any_selector(self.app.selectors["comment"])
                        submit_button = self.app.find_element_by_any_selector(self.app.selectors["submit"])

                        if not any([comment_box, name_field, email_field, phone_field, submit_button]):
                            self.update_status(url, "Failed (Elements not found)")
                            print("[FAILED]:\t\tElements not found")
                            continue
                        else:
                            if name_field:
                                name_field.send_keys("Eaton Park Quận 2")
                            if email_field:
                                email_field.send_keys("eatonpark@gmail.com")
                            if phone_field:
                                phone_field.send_keys("0398748129")
                            if website_field:
                                website_field.send_keys("https://canhoeatonpark.net/")
                            if comment_box:
                                comment_box.send_keys("<a href='https://canhoeatonpark.net/'>Eaton Park Quận 2</a> Eaton Park Quận 2 là dự án mới nhất của Gamuda Land, được phát triển với vị trí độc đáo ngay trên đường Mai Chí Thọ, Phường An Phú, Quận 2, nay thuộc TP Thủ Đức – TP Hồ Chí Minh")
                        
                            # Submit the comment
                            if submit_button:
                                time.sleep(1)
                                submit_button.click()
                                time.sleep(1)
                    
                    except ElementClickInterceptedException:
                        self.update_status(url, "Failed (Click Interception)")
                        print("[FAILED]:\t\tElementClickInterceptedException called")
                        continue
                    except ElementNotInteractableException:
                        self.update_status(url, "Failed (Element Not Interactable)")
                        print("[FAILED]:\t\tElementNotInteractableException called")
                        continue
                    except WebDriverException as e:
                        if 'out of memory' in str(e):
                            self.update_status(url, "Failed (Out of Memory)")
                            print("[FAILED]:\t\tOut of Memory Error called")
                        else:
                            self.update_status(url, "Failed (WebDriver Error)")
                            print("[FAILED]:\t\tWebDriverException called")
                        continue

                except TimeoutException:
                    self.update_status(url, "Failed (Timeout)")
                    print("[FAILED]:\t\tTimeout called")
                    self.app.restart_driver()
                    continue
                except UnexpectedAlertPresentException:
                    self.update_status(url, "Failed (Unexpected Alert)")
                    print("[FAILED]:\t\tUnexpectedAlertPresentException called")
                    continue
                except WebDriverException as e:
                    if 'out of memory' in str(e):
                        self.update_status(url, "Failed (Out of Memory)")
                        print("[FAILED]:\t\tOut of Memory Error called")
                    else:
                        self.update_status(url, "Failed (WebDriver Error)")
                        print("[FAILED]:\t\tWebDriverException called")
                    self.app.restart_driver()
                    continue

                if self.app.check_comment_posted(url, "Eaton Park Quận 2</a> Eaton Park Quận 2 là dự án mới nhất của Gamuda Land, được phát triển với vị trí độc đáo ngay trên đường Mai Chí Thọ, Phường An Phú, Quận 2, nay thuộc TP Thủ Đức – TP Hồ Chí Minh"):
                    # print(f"Success {url}")
                    self.update_status(url, "Success")
                    self.success_count += 1
                    self.update_success_count()
                    print(f"[SUCCESS]:\t\t{url}")
                else:
                    self.update_status(url, "Failed (Check Success Failed)")
                    print("[FAILED]:\t\tCheck Success Failed")

        finally:
            self.app.driver.quit()
            messagebox.showinfo("Info", "Scanning completed")

    def update_progress(self):
        self.progress_label.config(text=f"Progress: {self.scanned_urls}/{self.total_urls}")

    def update_success_count(self):
        self.success_label.config(text=f"Success: {self.success_count}")

    def update_status(self, url, status):
        index = self.app.urls.index(url)
        self.status_listbox.delete(index)
        self.status_listbox.insert(index, status)

    def update_status_listboxes(self, urls):
        self.url_listbox.delete(0, tk.END)
        self.status_listbox.delete(0, tk.END)
        for url in urls:
            self.url_listbox.insert(tk.END, url)
            self.status_listbox.insert(tk.END, "Pending")


if __name__ == "__main__":
    root = tk.Tk()
    gui = URLScannerGUI(root)
    root.mainloop()
