import os
import undetected_chromedriver as uc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
class Certidao:
    
    def __init__(self):
        options = uc.ChromeOptions()
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument("--disable-popup-blocking")
        options.add_argument('--no-first-run')
        options.add_argument("--window-size=2560,1440")
        options.add_argument('--no-sandbox')
        self.navegador = uc.Chrome(options=options,version_main=123)
        # self.navegador.get("https://registrocivil.org.br/login")
        # self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/form/div[2]/input').send_keys('certidao1@originalprecatorios.com.br')
        # self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/form/div[3]/div/input').send_keys('Gestaodedocs24*')
        # self.navegador.find_element(By.CLASS_NAME, 'btn-primary').click()
        time.sleep(4)
    def tipo_certidao(self, tipo):
        if tipo == 'casamento':
            self.certida_casamento()
        elif tipo == 'obito':
            self.certidao_obito()
        elif tipo == 'nascimento':
            self.certidao_nascimento()
    def certidao_nascimento(self):
        self.navegador.get(f"https://registrocivil.org.br/birth-certificate")
        self.navegador.find_elements(By.CLASS_NAME, 'multiselect__tags')[0].click()
        self.navegador.find_elements(By.CLASS_NAME, 'multiselect__tags')[0].click()
        self.navegador.find_element(By.ID, 'adopt-accept-all-button').click()
        time.sleep(2)
        
        lista = self.navegador.find_elements(By.TAG_NAME,'span')
        for va in lista:
            if va.text.find('São Paulo')>-1:
                va.click()
        self.navegador.find_elements(By.CLASS_NAME, 'multiselect__tags')[1].click()
        lista = self.navegador.find_elements(By.CLASS_NAME, 'multiselect__element')
        for va in lista:
            if  va.text.find('São Paulo')>-1:
                va.click()
        self.navegador.find_elements(By.CLASS_NAME, 'multiselect__tags')[2].click()
        lista = self.navegador.find_elements(By.CLASS_NAME, 'multiselect__element')
        for va in lista:
            if va.text.find('Capão Redondo - Distrito do Município de São Paulo')>-1:
                va.click()
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div/div/button[2]').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/input').send_keys('teste')
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/input').send_keys('07/08/2001')
        
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/input').send_keys(50462746801)
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[3]/div[1]/input').send_keys('teste')
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/input').send_keys('teste')
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/input').send_keys('teste')
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div/div/button[2]').click()
        self.navegador.find_element(By.XPATH, '//*[@id="txtBookNumber"]').send_keys(26262)
        self.navegador.find_element(By.XPATH, '//*[@id="txtSheetNumber"]').send_keys(262)
        self.navegador.find_element(By.XPATH, '//*[@id="txtTermNumber"]').send_keys(2622522)
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div/div/button[2]').click()
        self.navegador.find_elements(By.CLASS_NAME, 'lbl-card')[1].click()
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div/div/button[2]').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[8]/div[1]/div/label/b').click()
        self.navegador.find_element(By.ID, 'adopt-accept-all-button').click()
        time.sleep(1)
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/button[2]').click()
        time.sleep(1)
        
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[4]/button[2]').click()
        time.sleep(1)
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/form/div[2]/input').send_keys('certidao1@originalprecatorios.com.br')
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/form/div[3]/div/input').send_keys('Gestaodedocs24*')
        self.navegador.find_element(By.CLASS_NAME, 'btn-primary').click()
        time.sleep(5)
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[4]/button[2]').click()
        time.sleep(2)
        self.navegador.find_element(By.XPATH, '//*[@id="payment-method-card"]').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[4]/div/button[2]').click()
        
        
        
        
        
        
        
        
        
        
    def certida_casamento(self):
        self.navegador.get(f"https://registrocivil.org.br/marriage-certificate")
        self.navegador.find_elements(By.CLASS_NAME, 'multiselect__tags')[0].click()
        self.navegador.find_elements(By.CLASS_NAME, 'multiselect__tags')[0].click()
        time.sleep(2)
        self.navegador.find_element(By.ID, 'adopt-accept-all-button').click()
        lista = self.navegador.find_elements(By.TAG_NAME,'span')
        for va in lista:
            if va.text.find('São Paulo')>-1:
                va.click()
        self.navegador.find_elements(By.CLASS_NAME, 'multiselect__tags')[1].click()
        lista = self.navegador.find_elements(By.CLASS_NAME, 'multiselect__element')
        for va in lista:
            if  va.text.find('São Paulo')>-1:
                va.click()
        self.navegador.find_elements(By.CLASS_NAME, 'multiselect__tags')[2].click()
        lista = self.navegador.find_elements(By.CLASS_NAME, 'multiselect__element')
        for va in lista:
            if va.text.find('Capão Redondo - Distrito do Município de São Paulo')>-1:
                va.click()
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div/div/button[2]').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div/input').send_keys('24/12/2001')
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/input').send_keys('teste')
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/input').send_keys('teste')
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div/div/button[2]').click()
        self.navegador.find_element(By.XPATH, '//*[@id="txtBookNumber"]').send_keys(2655)
        self.navegador.find_element(By.XPATH, '//*[@id="txtSheetNumber"]').send_keys(265)
        self.navegador.find_element(By.XPATH, '//*[@id="txtTermNumber"]').send_keys(2828222)
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div/div/button[2]').click()
        self.navegador.find_elements(By.CLASS_NAME, 'lbl-card')[1].click()
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div/div/button[2]').click()
        self.navegador.find_element(By.ID, 'adopt-accept-all-button').click()
        time.sleep(1)
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[7]').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/button[2]').click()
        time.sleep(1)
        
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[4]/button[2]').click()
        time.sleep(1)
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[1]').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[4]/div/button[2]').click()
    def certidao_obito(self):
        self.navegador.get(f"https://registrocivil.org.br/death-certificate")
        self.navegador.find_elements(By.CLASS_NAME, 'multiselect__tags')[0].click()
        self.navegador.find_elements(By.CLASS_NAME, 'multiselect__tags')[0].click()
        time.sleep(2)
        self.navegador.find_element(By.ID, 'adopt-accept-all-button').click()
        lista = self.navegador.find_elements(By.TAG_NAME,'span')
        for va in lista:
            if va.text.find('São Paulo')>-1:
                va.click()
        self.navegador.find_elements(By.CLASS_NAME, 'multiselect__tags')[1].click()
        lista = self.navegador.find_elements(By.CLASS_NAME, 'multiselect__element')
        for va in lista:
            if  va.text.find('São Paulo')>-1:
                va.click()
        self.navegador.find_elements(By.CLASS_NAME, 'multiselect__tags')[2].click()
        lista = self.navegador.find_elements(By.CLASS_NAME, 'multiselect__element')
        for va in lista:
            if va.text.find('Capão Redondo - Distrito do Município de São Paulo')>-1:
                va.click()
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div/div/button[2]').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div/div[1]/input').send_keys('teste')
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]/div/input').send_keys('24/12/2011')
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div/div/button[2]').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/div/input').send_keys('teste')
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/input').send_keys('teste')
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/button[2]').click()
        self.navegador.find_element(By.XPATH, '//*[@id="txtBookNumber"]').send_keys(36525)
        self.navegador.find_element(By.XPATH, '//*[@id="txtSheetNumber"]').send_keys(365)
        self.navegador.find_element(By.XPATH, '//*[@id="txtTermNumber"]').send_keys(3653698)
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div/div/button[2]').click()
        self.navegador.find_elements(By.CLASS_NAME, 'lbl-card')[1].click()
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div/div/button[2]').click()
        self.navegador.find_element(By.ID, 'adopt-accept-all-button').click()
        time.sleep(1)
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[7]').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/button[2]').click()
        time.sleep(1)
        
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[4]/button[2]').click()
        time.sleep(1)
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/form/div[2]/input').send_keys('certidao1@originalprecatorios.com.br')
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/form/div[3]/div/input').send_keys('Gestaodedocs24*')
        self.navegador.find_element(By.CLASS_NAME, 'btn-primary').click()
        time.sleep(5)
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[4]/button[2]').click()
        time.sleep(2)
        self.navegador.find_element(By.XPATH, '//*[@id="payment-method-card"]').click()
        self.navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[4]/div/button[2]').click()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # forms[0].click()
        # [next(i.click() for i in lista if 'São Paulo' in i.text)]
        # forms[1].click()
        # lista1 = self.navegador.find_elements(By.TAG_NAME,'span')
        # for list in lista1:
        #     if list.text.find('São Paulo')>0:
        #         list.click()
        # forms[2].click()

        
        