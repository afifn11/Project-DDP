from tkinter import *
from tkinter import messagebox
import random
import time

# Membuat Frame Aplikasi
root = Tk()
root.geometry('1275x720+0+0')  # menentukan window aplikasi
root.resizable(0, 0)
root.title('Xie Xie Cafe')  # Nama Aplikasi

topFrame = Frame(root, bd=10, relief=RIDGE, bg='white')
topFrame.pack(side=TOP)

labelTitle = Label(topFrame, text='Xie Xie Cafe', font=('Castellar', 39, 'bold'), fg='#009999', bg='#302a18', bd=15,
                   width=30)  # judul
labelTitle.grid(row=0, column=10)

root.config(bg='#336666')  # warna dasar/ background

# Variabel
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()

# Variabel menu makanan
e_seafood_paelaa_var = StringVar()
e_chili_crab_var = StringVar()
e_chicken_muamba_var = StringVar()
e_steak_and_kidney_pie_var = StringVar()
e_mie_ayam_var= StringVar()
e_bakso_lava_var = StringVar()
e_ayam_betutu_var = StringVar()
e_beef_rendang_var = StringVar()
e_sate_ayam_var = StringVar()

# Variabel Menu Minuman
e_teh_tarik_var = StringVar()
e_thai_tea_var = StringVar()
e_teh_yuzu_var = StringVar()
e_es_teh_cincau_var = StringVar()
e_iced_matcha_boba_latte_var = StringVar()
e_jus_mangga_var = StringVar()
e_jus_alpukat_var = StringVar()
e_jus_jeruk_var = StringVar()
e_espresso_escapade_var = StringVar()

# variabel harga dalam struk
hargadarimakananvar = StringVar()
hargadariminumanvar = StringVar()
subtotalvar = StringVar()
servicetaxvar = StringVar()
totalcostvar = StringVar()
taxvaluevar = StringVar()

e_seafood_paelaa_var.set('0')
e_chili_crab_var.set('0')
e_chicken_muamba_var.set('0')
e_steak_and_kidney_pie_var.set('0')
e_mie_ayam_var.set('0')
e_bakso_lava_var.set('0')
e_ayam_betutu_var.set('0')
e_beef_rendang_var.set('0')
e_sate_ayam_var.set('0')

e_teh_tarik_var.set('0')
e_thai_tea_var.set('0')
e_teh_yuzu_var.set('0')
e_es_teh_cincau_var.set('0')
e_iced_matcha_boba_latte_var.set('0')
e_jus_mangga_var.set('0')
e_jus_alpukat_var.set('0')
e_jus_jeruk_var.set('0')
e_espresso_escapade_var.set('0')

# Fungsi
# Awal fungsi perhitungan harga total
tax = 3 / 100 
def totalcost():
    # Mengglobalkan beberapa variabel terlebih dahulu
    global hargadarimakanan, hargadariminuman, subtotalItems, totaltax
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
            var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or \
            var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
            var16.get() != 0 or var17.get() != 0 or var18.get() != 0:

        item1 = int(e_seafood_paelaa_var.get())
        item2 = int(e_chili_crab_var.get())
        item3 = int(e_chicken_muamba_var.get())
        item4 = int(e_steak_and_kidney_pie_var.get())
        item5 = int(e_mie_ayam_var.get())
        item6 = int(e_bakso_lava_var.get())
        item7 = int(e_ayam_betutu_var.get())
        item8 = int(e_beef_rendang_var.get())
        item9 = int(e_sate_ayam_var.get())

        item10 = int(e_teh_tarik_var.get())
        item11 = int(e_thai_tea_var.get())
        item12 = int(e_teh_yuzu_var.get())
        item13 = int(e_es_teh_cincau_var.get())
        item14 = int(e_iced_matcha_boba_latte_var.get())
        item15 = int(e_jus_mangga_var.get())
        item16 = int(e_jus_alpukat_var.get())
        item17 = int(e_jus_jeruk_var.get())
        item18 = int(e_espresso_escapade_var.get())
        
        hargadarimakanan = (item1*30000)+(item2*35000)+(item3*25000)+(item4*30000)+(item5*18000)+(item6*25000)+(item7*25000)+(item8*30000)+(item9*22000)
        hargadariminuman = (item10*15000)+(item11*12000)+(item12*12000)+(item13*15000)+(item14*17000)+(item15*15000)+(item16*15000)+(item17*12000)+(item18*25000)

        hargadarimakananvar.set(str(hargadarimakanan))
        hargadariminumanvar.set(str(hargadariminuman))

        subtotalItems = hargadarimakanan + hargadariminuman
        subtotalvar.set(str(subtotalItems))

        #tax=(11/100)

        taxvaluevar.set(str(tax))
        totaltax = subtotalItems * tax

        servicetaxvar.set(totaltax)

        totalcost = subtotalItems+totaltax
        totalcostvar.set(str(totalcost))

    else:
        messagebox.showerror('Error','Tidak ada item yang dipilih')
