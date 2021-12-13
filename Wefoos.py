def garis ():
    print(100*"-")

#Menu
print("                                       WEFOOS ID                                      ")
print("                            Tempat Clothing untuk milenial                            ")
print("-------------------------------------------|------------------------------------------")
print("Kode      Outwear               Harga      |  Kode       Pants                Harga   ")
print("-------------------------------------------|------------------------------------------")
print("TS        T-Shirt               Rp. 100000 |  JN        Jeans               Rp. 150000")
print("CW        Crewneck              Rp. 100000 |  CH        Chino               Rp. 100000")
print("HD        Hoodie                Rp. 130000 |  AP        Ankle               Rp. 120000")
print("FL        Flannel               Rp. 120000 |  JP        Jogger              Rp. 120000")
print("-------------------------------------------|------------------------------------------")

print("\n")

#Batasan
banyak=int(input("Banyak Data : "))

#list
listbanyak_beli=[]                                   # jadi didalam [] ada variabel setelah di input
listkode=[]


#Input
for i in range(banyak):                              #fungsi i untuk menyimpan nilai dari perulangan
    print("\nData Ke-",i+1)
    kode_data=input("Kode Outwear [TS/CW/HD/FL] Kode Pants [JN/CH/AP/JP] : ")
    listkode.append(kode_data)                        #untuk memasuk kan kode_ptg kedalam listkode
    banyak_beli=int(input("Banyak Beli : "))
    listbanyak_beli.append(banyak_beli)

jmlh_byr = input("\nJumlah Bayar : ")

#output head
print("                         WEFOOS ID                              ")
garis()
print("No.   | Jenis          | Harga        |Banyak                   | Sub Total")
print("      |                | Satuan Beli                                       ")
garis()

#Proses Oprasi
jmlh_hrg=0
for i in range(banyak):
    #fungsi if
    if listkode[i] =="TS" or listkode[i] =="ts":
        jns_nama="T-Shirt"
        harga_satuan=100000
    elif listkode[i] =="RB" or listkode[i] =="rb":
        jns_nama="Crewneck"
        harga_satuan=100000
    elif listkode[i] =="HD" or listkode[i] =="hd":
        jns_nama="Hoodie"
        harga_satuan=130000
    elif listkode[i] =="FL" or listkode[i] =="fl":
        jns_nama="Flannel"
        harga_satuan=120000
    elif listkode[i] =="JN" or listkode[i] =="jn":
        jns_nama="Jeans"
        harga_satuan=150000
    elif listkode[i] =="CP" or listkode[i] =="cp":
        jns_nama="Chino"
        harga_satuan=100000
    elif listkode[i] =="AP" or listkode[i] =="ap":
        jns_nama="Ankle"
        harga_satuan=120000
    elif listkode[i] =="JP" or listkode[i] =="jp":
        jns_nama="Jogger"
        harga_satuan=120000
        
    else:
        print("Maaf, kode tidak ditemukan")
        (exit)


    #operasi Subtotal
    subtotal=harga_satuan * listbanyak_beli[i]
    jmlh_hrg=jmlh_hrg+subtotal
    #PPN/PAJAK 10%
    pjk=jmlh_hrg*0.1
    #operasi kembali
    Kembali=int (jmlh_byr) - int (jmlh_hrg) - int(pjk)
    

    print(i+1,"    ",jns_nama,"\t\t",harga_satuan,"       ",listbanyak_beli[i],"     \t\t\t"  ,subtotal )
    
garis()
print("                                                     Total Bayar  Rp.",(jmlh_hrg))
print("                                                     PPN          Rp.",(pjk))
print("                                                     Jumlah Bayar Rp.",jmlh_byr)
print("                                                     -----------------------------------------------")
print("                                                     Kembali      Rp.",Kembali)
print("                                                     -----------------------------------------------")
print("Terima kasih sudah berbelanja di toko kami, semoga hari anda menyenangkan :) ")
