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
web = webdriver.Chrome(executable_path = driver_path)
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
aerosol = 7
nonaerosol = 7
dokter = 6

jam = "11:40:30"
Shift = "pagi"
Nama = "abajsas"
NoHp = "01234567"
DosenP = "Drg. Juwita"
NamaPasien = "Sabsg"
NoRekamMedis = "0000"

x = '//*[@id="i'
z = '"]/div[3]/div'

sk = len(Shift)
if sk == 4:
    skp = sk + 3
    skp_str = str(skp)
    xkz = x + skp_str + z
else:
    skp = sk + 5
    skp_str = str(skp)
    xkz = x + skp_str + z

yy = aerosol * 3
y = 5 + yy
y_str = str(y)
xyz = x + y_str + z

ss = nonaerosol * 3
s = 2 + ss
s_str = str(s)
xsz = x + s_str + z

dd = dokter * 3
d = 2 + dd
d_str = str(d)
xdz = x + d_str + z

def next():
    Next = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span/span')
    Next.click()

def reservasi():
    Submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    Submit.click()
    print("reservasi ke 1")

    g = 5

    for i in range(g):
        web.refresh()
        act = ActionChains(web)
        act.send_keys(Keys.F5).send_keys(Keys.ENTER).perform()
        print("reservasi ke", i + 2)

ShiftKerja = web.find_element_by_xpath(xkz)
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

time.sleep(1)

if bekerja == 1:
    RencanaKerja = web.find_element_by_xpath('//*[@id="i5"]/div[3]/div')
    RencanaKerja.click()
    next()

    TindakanAerosol = web.find_element_by_xpath(xyz)
    TindakanAerosol.click()
    next()

    time.sleep(1)

    PilihDokter = web.find_element_by_xpath(xdz)
    PilihDokter.click()
    next()

elif bekerja == 2 :
    RencanaKerja = web.find_element_by_xpath('//*[@id="i8"]/div[3]/div')
    RencanaKerja.click()
    next()

    TindakanAerosol = web.find_element_by_xpath(xsz)
    TindakanAerosol.click()
    next()

    time.sleep(1)

    PilihDokter = web.find_element_by_xpath(xdz)
    PilihDokter.click()
    next()

Pasien = web.find_element_by_xpath('//*[@id="i8"]/div[3]/div')
Pasien.click()
next()

time.sleep(1)

namaP = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
namaP.send_keys(NamaPasien)

medis = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
medis.send_keys(NoRekamMedis)

time.sleep(1)

schedule.every().day.at(jam).do(reservasi)

while True:
    schedule.run_pending()
    time.sleep(1)