# batas perhitungan fungsi harga total

# fungsi cetak struk
def struk():
    global billnumber, date
    if hargadarimakananvar.get() != '' or hargadariminumanvar.get() != '':
        textStruk.delete(1.0,END)
        x = random.randint(100,10000)
        billnumber = 'BILL' + str(x)
        date = time.strftime('%d/%m/%Y')
        textStruk.insert(END,'Resep:\t        '+billnumber+'\t           '+date+'\n')
        textStruk.insert(END, '==============================\n')
        textStruk.insert(END,'Items:\t\t       Harga Total (Rp)\n')
        textStruk.insert(END, '==============================\n')
        if e_seafood_paelaa_var.get()!='0':
            textStruk.insert(END,f'seafood paelaa\t\t\tRp {int(e_seafood_paelaa_var.get())*30000}\n\n')
        
        if e_chili_crab_var.get()!='0':
            textStruk.insert(END,f'chili crab\t\t\tRp {int(e_chili_crab_var.get())*35000}\n\n')

        if e_chicken_muamba_var.get()!='0':
            textStruk.insert(END,f'chicken muamba\t\t\tRp {int(e_chicken_muamba_var.get())*25000}\n\n')

        if e_steak_and_kidney_pie_var.get()!='0':
            textStruk.insert(END,f'steak and kidney pie\t\t\tRp {int(e_steak_and_kidney_pie_var.get())*30000}\n\n')

        if e_mie_ayam_var.get()!='0':
            textStruk.insert(END,f'mie ayam\t\t\tRp {int(e_mie_ayam_var.get())*18000}\n\n')

        if e_bakso_lava_var.get()!='0':
            textStruk.insert(END,f'bakso lava\t\t\tRp {int(e_bakso_lava_var.get())*25000}\n\n')

        if e_ayam_betutu_var.get()!='0':
            textStruk.insert(END,f'ayam betutu\t\t\tRp {int(e_ayam_betutu_var.get())*25000}\n\n')

        if e_beef_rendang_var.get()!='0':
            textStruk.insert(END,f'beef rendang\t\t\tRp {int(e_beef_rendang_var.get())*30000}\n\n')

        if e_sate_ayam_var.get()!='0':
            textStruk.insert(END,f'sate ayam\t\t\tRp {int(e_sate_ayam_var.get())*22000}\n\n')

        if e_teh_tarik_var.get()!='0':
            textStruk.insert(END,f'teh tarik\t\t\tRp {int(e_teh_tarik_var.get())*15000}\n\n')
        
        if e_thai_tea_var.get()!='0':
            textStruk.insert(END,f'thai tea\t\t\tRp {int(e_thai_tea_var.get())*12000}\n\n')

        if e_teh_yuzu_var.get()!='0':
            textStruk.insert(END,f'teh yuzu\t\t\tRp {int(e_teh_yuzu_var.get())*12000}\n\n')

        if e_es_teh_cincau_var.get()!='0':
            textStruk.insert(END,f'es teh cincau\t\t\tRp {int(e_es_teh_cincau_var.get())*15000}\n\n')

        if e_iced_matcha_boba_latte_var.get()!='0':
            textStruk.insert(END,f'iced matcha boba latte\t\t\tRp {int(e_iced_matcha_boba_latte_var.get())*17000}\n\n')

        if e_jus_mangga_var.get()!='0':
            textStruk.insert(END,f'jus mangga\t\t\tRp {int(e_jus_mangga_var.get())*15000}\n\n')

        if e_jus_alpukat_var.get()!='0':
            textStruk.insert(END,f'jus alpukat\t\t\tRp {int(e_jus_alpukat_var.get())*15000}\n\n')

        if e_jus_jeruk_var.get()!='0':
            textStruk.insert(END,f'jus jeruk\t\t\tRp {int(e_jus_jeruk_var.get())*12000}\n\n')

        if e_espresso_escapade_var.get()!='0':
            textStruk.insert(END,f'espresso escapade\t\t\tRp {int(e_espresso_escapade_var.get())*25000}\n\n')

        textStruk.insert(END, '==============================\n')

        if hargadarimakananvar.get() !='RP 0':
            textStruk.insert(END, f'Harga dari Makanan\t\t\t Rp {hargadarimakanan}\n\n')

        if hargadariminumanvar.get() !='RP 0':
            textStruk.insert(END, f'Harga dari Minuman\t\t\t Rp {hargadariminuman}\n\n')

            textStruk.insert(END, f'Subtotal\t\t\t Rp {subtotalItems}\n\n')
            textStruk.insert(END, f'Service Tax\t\t Rp {totaltax}\n\n')
            textStruk.insert(END, f'Harga Total\t\t Rp {subtotalItems+totaltax}\n\n')
            textStruk.insert(END, '==============================\n')

    else:
        messagebox.showerror('Error','Tidak ada item yang dipilih')
        # batas fungsi cetak struk
            
