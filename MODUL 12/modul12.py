import mysql.connector

cnx=mysql.connector.connect(host='localhost',
                            user='root',
                            database='perhotelan')

def selectTamu(cnx):
    cursor=cnx.cursor()

    sql='SELECT*FROM Tamu'

    cursor.execute(sql)

    results=cursor.fetchall()
    print(results)

    print('data Tamu')

def selectKamar(cnx):
    cursor=cnx.cursor()

    sql='SELECT*FROM Kamar'

    cursor.execute(sql)

    results=cursor.fetchall()
    print(results)

    print('data Kamar')

def selectTransaksi(cnx):
    cursor=cnx.cursor()

    sql='SELECT*FROM Transaksi'

    cursor.execute(sql)

    results=cursor.fetchall()
    print(results)

    print('data Transaksi')

def tambahTamu(cnx):
    cursor=cnx.cursor()

    id_tamu=input('Masukkan id Tamu: ')
    nama_tamu=input ('Masukkan Nama Tamu: ')
    alamat_tamu=input ('Masukkan alamat Tamu: ')

    sql='INSERT INTO Tamu (id_tamu, nama_tamu, alamat_tamu) VALUES (%s, %s, %s)'
    val=(id_tamu, nama_tamu, alamat_tamu)

    cursor.execute(sql, val)
    cnx.commit()
    print('Berhasil ditambahkan')

def tambahKamar(cnx):
    cursor=cnx.cursor()

    no_kamar=input('Masukkan nomor kamar: ')
    jenis_kasur=input('Masukkan jenis kasur: ')
    harga_permalam=input('Masukkan harga/malam: ')

    sql='INSERT INTO Kamar (no_kamar, jenis_kasur, harga_permalam) VALUES (%s, %s, %s)'
    val=(no_kamar, jenis_kasur, harga_permalam)

    cursor.execute(sql, val)
    cnx.commit()
    print('Berhasil ditambahkan')

def tambahTransaksi(cnx):
    cursor=cnx.cursor()

    no_transaksi=input('Masukkan nomor transaksi: ')
    booking=input('Masukkan tanggal Booking: ')
    check_in=input('Masukkan tanggal check in: ')
    check_out=input('Masukkan tanggal check out: ')

    sql='INSERT INTO transaksi (no_transaksi, booking, check_in, check_out) VALUES (%s, %s, %s, %s)'
    val=(no_transaksi, booking, check_in, check_out)

    cursor.execute(sql, val)
    cnx.commit()
    print('Berhasil ditambahkan')

def hapusTamu(cnx):
    cursor=cnx.cursor()

    id_tamu=input('Masukkan id Tamu: ')
    sql='DELETE FROM Tamu WHERE id_tamu=%s'
    val=(id_tamu, )

    cursor.execute(sql, val)
    cnx.commit()

    print('Berhasil dihapus')

def hapusKamar(cnx):
    cursor=cnx.cursor()

    no_kamar=input('Masukkan nomor kamar: ')
    sql='DELETE FROM Kamar WHERE no_kamar=%s'
    val=(no_kamar, )

    cursor.execute(sql, val)
    cnx.commit()

    print('Berhasil dihapus')

def hapusTransaksi(cnx):
    cursor=cnx.cursor()

    no_transaksi=input('Masukkan nomor transaksi: ')
    sql='DELETE FROM Transaksi WHERE no_transaksi=%s'
    val=(no_transaksi, )

    cursor.execute(sql, val)
    cnx.commit()

    print('Berhasil dihapus')

def updateTamu(cnx):

    cursor=cnx.cursor()
    
    id_tamu=input('Masukkan id Tamu: ')
    nama_tamu=input ('Masukkan Nama baru: ')
    alamat_tamu=input ('Masukkan alamat baru: ')

    sql='UPDATE Tamu SET nama_tamu=%s, alamat_tamu=%s WHERE id_tamu=%s'
    val=(nama_tamu, alamat_tamu, id_tamu)

    cursor.execute(sql, val)
    cnx.commit()

    print('Berhasil update')

def updateKamar(cnx):

    cursor=cnx.cursor()
    
    no_kamar=input('Masukkan nomor kamar: ')
    jenis_kasur=input('Masukkan jenis baru: ')
    harga_permalam=input('Masukkan harga baru: ')

    sql='UPDATE Kamar SET jenis_kasur=%s, harga_permalam=%s WHERE no_kamar=%s'
    val=(jenis_kasur, harga_permalam, no_kamar)

    cursor.execute(sql, val)
    cnx.commit()

    print('Berhasil update')

def updateTransaksi(cnx):

    cursor=cnx.cursor()
    
    no_transaksi=input('Masukkan nomor transaksi: ')
    booking=input('Masukkan tanggal Booking baru: ')
    check_in=input('Masukkan tanggal check in baru: ')
    check_out=input('Masukkan tanggal check out baru: ')

    sql='UPDATE Transaksi SET booking=%s, check_in=%s, check_out=%s WHERE no_transaksi=%s'
    val=(booking, check_in, check_out, no_transaksi)

    cursor.execute(sql, val)
    cnx.commit()

    print('Berhasil update')


print("=====Aplikasi Database PERHOTELAN=====")
print("1.Select")
print("2.Insert")
print("3.Delete")
print("4.Update")
print("0.Keluar")
menu=input("Pilih perintah : ")
print("===========================")
print("1.Tamu")
print("2.Kamar")
print("3.Transaksi")
menu2=input("Pilih entitas : ")

if menu=="1":
    if menu2=="1":
        selectTamu(cnx)
    elif menu2=="2":
        selectKamar(cnx)
    elif menu2=="3":
        selectTransaksi(cnx)

elif menu=="2":
    if menu2=="1":
        tambahTamu(cnx)
    elif menu2=="2":
        tambahKamar(cnx)
    elif menu2=="3":
        tambahTransaksi(cnx)
        
elif menu=="3":
    if menu2=="1":
        hapusTamu(cnx)
    elif menu2=="2":
        hapusKamar(cnx)
    elif menu2=="3":
        hapusTransaksi(cnx)
        
elif menu=="4":
    if menu2=="1":
        updateTamu(cnx)
    elif menu2=="2":
        updateKamar(cnx)
    elif menu2=="3":
        updateTransaksi(cnx)
    
    
elif menu=="0":
    exit()
else:
    print("salah")
