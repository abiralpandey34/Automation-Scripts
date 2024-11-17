import pickle
from sqlite3 import connect

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

email = "" # Provide Email Here
password = "" # Provide Password Here

def Login():
    input_element = driver.find_element('css selector','input[placeholder="Username, phone or email"]')
    input_element.send_keys(email)

    try:
        password_element = driver.find_element('css selector', 'input[placeholder="Password"]')
        password_element.send_keys(password)

        login_element = driver.find_element(
        'xpath',
        '//div[text()="Log in"]'
        )
        login_element.click()
        time.sleep(10)


    except:
        login_element = driver.find_element(
        'xpath',
        '//div[text()="Log in"]')

        login_element.click()
        time.sleep(5)

        password_element = driver.find_element('css selector', 'input[placeholder="Password"]')    
        password_element.send_keys("Qi@k@A12")

        login_element = driver.find_element(
            'xpath',
            '//div[text()="Log in"]'
        )
        login_element.click()

def SaveCookie():
    with open("cookies.pkl", "wb") as file:
        pickle.dump(driver.get_cookies(), file)

def LoadCookie():
    with open("cookies.pkl", "rb") as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
    
    driver.refresh()

def LoadAllContent():
    max_scrolls = 12
    scrolls = 0

    while scrolls < max_scrolls:
        scrolls += 1
        print(f"Scrolling {scrolls}...")

        # Get the current scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")

        # Check if new content was loaded (height change)
        if new_height == last_height:
            print("No more content to load. Stopping.")
            return


def save_to_db(date, posttt_time, post, like, comment, repost):
    try:
        conn = connect('in_dark_reality.db')
        cursor = conn.cursor()
        # Create the table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                time TEXT,
                post TEXT,
                like TEXT,
                comment TEXT,
                repost TEXT
            )
        """)
        
        # Parameterized query
        cursor.execute("""
            INSERT INTO posts (date, time, post, like, comment, repost)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (date, posttt_time, post, like, comment, repost))  # Pass values as a tuple
        
        conn.commit()
        conn.close()
        print("Added to DB successfully")
    except Exception as e:
        print("DB not working for:\n")
        print("Error:", e)


driver.get("https://www.threads.net/login/")

LoadCookie()
driver.get("https://www.threads.net/@in.dark.reality")
LoadAllContent()

elements = driver.find_elements('xpath', '//*[@data-pressable-container="true"]')

all_post = []
all_date = []
all_time = []
all_like = []
all_comment = []
all_repost = []

print(f"Total Number of Posts are: {len(elements)}")


for element in elements:

    post_div = element.find_element('xpath', './div/div[3]/div/div[1]')

    like_text = 0
    comment_text = 0
    repost_text = 0

    if(len(str(post_div.text)) > 1 ):
        print("\nText Post Found----------------")
        try:
            indicator_div = element.find_element('xpath', './div/div[3]/div/div[2]')
            temp_div = indicator_div.find_elements('xpath','./div/div')

            i = 0
            for temp in temp_div:
                try:
                    if(i!=3):
                        value_div = temp.find_elements(By.TAG_NAME, 'span')[0]
                    if(i==0):
                        like_text = value_div.text
                    elif(i==1):
                        comment_text = value_div.text
                    elif(i==2):
                        repost_text = value_div.text
                    else:
                        pass
                except:
                    print("-")
                
                finally:
                    i+=1

            # print(f"\nPost is: {post_div.text}")
            # print(f"The Likes are: {like_text}")
            # print(f"The Comment are: {comment_text}")
            # print(f"The Repost are: {repost_text}")
        except:
            print("\nIndicator Div wasn't Found - This message shouldn't be displayed")
    else:
        print("\nIt is a image post")



    # Extracting Date / Time
    time_div = element.find_element('tag name', 'time')
    time_title = time_div.get_attribute('title')
    post_date = time_title.split(",")[0]
    post_time = time_title.split(",")[1]


    if(len(str(post_div.text)) > 1):
        all_post.append(post_div.text)
        all_date.append(post_date)
        all_time.append(post_time)

        all_like.append(like_text)
        all_comment.append(comment_text)
        all_repost.append(repost_text)


j = 0
while j < len(all_post):
    save_to_db(all_date[j], all_time[j], all_post[j], all_like[j], all_comment[j], all_repost[j])
    j += 1
    time.sleep(0.2)


time.sleep(4)
time.sleep(10)
driver.quit()