# fungsi reset pesanan

def reset():
    textStruk.delete(1.0, END)
    e_seafood_paelaa_var.set('0')
    e_chili_crab_var.set('0')
    e_chicken_muamba_var.set('0')
    e_steak_and_kidney_pie_var.set('0')
    e_mie_ayam_var.set('0')
    e_bakso_lava_var.set('0')
    e_ayam_betutu_var.set('0')
    e_beef_rendang_var.set('0')
    e_sate_ayam_var.set('0')

    e_teh_tarik_var.set('0')
    e_thai_tea_var.set('0')
    e_teh_yuzu_var.set('0')
    e_es_teh_cincau_var.set('0')
    e_iced_matcha_boba_latte_var.set('0')
    e_jus_mangga_var.set('0')
    e_jus_alpukat_var.set('0')
    e_jus_jeruk_var.set('0')
    e_espresso_escapade_var.set('0')
    # batas untuk variabel

    textseafoodpaelaa.config(state=DISABLED)
    textchilicrab.config(state=DISABLED)
    textchickenmuamba.config(state=DISABLED)
    textsteakandkidneypie.config(state=DISABLED)
    textmieayam.config(state=DISABLED)
    textbaksolava.config(state=DISABLED)
    textayambetutu.config(state=DISABLED)
    textbeefrendang.config(state=DISABLED)
    textsateayam.config(state=DISABLED)
    texttehtarik.config(state=DISABLED)
    textthaitea.config(state=DISABLED)
    texttehyuzu.config(state=DISABLED)
    textestehcincau.config(state=DISABLED)
    texticedmatchabobalatte.config(state=DISABLED)
    textjusmangga.config(state=DISABLED)
    textjusalpukat.config(state=DISABLED)
    textjusjeruk.config(state=DISABLED)
    textespressoescapade.config(state=DISABLED)


    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)

    hargadarimakananvar.set('')
    hargadariminumanvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')
    taxvaluevar.set('')


