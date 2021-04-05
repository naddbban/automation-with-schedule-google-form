from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import schedule

time.sleep(1)

#options = Options()
#options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
driver_path = "chromedriver.exe"
web = webdriver.Chrome( executable_path = driver_path)
web.get('https://docs.google.com/forms/d/e/1FAIpQLSfvlE_ZoOd_gbI53nDnUJE5ud2lfq5r6Giqfj1DvRqN6-tkig/viewform')

    # bekerja               # aerosol                       # nonaerosol                        # dokter
    # [1] aerosol           # [1]KURETASE                   # [1]KONTROL MJ                     # [1]drg. Laila N
    # [2] Non Aerosol       # [2]RESTORASI                  # [2]KONTROL PSA                    # [2]drg. Ariyani Faizah, MDSc
                            # [3]MJ (MAHKOTA JAKET)         # [3]KONTROL RESTORASI              # [3]drg. Juwita RN, MSc
                            # [4]PSA                        # [4]KONTROL KURETASE               # [4]drg. Lasmi Dewi, Sp.KGA
                            # [5]PULPEKTOMI                 # [5]KONTROL CABUT                  # [5]drg. Edi Karyadi, MM, MDSc, Sp.Perio
                            # [6]KONTROL PULPEKTOMI         # [6]EKSTRAKSI                      # [6]drg. Arny, Sp.KG
                            # [7]INLAY                      # [7]KONTROL EKSTRAKSI              # [7]drg. Nina Runting, Sp.BMM
                            # [8]INSERSI INLAY              # [8]EKSO                           # [8]drg. Pamungkas Handy M
                            # [9]KONTROL INLAY              # [9]KONTROL EKSO                   # [9]drg. Nur Rachmawati, Sp.Ort
                            # [10]PCC                       # [10]PL (PEMERIKSAAN LENGKAP)      # [10]drg. Iyop Ropika, MDSc., Sp.KGA
                            # [11]INSERSI                   # [11]INDIKASI MJ                   # [11]drg. Ikmal Hafizi, MDSc
                            # [12]ONLAY                     # [12]INNORKASI INLAY               # [12]drg. Nendika, MH
                            # [13]BUR TULANG                # [13]INDIKASI PSA                  # [13]drg. Septriyani K. MDSc. Sp.KGA
                            # [14]INDIKASI PULPEKTOMI       # [14]INDIKASI KURET
                                                            # [15]KONTROL ORTHO
                                                            # [16]KONTROL SCALLING

bekerja = 1

aerosol = 4

nonaerosol = 0

dokter = 6 

jam = "17:46:30"
Nama = "abajsas"
NoHp = "01234567"
DosenP = "Drg. Juwita"
NamaPasien = "Sabsg"
NoRekamMedis = "0000"

# Tindakan = "preparasi MJ dan Indikasi PSA"

######### Pagi #########
ShiftKerja = web.find_element_by_xpath('//*[@id="i7"]/div[3]/div')
ShiftKerja.click()

######### Siang #########
#ShiftKerja = web.find_element_by_xpath('//*[@id="i10"]/div[3]/div')
#ShiftKerja.click()

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

time.sleep(1)

# tindak = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')
# tindak.send_keys(Tindakan)

