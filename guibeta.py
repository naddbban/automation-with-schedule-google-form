from tkinter import Tk,Label,Frame,Entry,Button,ttk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import schedule

window = Tk()

def submit():
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
                            # [14]INDIKASI PULPEKTOMI       # [14]INDIKASI KURET                # [14] drg. Noor Hafida W., Sp.KG
                                                            # [15]KONTROL ORTHO                 # [15] drg. Cahyani
                                                            # [16]KONTROL SCALLING

    bekerja = bekerja_combo.get()
    aerosol = aerosol_combo.get()
    print(aerosol)
    print(len(aerosol))
    # nonaerosol = aerosol_combo.get()

    dokter = dokter_combo.get()
    jam = jam_entry.get()
    Shift = shift_entry.get()
    Nama = nama_entry.get()
    NoHp = nohp_entry.get()
    NamaPasien = pasien_entry.get()
    NoRekamMedis = medis_entry.get()

    if bekerja == "aerosol":
        kerja = 1
    elif bekerja == "nonaerosol":
        kerja = 2

    if aerosol == "KURETASE":
        ae = 1
    elif aerosol == "RESTORASI":
        ae = 2
    elif aerosol == "MJ (MAHKOTA JAKET)":
        ae = 3
    elif aerosol == "PSA":
        ae = 4
    elif aerosol == "PULPEKTOMI":
        ae = 5
    elif aerosol == "KONTROL PULPEKTOMI":
        ae = 6
    elif aerosol == "INLAY":
        ae = 7
    elif aerosol == "INSERSI INLAY":
        ae = 8
    elif aerosol == "KONTROL INLAY":
        ae = 9
    elif aerosol == "PCC":
        ae = 10
    elif aerosol == "INSERSI":
        ae = 11
    elif aerosol == "ONLAY":
        ae = 12
    elif aerosol == "BUR TULANG":
        ae = 13
    elif aerosol == "INDIKASI PULPEKTOMI":
        ae = 14

    if aerosol == "KONTROL MJ":
        nonae = 1
    elif aerosol == "KONTROL PSA":
        nonae = 2
    elif aerosol == "KONTROL RESTORASI":
        nonae = 3
    elif aerosol == "KONTROL KURETASE":
        nonae = 4
    elif aerosol == "KONTROL CABUT":
        nonae = 5
    elif aerosol == "EKSTRAKSI":
        nonae = 6
    elif aerosol == "KONTROL EKSTRAKSI":
        nonae = 7
    elif aerosol == "EKSO":
        nonae = 8
    elif aerosol == "KONTROL EKSO":
        nonae = 9
    elif aerosol == "PL (PEMERIKSAAN KENGKAP)":
        nonae = 10
    elif aerosol == "INDIKASI MJ":
        nonae = 11
    elif aerosol == "INNORKASI INLAY":
        nonae = 12
    elif aerosol == "INDIKASI PSA":
        nonae = 13
    elif aerosol == "INDIKASI KURET":
        nonae = 14
    elif aerosol == "KONTROL ORTHO":
        nonae = 15
    elif aerosol == "KONTROL SCALLING":
        nonae = 16 

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



    

    if dokter == "drg. Laila N":
        ddd = 1
    elif dokter == "drg. Ariyani Faizah":
        ddd = 2
    elif dokter == "drg. Juwita RN":
        ddd = 3
    elif dokter == "drg. Lasmi Dewi":
        ddd = 4
    elif dokter == "drg. Edi Karyadi":
        ddd = 5
    elif dokter == "drg. Arny":
        ddd = 6
    elif dokter == "drg. Nina Runting":
        ddd = 7
    elif dokter == "drg. Pamungkas Handy":
        ddd = 8
    elif dokter == "drg. Nur Rachmawati":
        ddd = 9
    elif dokter == "drg. Iyop Ropika":
        ddd = 10
    elif dokter == "drg. Ikmal Hafizi":
        ddd = 11
    elif dokter == "drg. Nendika":
        ddd = 12
    elif dokter == "drg. Septriyani":
        ddd = 13
    elif dokter == "drg. Noor Hafida":
        ddd = 14
    elif dokter == "drg. Cahyani":
        ddd = 15

    dd = ddd * 3
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

    Keperluan = web.find_element_by_xpath('//*[@id="i25"]/div[3]/div')
    Keperluan.click()

    Next1 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    Next1.click()

    time.sleep(1)

    if kerja == 1:

        yy = ae * 3
        y = 5 + yy
        y_str = str(y)
        xyz = x + y_str + z
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

    elif kerja == 2 :

        ss = nonae * 3
        s = 2 + ss
        s_str = str(s)
        xsz = x + s_str + z
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

window.title("Reservasi")
window.resizable("false", "false")
window.geometry("400x330")
mainframe = Frame(window, bg="red")
mainframe.pack(fill="both", expand=True)