# mengaktifkan fungsi entry makanan

def seafood_paelaa():
    if var1.get() == 1:
        textseafoodpaelaa.config(state=NORMAL)
        textseafoodpaelaa.delete(0,END)
        textseafoodpaelaa.focus()
    else:
        textseafoodpaelaa.config(state=DISABLED)
        e_seafood_paelaa_var.set('0')

def chili_crab():
    if var2.get() == 1:
        textchilicrab.config(state=NORMAL)
        textchilicrab.delete(0,END)
        textchilicrab.focus()
    else:
        textchilicrab.config(state=DISABLED)
        e_chili_crab_var.set('0')

def chicken_muamba():
    if var3.get() == 1:
        textchickenmuamba.config(state=NORMAL)
        textchickenmuamba.delete(0,END)
        textchickenmuamba.focus()
    else:
        textchickenmuamba.config(state=DISABLED)
        e_chicken_muamba_var.set('0')

def steak_and_kidney_pie():
    if var4.get() == 1:
        textsteakandkidneypie.config(state=NORMAL)
        textsteakandkidneypie.delete(0,END)
        textsteakandkidneypie.focus()
    else:
        textsteakandkidneypie.config(state=DISABLED)
        e_steak_and_kidney_pie_var.set('0')

def mie_ayam():
    if var5.get() == 1:
        textmieayam.config(state=NORMAL)
        textmieayam.delete(0,END)
        textmieayam.focus()
    else:
        textmieayam.config(state=DISABLED)
        e_mie_ayam_var.set('0')

def bakso_lava():
    if var6.get() == 1:
        textbaksolava.config(state=NORMAL)
        textbaksolava.delete(0,END)
        textbaksolava.focus()
    else:
        textbaksolava.config(state=DISABLED)
        e_bakso_lava_var.set('0')

def ayam_betutu():
    if var7.get() == 1:
        textayambetutu.config(state=NORMAL)
        textayambetutu.delete(0,END)
        textayambetutu.focus()
    else:
        textayambetutu.config(state=DISABLED)
        e_ayam_betutu_var.set('0')

def beef_rendang():
    if var8.get() == 1:
        textbeefrendang.config(state=NORMAL)
        textbeefrendang.delete(0,END)
        textbeefrendang.focus()
    else:
        textbeefrendang.config(state=DISABLED)
        e_beef_rendang_var.set('0')

def sate_ayam():
    if var9.get() == 1:
        textsateayam.config(state=NORMAL)
        textsateayam.delete(0,END)
        textsateayam.focus()
    else:
        textsateayam.config(state=DISABLED)
        e_sate_ayam_var.set('0')


def teh_tarik():
    if var10.get() == 1:
        texttehtarik.config(state=NORMAL)
        texttehtarik.delete(0,END)
        texttehtarik.focus()
    else:
        texttehtarik.config(state=DISABLED)
        e_teh_tarik_var.set('0')

def thai_tea():
    if var11.get() == 1:
        textthaitea.config(state=NORMAL)
        textthaitea.delete(0,END)
        textthaitea.focus()
    else:
        textthaitea.config(state=DISABLED)
        e_thai_tea_var.set('0')

def teh_yuzu():
    if var12.get() == 1:
        texttehyuzu.config(state=NORMAL)
        texttehyuzu.delete(0,END)
        texttehyuzu.focus()
    else:
        texttehyuzu.config(state=DISABLED)
        e_teh_yuzu_var.set('0')

def es_teh_cincau():
    if var13.get() == 1:
        textestehcincau.config(state=NORMAL)
        textestehcincau.delete(0,END)
        textestehcincau.focus()
    else:
        textestehcincau.config(state=DISABLED)
        e_es_teh_cincau_var.set('0')

