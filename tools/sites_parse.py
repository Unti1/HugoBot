from settings import *

class Parser():
    def __init__(self):
        self.driver:webdriver.Chrome = None
        self.browser_startUp(PROFILE_ID = config["Parser"]["profile_id"],invisable=True)
        self.wait = WebDriverWait(self.driver,15)
        self.kwork_data = {}

    def browser_startUp(self, PROFILE_ID,invisable):
        """Создание настройка и создания эмуляции браузера
        """
        
        # Настройка браузера Google
        chrome_drive_path = Service('./settings/chromedriver-linux')
        options = webdriver.ChromeOptions()
        reg_url = f'http://localhost:3001/v1.0/browser_profiles/{PROFILE_ID}/start?automation=1'
        response = requests.get(reg_url)
        respons_json = response.json()
        PORT = str(respons_json['automation']['port'])
        options.debugger_address = '127.0.0.1:'+ PORT
        options.add_argument("window-size=1600,900")
        # Доп. параметры
        options.add_argument('--disable-logging')
        options.add_argument('--ignore-error')
        if invisable:
            options.add_argument('--headless')
        options.add_argument('--no-sandbox')

        self.driver = webdriver.Chrome(service=chrome_drive_path,chrome_options=options)
    
    async def kwork_parse(self):
        import time
        self.driver.get("https://kwork.ru/projects?a=1")
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@data-id]")))
        cards_len = len(self.driver.find_elements(By.XPATH,"//div[@data-id]"))
        print(cards_len)
        for ind in range(cards_len):
            card = self.driver.find_element(By.XPATH,f"//div[@data-id][{ind+1}]")
            if "показать полностью" in card.text.lower():
                more = self.driver.find_element(By.XPATH,f'//div[@data-id][{ind+1}]//span[@class="link_local"][1]')
                self.driver.execute_script("arguments[0].click();", more)
            title = self.driver.find_element(By.XPATH,f'//div[@data-id][{ind+1}]//a[1]').text
            link = self.driver.find_element(By.XPATH,f'//div[@data-id][{ind+1}]//a[1]').get_attribute("href")
            author = self.driver.find_elements(By.XPATH,f'//div[@data-id][{ind+1}]//a')[1].text
            cost = self.driver.find_element(By.XPATH,f'//div[@data-id][{ind+1}]//div[@class="wants-card__header-right-block"]').text
            description = self.driver.find_element(By.XPATH,f'//div[@data-id][{ind+1}]//div[@class="wants-card__description-text br-with-lh"]').text
            
            with open("data/block_keywords.txt","r") as fl:
                text = fl.read()
                block_keywords = text.split(", ")
            
            if title not in self.kwork_data.keys():
                for block_keyword in block_keywords:
                    if block_keyword not in title.lower() and block_keywords not in description.lower():
                        self.kwork_data[title] = {"link":link,"author":author,'cost': cost, 'description':description}
        return(self.kwork_data)
