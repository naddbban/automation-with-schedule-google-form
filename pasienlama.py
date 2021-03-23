from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import schedule

time.sleep(1)

def reservasi():
    options = Options()
    options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    driver_path = "chromedriver.exe"
    web = webdriver.Chrome(options = options, executable_path = driver_path)
    web.get('https://docs.google.com/forms/d/e/1FAIpQLSfuVxcUB5YU1BAo1Y2U-C-o5purJqaD7PP_Qtqf8Ps-bKWWMA/viewform')

    Nama = "Arida periode 10"
    NoHp = "08978095095"
    DosenP = "Drg. arny"
    Tindakan = "indikasi psa"
    NamaPasien = "erika"
    NoRekamMedis = "6904"

    ######### Pagi #########
    #ShiftKerja = web.find_element_by_xpath('//*[@id="i7"]/div[3]/div')
    #ShiftKerja.click()

    ######### Siang #########
    ShiftKerja = web.find_element_by_xpath('//*[@id="i10"]/div[3]/div')
    ShiftKerja.click()

    nama = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    nama.send_keys(Nama)

    no = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    no.send_keys(NoHp)

    dosen = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    dosen.send_keys(DosenP)

    Keperluan = web.find_element_by_xpath('//*[@id="i29"]/div[3]/div')
    Keperluan.click()

    Next1 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    Next1.click()

    time.sleep(0.5)

    tindak = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')
    tindak.send_keys(Tindakan)


    ######### Non Aerosol #########
    #RencanaKerja = web.find_element_by_xpath('//*[@id="i12"]/div[3]/div')
    #RencanaKerja.click()

    ######### Aerosol #########
    RencanaKerja = web.find_element_by_xpath('//*[@id="i9"]/div[3]/div')
    RencanaKerja.click()

    Next2 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    Next2.click()

    Pasien = web.find_element_by_xpath('//*[@id="i8"]/div[3]/div')
    Pasien.click()

    Next3 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    Next3.click()

    time.sleep(0.5)

    namaP = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    namaP.send_keys(NamaPasien)

    medis = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    medis.send_keys(NoRekamMedis)

    time.sleep(0.5)

    Submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    Submit.click()

    g = [1,2,3,4,5,6,7,8,9,10]

    for i in g:
        web.refresh()
        act = ActionChains(web)
        act.send_keys(Keys.F5).send_keys(Keys.ENTER).perform()
        print("reservasi ke", i)
 

schedule.every().day.at("07:29:47").do(reservasi)

while True:
    schedule.run_pending()
    time.sleep(1)