def iced_matcha_boba_latte():
    if var14.get() == 1:
        texticedmatchabobalatte.config(state=NORMAL)
        texticedmatchabobalatte.delete(0,END)
        texticedmatchabobalatte.focus()
    else:
        texticedmatchabobalatte.config(state=DISABLED)
        e_iced_matcha_boba_latte_var.set('0')

def jus_mangga():
    if var15.get() == 1:
        textjusmangga.config(state=NORMAL)
        textjusmangga.delete(0,END)
        textjusmangga.focus()
    else:
        textjusmangga.config(state=DISABLED)
        e_jus_mangga_var.set('0')

def jus_alpukat():
    if var16.get() == 1:
        textjusalpukat.config(state=NORMAL)
        textjusalpukat.delete(0,END)
        textjusalpukat.focus()
    else:
        textjusalpukat.config(state=DISABLED)
        e_jus_alpukat_var.set('0')

def jus_jeruk():
    if var17.get() == 1:
        textjusjeruk.config(state=NORMAL)
        textjusjeruk.delete(0,END)
        textjusjeruk.focus()
    else:
        textjusjeruk.config(state=DISABLED)
        e_jus_jeruk_var.set('0')

def espresso_escapade():
    if var18.get() == 1:
        textespressoescapade.config(state=NORMAL)
        textespressoescapade.delete(0,END)
        textespressoescapade.focus()
    else:
        textespressoescapade.config(state=DISABLED)
        e_espresso_escapade_var.set('0')

# membuat frame kiri untuk menu cafe

menuFrame = Frame(root, bd=10, relief=RIDGE, bg='#003333')
menuFrame.pack(side=LEFT)

hargaFrame = Frame(menuFrame, bd=9, relief=RIDGE, bg='#050206', pady=12)
hargaFrame.pack(side=BOTTOM)

makananFrame = LabelFrame(menuFrame, text='Makanan', font=('Castellar',19, 'bold'), bd=10, relief=RIDGE, fg='#2f2f2f', bg='#f6f6f6')
makananFrame.pack(side=LEFT)

minumanFrame = LabelFrame(menuFrame, text='Minuman', font=('Castellar',19, 'bold'), bd=10, relief=RIDGE, fg='#2f2f2f', bg='#f6f6f6')
minumanFrame.pack(side=LEFT)

# membuat tampilan daftar menu makanan

seafood_paelaa_button = Checkbutton(makananFrame, text='Seafood Paelaa', font=('Calibri', 16, 'bold'), onvalue=1, offvalue=0, variable=var1, 
                   command= seafood_paelaa, bg='#f6f6f6')
seafood_paelaa_button.grid(row=0, column=0, sticky=W)

chili_crab_button = Checkbutton(makananFrame, text='Chili Crab', font=('Calibri', 16, 'bold'), onvalue=1, offvalue=0, variable=var2, 
                   command= chili_crab, bg='#f6f6f6')
chili_crab_button.grid(row=1, column=0, sticky=W)

chicken_muamba_button = Checkbutton(makananFrame, text='Chicken Muamba', font=('Calibri', 16, 'bold'), onvalue=1, offvalue=0, variable=var3, 
                   command= chicken_muamba, bg='#f6f6f6')
chicken_muamba_button.grid(row=2, column=0, sticky=W)

steak_and_kidney_pie_button = Checkbutton(makananFrame, text='Steak and kidney pie', font=('Calibri', 16, 'bold'), onvalue=1, offvalue=0, variable=var4, 
                   command= steak_and_kidney_pie, bg='#f6f6f6')
steak_and_kidney_pie_button.grid(row=3, column=0, sticky=W)

mie_ayam_button = Checkbutton(makananFrame, text='Mie Ayam', font=('Calibri', 16, 'bold'), onvalue=1, offvalue=0, variable=var5, 
                   command= mie_ayam, bg='#f6f6f6')
mie_ayam_button.grid(row=4, column=0, sticky=W)

bakso_lava_button = Checkbutton(makananFrame, text='Bakso Lava', font=('Calibri', 16, 'bold'), onvalue=1, offvalue=0, variable=var6, 
                   command= bakso_lava, bg='#f6f6f6')