hframe = Frame(window)
label1 = Label(hframe, text = "Jam", padx = 10, pady = 2)
label1.grid(row = 1, column = 0, padx = 10, pady = 5)
label2 = Label(hframe, text = "Shift", padx = 10, pady = 2)
label2.grid(row = 2, column = 0, padx = 10, pady = 5)
label3 = Label(hframe, text = "Nama", padx = 10, pady = 2)
label3.grid(row = 3, column = 0, padx = 10, pady = 5)
label4 = Label(hframe, text = "No HP", padx = 10, pady = 2)
label4.grid(row = 4, column = 0, padx = 10, pady = 5)
label5 = Label(hframe, text = "Nama pasien", padx = 10, pady = 2)
label5.grid(row = 5, column = 0, padx = 10, pady = 5)
label6 = Label(hframe, text = "No Rekam Medis", padx = 10, pady = 2)
label6.grid(row = 6, column = 0, padx = 10, pady = 5)

jam_entry = Entry(hframe, width = "30")
jam_entry.grid(row = 1, column = 1, padx = 10, pady = 5)
jam_entry.insert(0, "07:29:58")
shift_entry = Entry(hframe, width = "30")
shift_entry.grid(row = 2, column = 1, padx = 10, pady = 5)
shift_entry.insert(0, "pagi")
nama_entry = Entry(hframe, width = "30")
nama_entry.grid(row = 3, column = 1, padx = 10, pady = 5)
nama_entry.insert(0, "Arida")
nohp_entry = Entry(hframe, width = "30")
nohp_entry.grid(row = 4, column = 1, padx = 10, pady = 5)
nohp_entry.insert(0, "08978095095")
pasien_entry = Entry(hframe, width = "30")
pasien_entry.grid(row = 5, column = 1, padx = 10, pady = 5)
pasien_entry.insert(0, "asd")
medis_entry = Entry(hframe, width = "30")
medis_entry.grid(row = 6, column = 1, padx = 10, pady = 5)
medis_entry.insert(0, "0000")

list_bekerja = [
    "aerosol",
    "nonaerosol"
]

list_aerosol = [
    "KURETASE",
    "RESTORASI",
    "MJ (MAHKOTA JAKET)",
    "PSA",
    "PULPEKTOMI",
    "KONTROL PULPEKTOMI",
    "INLAY",
    "INSERSI INLAY",
    "KONTROL INLAY",
    "PCC",
    "INSERSI",
    "ONLAY",
    "BUR TULANG",
    "INDIKASI PULPEKTOMI"
]

list_nonaerosol = [
    "KONTROL MJ",
    "KONTROL PSA",
    "KONTROL RESTORASI",
    "KONTROL KURETASE",
    "KONTROL CABUT",
    "EKSTRAKSI",
    "KONTROL EKSTRAKSI",
    "EKSO",
    "KONTROL EKSO",
    "PL (PEMERIKSAAN KENGKAP)",
    "INDIKASI MJ",
    "INNORKASI INLAY",
    "INDIKASI PSA",
    "INDIKASI KURET",
    "KONTROL ORTHO",
    "KONTROL SCALLING"
]

list_dokter = [
    "drg. Laila N",
    "drg. Ariyani Faizah",
    "drg. Juwita RN",
    "drg. Lasmi Dewi",
    "drg. Edi Karyadi",
    "drg. Arny",
    "drg. Nina Runting",
    "drg. Pamungkas Handy",
    "drg. Nur Rachmawati",
    "drg. Iyop Ropika",
    "drg. Ikmal Hafizi",
    "drg. Nendika",
    "drg. Septriyani",
    "drg. Noor Hafida",
    "drg. Cahyani"
]

def pick_kerja(e):
    if bekerja_combo.get() == "aerosol":
        aerosol_combo.config(value = list_aerosol)
        aerosol_combo.current(0)
    if bekerja_combo.get() == "nonaerosol":
        aerosol_combo.config(value = list_nonaerosol)
        aerosol_combo.current(0)

bekerja_combo = ttk.Combobox(hframe, width = "27", value = list_bekerja)
bekerja_combo.grid(row = 7, column = 1, padx = 10, pady = 5)
bekerja_combo.current(0)
bekerja_combo.bind("<<ComboboxSelected>>", pick_kerja)
# my_combo.pack()

aerosol_combo = ttk.Combobox(hframe, width = "27", value = [""] )
aerosol_combo.grid(row = 8, column = 1, padx = 10, pady = 5)
aerosol_combo.current(0)
aerosol_combo.bind("<<ComboboxSelected>>")

dokter_combo = ttk.Combobox(hframe, width = "27", value = list_dokter )
dokter_combo.grid(row = 9, column = 1, padx = 10, pady = 5)
dokter_combo.current(0)
dokter_combo.bind("<<ComboboxSelected>>")

hframe1 = Frame(window, width = "20",padx = 5, pady = 5)
button1 = Button(hframe1, text = "Submit", padx = 5, pady = 5, command = submit)
button1.pack()

hframe.pack(fill="x")
hframe1.pack(fill="x")


window.mainloop()