if bekerja == 1:
    RencanaKerja = web.find_element_by_xpath('//*[@id="i5"]/div[3]/div')
    RencanaKerja.click()

    Next2 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    Next2.click()

    if aerosol == 1:
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i8"]/div[3]/div')
        TindakanAerosol.click()
    elif aerosol == 2 :
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i11"]/div[3]/div')
        TindakanAerosol.click()
    elif aerosol == 3 :
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i14"]/div[3]/div')
        TindakanAerosol.click()
    elif aerosol == 4 :
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i17"]/div[3]/div')
        TindakanAerosol.click()
    elif aerosol == 5 :
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i20"]/div[3]/div')
        TindakanAerosol.click()
    elif aerosol == 6 :
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i23"]/div[3]/div')
        TindakanAerosol.click()
    elif aerosol == 7 :
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i26"]/div[3]/div')
        TindakanAerosol.click()
    elif aerosol == 8 :
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i29"]/div[3]/div')
        TindakanAerosol.click()
    elif aerosol == 9 :
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i32"]/div[3]/div')
        TindakanAerosol.click()
    elif aerosol == 10 :
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i35"]/div[3]/div')
        TindakanAerosol.click()
    elif aerosol == 11 :
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i38"]/div[3]/div')
        TindakanAerosol.click()
    elif aerosol == 12 :
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i41"]/div[3]/div')
        TindakanAerosol.click()
    elif aerosol == 13 :
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i44"]/div[3]/div')
        TindakanAerosol.click()
    elif aerosol == 14 :
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i47"]/div[3]/div')
        TindakanAerosol.click()

    Next3 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    Next3.click()

    time.sleep(1)

    if dokter == 1:
        PilihDokter = web.find_element_by_xpath('//*[@id="i5"]/div[3]/div')
        PilihDokter.click()
    elif dokter == 2:
        PilihDokter = web.find_element_by_xpath('//*[@id="i8"]/div[3]/div')
        PilihDokter.click()
    elif dokter == 3 :
        PilihDokter = web.find_element_by_xpath('//*[@id="i11"]/div[3]/div')
        PilihDokter.click()
    elif dokter == 4 :
        PilihDokter = web.find_element_by_xpath('//*[@id="i14"]/div[3]/div')
        PilihDokter.click()
    elif dokter == 5 :
        PilihDokter = web.find_element_by_xpath('//*[@id="i17"]/div[3]/div')
        PilihDokter.click()
    elif dokter == 6 :
        PilihDokter = web.find_element_by_xpath('//*[@id="i20"]/div[3]/div')
        PilihDokter.click()
    elif dokter == 7 :
        PilihDokter = web.find_element_by_xpath('//*[@id="i23"]/div[3]/div')
        PilihDokter.click()
    elif dokter == 8 :
        PilihDokter = web.find_element_by_xpath('//*[@id="i26"]/div[3]/div')
        PilihDokter.click()
    elif dokter == 9 :
        PilihDokter = web.find_element_by_xpath('//*[@id="i29"]/div[3]/div')
        PilihDokter.click()
    elif dokter == 10 :
        PilihDokter = web.find_element_by_xpath('//*[@id="i32"]/div[3]/div')
        PilihDokter.click()
    elif dokter == 11 :
        PilihDokter = web.find_element_by_xpath('//*[@id="i35"]/div[3]/div')
        PilihDokter.click()
    elif dokter == 12 :
        PilihDokter = web.find_element_by_xpath('//*[@id="i38"]/div[3]/div')
        PilihDokter.click()
    elif dokter == 13 :
        PilihDokter = web.find_element_by_xpath('//*[@id="i41"]/div[3]/div')
        PilihDokter.click()

    Next4 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span/span')
    Next4.click()