bakso_lava_button.grid(row=5, column=0, sticky=W)

ayam_betutu_button = Checkbutton(makananFrame, text='Ayam Betutu', font=('Calibri', 16, 'bold'), onvalue=1, offvalue=0, variable=var7, 
                   command= ayam_betutu, bg='#f6f6f6')
ayam_betutu_button.grid(row=6, column=0, sticky=W)

beef_rendang_button = Checkbutton(makananFrame, text='Beef Rendang', font=('Calibri', 16, 'bold'), onvalue=1, offvalue=0, variable=var8, 
                   command= beef_rendang, bg='#f6f6f6')
beef_rendang_button.grid(row=7, column=0, sticky=W)

sate_ayam_button = Checkbutton(makananFrame, text='Sate Ayam', font=('Calibri', 16, 'bold'), onvalue=1, offvalue=0, variable=var9, 
                   command= sate_ayam, bg='#f6f6f6')
sate_ayam_button.grid(row=8, column=0, sticky=W)


# menambahkan fields entry untuk item makanan
textseafoodpaelaa = Entry(makananFrame, font=('Calibri', 16, 'bold'), bd=7, width=8, state=DISABLED, textvariable=e_seafood_paelaa_var)
textseafoodpaelaa.grid(row=0, column=1)

textchilicrab = Entry(makananFrame, font=('Calibri', 16, 'bold'), bd=7, width=8, state=DISABLED, textvariable=e_chili_crab_var)
textchilicrab.grid(row=1, column=1)

textchickenmuamba = Entry(makananFrame, font=('Calibri', 16, 'bold'), bd=7, width=8, state=DISABLED, textvariable=e_chicken_muamba_var)
textchickenmuamba.grid(row=2, column=1)

textsteakandkidneypie = Entry(makananFrame, font=('Calibri', 16, 'bold'), bd=7, width=8, state=DISABLED, textvariable=e_steak_and_kidney_pie_var)
textsteakandkidneypie.grid(row=3, column=1)

textmieayam = Entry(makananFrame, font=('Calibri', 16, 'bold'), bd=7, width=8, state=DISABLED, textvariable=e_mie_ayam_var)
textmieayam.grid(row=4, column=1)

textbaksolava = Entry(makananFrame, font=('Calibri', 16, 'bold'), bd=7, width=8, state=DISABLED, textvariable=e_bakso_lava_var)
textbaksolava.grid(row=5, column=1)

textayambetutu = Entry(makananFrame, font=('Calibri', 16, 'bold'), bd=7, width=8, state=DISABLED, textvariable=e_ayam_betutu_var)
textayambetutu.grid(row=6, column=1)

textbeefrendang = Entry(makananFrame, font=('Calibri', 16, 'bold'), bd=7, width=8, state=DISABLED, textvariable=e_beef_rendang_var)
textbeefrendang.grid(row=7, column=1)

textsateayam = Entry(makananFrame, font=('Calibri', 16, 'bold'), bd=7, width=8, state=DISABLED, textvariable=e_sate_ayam_var)
textsateayam.grid(row=8, column=1)


# membuat daftar tampilan menu minuman
teh_tarik_button = Checkbutton(minumanFrame, text='Teh Tarik', font=('Calibri', 16, 'bold'), onvalue=1, offvalue=0, variable=var10, 
                   command= teh_tarik, bg='#f6f6f6')
teh_tarik_button.grid(row=0, column=0, sticky=W)

thai_tea_button = Checkbutton(minumanFrame, text='Thai Tea', font=('Calibri', 16, 'bold'), onvalue=1, offvalue=0, variable=var11, 
                   command= thai_tea, bg='#f6f6f6')
thai_tea_button.grid(row=1, column=0, sticky=W)

teh_yuzu_button = Checkbutton(minumanFrame, text='Teh Yuzu', font=('Calibri', 16, 'bold'), onvalue=1, offvalue=0, variable=var12, 
                   command= teh_yuzu, bg='#f6f6f6')
