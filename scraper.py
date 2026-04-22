from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def run_scraper():
    print("Запуск автоматичного скрапера...")
    

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        
        url = "http://127.0.0.1:8000/"
        print(f"Переходимо за адресою: {url}")
        driver.get(url)
        
        
        time.sleep(2) 
        
       
        page_title = driver.title
        
       
        print("\n" + "="*40)
        print(f"[SUCCESS] Скрапінг успішний!")
        print(f"Заголовок сайту: '{page_title}'")
        print("="*40 + "\n")
        
    except Exception as e:
        print(f"\n[ERROR] Щось пішло не так: {e}")
    finally:

        time.sleep(2)
        driver.quit()
        print("Браузер закрито.")

if __name__ == "__main__":
    run_scraper()