
#mendefinisikan variabel pria
def pria(p):

    # menghitung jumlah huruf yang biasanya terdapat pada nama gender pria
    i = 0
    for n in range(0,len(name)):
        if p[n]=="b" :
            i = i+1
        elif p[n]=="d" :
            i = i+1
        elif p[n]=="o" :
            i = i+1
    return i

#mendefinisikan fungsi wanita
def wanita(w):
    # menghitung jumlah huruf yang biasanya terdapat pada nama gender wanita
    i = 0
    for n in range(0,len(name)):
        if w[n] == "a" :
            i = i+1
        elif w[n] == "u" :
            i = i+1
        elif w[n] == "e" :
            i = i+1
        elif w[n] == "t" :
            i = i+1
        elif w[n] == "l" :
            i = i+1
    return i


#menginputkan nama yang akan diprediksi
name = input("Nama : ")

#penentuan jenis gender dari inputan nama
if pria(name) > wanita(name) :
    print ('Jenis Kelamin : Pria')
elif wanita(name) > pria(name) :
    print('Jenis Kelamin : Wanita')
else: print('Jenis Kelamin : Tidak Diketahui')


#setelah dilakukan beberapa kali percobaan ternyata keakuratan dari prediksi nama masih diragukan kebenarannya karena masih banyak nama bergender pria disebutkan bergender wanita