teh_yuzu_button.grid(row=2, column=0, sticky=W)

es_teh_cincau_button = Checkbutton(minumanFrame, text='Es Teh Cincau', font=('Calibri', 16, 'bold'), onvalue=1, offvalue=0, variable=var13, 
                   command= es_teh_cincau, bg='#f6f6f6')
es_teh_cincau_button.grid(row=3, column=0, sticky=W)

iced_matcha_boba_latte_button = Checkbutton(minumanFrame, text='Iced Matcha Boba Latte', font=('Calibri', 16, 'bold'), onvalue=1, offvalue=0, variable=var14, 
                   command= iced_matcha_boba_latte, bg='#f6f6f6')
iced_matcha_boba_latte_button.grid(row=4, column=0, sticky=W)

jus_mangga_button = Checkbutton(minumanFrame, text='Jus Mangga', font=('Calibri', 16, 'bold'), onvalue=1, offvalue=0, variable=var15, 
                   command= jus_mangga, bg='#f6f6f6')
jus_mangga_button.grid(row=5, column=0, sticky=W)

jus_alpukat_button = Checkbutton(minumanFrame, text='Jus Alpukat', font=('Calibri', 16, 'bold'), onvalue=1, offvalue=0, variable=var16, 
                   command= jus_alpukat, bg='#f6f6f6')
jus_alpukat_button.grid(row=6, column=0, sticky=W)

jus_jeruk_button = Checkbutton(minumanFrame, text='Jus Jeruk', font=('Calibri', 16, 'bold'), onvalue=1, offvalue=0, variable=var17, 
                   command= jus_jeruk, bg='#f6f6f6')
jus_jeruk_button.grid(row=7, column=0, sticky=W)

espresso_escapade_button = Checkbutton(minumanFrame, text='Espresso Escapade', font=('Calibri', 16, 'bold'), onvalue=1, offvalue=0, variable=var18, 
                   command= espresso_escapade, bg='#f6f6f6')
espresso_escapade_button.grid(row=8, column=0, sticky=W)


# menambahkan fields entry untuk item minuman
texttehtarik = Entry(minumanFrame, font=('Calibri', 16, 'bold'), bd=7, width=8, state=DISABLED, textvariable=e_teh_tarik_var)
texttehtarik.grid(row=0, column=1)

textthaitea = Entry(minumanFrame, font=('Calibri', 16, 'bold'), bd=7, width=8, state=DISABLED, textvariable=e_thai_tea_var)
textthaitea.grid(row=1, column=1)

texttehyuzu = Entry(minumanFrame, font=('Calibri', 16, 'bold'), bd=7, width=8, state=DISABLED, textvariable=e_teh_yuzu_var)
texttehyuzu.grid(row=2, column=1)

textestehcincau = Entry(minumanFrame, font=('Calibri', 16, 'bold'), bd=7, width=8, state=DISABLED, textvariable=e_es_teh_cincau_var)
textestehcincau.grid(row=3, column=1)

texticedmatchabobalatte = Entry(minumanFrame, font=('Calibri', 16, 'bold'), bd=7, width=8, state=DISABLED, textvariable=e_iced_matcha_boba_latte_var)
texticedmatchabobalatte.grid(row=4, column=1)

textjusmangga = Entry(minumanFrame, font=('Calibri', 16, 'bold'), bd=7, width=8, state=DISABLED, textvariable=e_jus_mangga_var)
textjusmangga.grid(row=5, column=1)

textjusalpukat = Entry(minumanFrame, font=('Calibri', 16, 'bold'), bd=7, width=8, state=DISABLED, textvariable=e_jus_alpukat_var)
textjusalpukat.grid(row=6, column=1)

textjusjeruk = Entry(minumanFrame, font=('Calibri', 16, 'bold'), bd=7, width=8, state=DISABLED, textvariable=e_jus_jeruk_var)
textjusjeruk.grid(row=7, column=1)