elif bekerja == 2 :
    RencanaKerja = web.find_element_by_xpath('//*[@id="i8"]/div[3]/div')
    RencanaKerja.click()

    Next2 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    Next2.click()

    if nonaerosol == 1:
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i5"]/div[3]/div')
        TindakanAerosol.click()
    elif nonaerosol == 2:
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i8"]/div[3]/div')
        TindakanAerosol.click()
    elif nonaerosol == 3 :
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i11"]/div[3]/div')
        TindakanAerosol.click()
    elif nonaerosol == 4 :
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i14"]/div[3]/div')
        TindakanAerosol.click()
    elif nonaerosol == 5 :
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i17"]/div[3]/div')
        TindakanAerosol.click()
    elif nonaerosol == 6 :
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i20"]/div[3]/div')
        TindakanAerosol.click()
    elif nonaerosol == 7 :
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i23"]/div[3]/div')
        TindakanAerosol.click()
    elif nonaerosol == 8 :
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i26"]/div[3]/div')
        TindakanAerosol.click()
    elif nonaerosol == 9 :
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i29"]/div[3]/div')
        TindakanAerosol.click()
    elif nonaerosol == 10 :
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i32"]/div[3]/div')
        TindakanAerosol.click()
    elif nonaerosol == 11 :
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i35"]/div[3]/div')
        TindakanAerosol.click()
    elif nonaerosol == 12 :
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i38"]/div[3]/div')
        TindakanAerosol.click()
    elif nonaerosol == 13 :
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i41"]/div[3]/div')
        TindakanAerosol.click()
    elif nonaerosol == 14 :
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i44"]/div[3]/div')
        TindakanAerosol.click()
    elif nonaerosol == 15 :
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i47"]/div[3]/div')
        TindakanAerosol.click()
    elif nonaerosol == 16 :
        TindakanAerosol = web.find_element_by_xpath('//*[@id="i50"]/div[3]/div')
        TindakanAerosol.click()

    Next3 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    Next3.click()

    time.sleep(1)

    if dokter == 1:
        PilihDokter = web.find_element_by_xpath('//*[@id="i5"]/div[3]/div')
        PilihDokter.click()
    elif dokter == 2:
        PilihDokter = web.find_element_by_xpath('//*[@id="i8"]/div[3]/div')
        PilihDokter.click()
    elif dokter == 3 :
        PilihDokter = web.find_element_by_xpath('//*[@id="i11"]/div[3]/div')
        PilihDokter.click()
    elif dokter == 4 :
        PilihDokter = web.find_element_by_xpath('//*[@id="i14"]/div[3]/div')
        PilihDokter.click()
    elif dokter == 5 :
        PilihDokter = web.find_element_by_xpath('//*[@id="i17"]/div[3]/div')
        PilihDokter.click()
    elif dokter == 6 :
        PilihDokter = web.find_element_by_xpath('//*[@id="i20"]/div[3]/div')
        PilihDokter.click()
    elif dokter == 7 :
        PilihDokter = web.find_element_by_xpath('//*[@id="i23"]/div[3]/div')
        PilihDokter.click()
    elif dokter == 8 :
        PilihDokter = web.find_element_by_xpath('//*[@id="i26"]/div[3]/div')
        PilihDokter.click()
    elif dokter == 9 :
        PilihDokter = web.find_element_by_xpath('//*[@id="i29"]/div[3]/div')
        PilihDokter.click()
    elif dokter == 10 :
        PilihDokter = web.find_element_by_xpath('//*[@id="i32"]/div[3]/div')
        PilihDokter.click()
    elif dokter == 11 :
        PilihDokter = web.find_element_by_xpath('//*[@id="i35"]/div[3]/div')
        PilihDokter.click()
    elif dokter == 12 :
        PilihDokter = web.find_element_by_xpath('//*[@id="i38"]/div[3]/div')
        PilihDokter.click()
    elif dokter == 13 :
        PilihDokter = web.find_element_by_xpath('//*[@id="i41"]/div[3]/div')
        PilihDokter.click()

    Next4 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span/span')
    Next4.click()
    
######### Non Aerosol #########
#RencanaKerja = web.find_element_by_xpath('//*[@id="i8"]/div[3]/div')
#RencanaKerja.click()

######### Aerosol #########
# RencanaKerja = web.find_element_by_xpath('//*[@id="i5"]/div[3]/div')
# RencanaKerja.click()

    

Pasien = web.find_element_by_xpath('//*[@id="i8"]/div[3]/div')
Pasien.click()

Next5 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span/span')
Next5.click()

namaP = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
namaP.send_keys(NamaPasien)

medis = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
medis.send_keys(NoRekamMedis)

time.sleep(1)
 
def reservasi():
    Submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    Submit.click()

    g = [1,2,3,4,5]

    for i in g:
        web.refresh()
        act = ActionChains(web)
        act.send_keys(Keys.F5).send_keys(Keys.ENTER).perform()
        print("reservasi ke", i)

schedule.every().day.at(jam).do(reservasi)

while True:
    schedule.run_pending()
    time.sleep(1)