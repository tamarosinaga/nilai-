def nilai():
    from texttable import Texttable
    table = Texttable ()

    print ("\n\tPROGRAM NILAI UJIAN\n")
    jawab = "y"
    no = 0
    nama = []
    nim =[]
    nilai_tugas = []
    nilai_uts = []
    nilai_uas = []
    
    

    while(jawab == "y"):
        nama.append(input("masukan nama : "))
        nim.append(input("masukan nim : "))
        nilai_tugas.append(input("nilai tugas : "))
        nilai_uts.append(input("nilai uts : "))
        nilai_uas.append(input("nilai uas : "))
        jawab = input("tambah data (y/t)? : ")
        no += 1

    for i in range(no):
        tugas = int(nilai_tugas[i])
        uts = int(nilai_uts[i])
        uas = int(nilai_uas[i])
        akhir = (tugas*30/100) + (uts*35/100) + (uas*35/100)
        table.add_rows([['No','Nama','NIM','TUGAS','UTS','UAS','AKHIR'],[i+1, nama[i],nim[i],nilai_tugas[i],nilai_uts[i],nilai_uas[i],akhir]])

    print (table.draw())