textespressoescapade = Entry(minumanFrame, font=('Calibri', 16, 'bold'), bd=7, width=8, state=DISABLED, textvariable=e_espresso_escapade_var)
textespressoescapade.grid(row=8, column=1)

# membuat frame kanan untuk struk
framekanan = Frame(root, bd=15, relief=RIDGE)
framekanan.pack(side=RIGHT)

strukFrame = Frame(framekanan, bd=1, relief=RIDGE, bg='#f0f0f0')
strukFrame.pack()

buttonFrame = Frame(framekanan, bd=3, relief=RIDGE)
buttonFrame.pack()

# membuat label harga dan kolom entry
LabelHargadariMakanan = Label(hargaFrame, text='Harga Makanan', font=('Constantia', 12, 'bold'), bg='#050206', fg='#fde4c3')
LabelHargadariMakanan.grid(row=0, column=0)

textHargadariMakanan = Entry(hargaFrame, font=('Calibri', 14, 'bold'), bd=6, width=16, state='readonly', textvariable=hargadarimakananvar)
textHargadariMakanan.grid(row=0, column=1, padx=41)

LabelHargadariMinuman = Label(hargaFrame, text='Harga Minuman', font=('Constantia', 12, 'bold'), bg='#050206', fg='#fde4c3')
LabelHargadariMinuman.grid(row=1, column=0)

textHargadariMinuman = Entry(hargaFrame, font=('Calibri', 14, 'bold'), bd=6, width=16, state='readonly', textvariable=hargadariminumanvar)
textHargadariMinuman.grid(row=1, column=1, padx=41)

LabelSubtotal =Label(hargaFrame, text='Subtotal', font=('Constantia', 12, 'bold'), bg='#050206', fg='#fde4c3')
LabelSubtotal.grid(row=0, column=2)

textSubtotal = Entry(hargaFrame, font=('Calibri', 14, 'bold'), bd=6, width=16, state='readonly', textvariable=subtotalvar)
textSubtotal.grid(row=0, column=3, padx=41)

LabelTax =Label(hargaFrame, text='Pajak'+' '+str(tax*100)+'%', font=('Constantia', 12, 'bold'), bg='#050206', fg='#fde4c3')
LabelTax.grid(row=1, column=2)

textTax = Entry(hargaFrame, font=('Calibri', 14, 'bold'), bd=6, width=16, state='readonly', textvariable=servicetaxvar)
textTax.grid(row=1, column=3, padx=41)

LabelHargaTotal =Label(hargaFrame, text='Harga Total', font=('Constantia', 12, 'bold'), bg='#050206', fg='#fde4c3')
LabelHargaTotal.grid(row=2, column=2)

textHargaTotal = Entry(hargaFrame, font=('Calibri', 14, 'bold'), bd=6, width=16, state='readonly', textvariable=totalcostvar)
textHargaTotal.grid(row=2, column=3, padx=41)

# membuat tampilan button struk (tombol pada frame kanan)
buttonTotal = Button(buttonFrame, text='Total', font=('arial', 12, 'bold'), fg='#fefefe', bg='#050206', bd=3, padx=12,
                     command=totalcost)
buttonTotal.grid(row=1, column=0)

buttonStruk = Button(buttonFrame, text='Struk', font=('arial', 12, 'bold'), fg='#fefefe', bg='#050206', bd=3, padx=12,
                     command=struk)
buttonStruk.grid(row=1, column=1)

buttonReset = Button(buttonFrame, text='Reset', font=('arial', 12, 'bold'), fg='#fefefe', bg='#FF0000', bd=3, padx=12,
                     command=reset)
buttonReset.grid(row=1, column=2)

# menentukan teks pada frame struk
textStruk = Text(strukFrame, font=('arial', 12, 'bold'), bd=3, width=45, height=26)
textStruk.grid(row=0, column=0)

root.mainloop()
