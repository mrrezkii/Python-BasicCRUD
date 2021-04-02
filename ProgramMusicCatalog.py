import mysql.connector                                          # import lib mysql connector
from beautifultable import BeautifulTable                       # import beautiful table
from tkinter.filedialog import askopenfilename

import tkinter as tk
from PIL import Image, ImageTk
import glob

class MusicCatalog():                                           # Kelas Music Dialog
    def readMusic(self):                                        # method read music
        cursor = db.cursor()                                    # variable untuk akses db
        sql = "SELECT * FROM `music`"                           # query sql untuk mengambil semua data
        cursor.execute(sql)                                     # eksekusi sql
        results = cursor.fetchall()                             # simpan hasil sql kedalam var result
        
        table = BeautifulTable()                                # deklrasi table

        table.column_headers = ['Id', 'Judul Musik', 'Album', 'Artis', 'Cover Album']       # pembuatan table
        for row in results:                                     # looping table
            table.append_row([row[0], row[1], row[2], row[3], row[4]])      # append data
        print(table)                                            # print table

        
    def insertMusic(self):                                      # method insert music
        try:                                                    # try blok : checking condition error
            isJudul = input("Masukkan judul musik           : ")    # input judul
            if not isJudul:                                         # jika judul kosong
                print("Data harus diisi")                           # notif
                return                                              # hentikan method
            isAlbum = input("Masukkan nama album            : ")    # input album
            if not isAlbum:                                         # jika album kosong
                print("Data harus diisi")                           # notif
                return                                              # hentikan method
            isArtis = input("Masukkan nama artis            : ")    # input artis
            if not isArtis:                                         # jika artis kosong
                print("Data harus diisi")                           # notif
                return                                              # hentikan method
            isCover = input("Masukkan gambar album          : ")    # input cover
            if not isCover:                                         # jika cover kosong
                print("Data harus diisi")                           # notif
                return                                              # hentikan method
        except ValueError as e:
            print(e)
        else:
            cursor = db.cursor()                                # variable untuk akses db
            sql = "INSERT INTO `music`(`judul_musik`, `album`, `artis`, `cover_album`) VALUES (%s, %s, %s, %s)"     # query sql untuk mengambil semua data
            val = (isJudul, isAlbum, isArtis, isCover)          # pengisian %s
            cursor.execute(sql, val)                            # eksekusi db
            db.commit()                                         # commit ke db
            print("Successfull insert data")                    # notif

    def updateMusic(self):                                      # method update music
        try:
            cursor = db.cursor()                                # method read music
            isId = int(input("Masukkan id yang ingin di update \t: "))  # input id
            print('''
                DATA YANG INGIN DI UPDATE
                1. Judul
                2. Album
                3. Artis
                4. Cover
            ''')
            isOption = int(input("Masukkan bagian data yang ingin di update \t:"))      # input Option
        except ValueError:                                      # jika ada value error
            print("Data yang Anda input tidak valid")           # notif
        else:                                                   # jika tidak ada value error
            if isOption == 1:                                   # jika option pilih 1
                isData = input("Ingin diganti dengan data \t :")        # input data
                sql = "UPDATE `music` SET `judul_musik`=%s  WHERE id=%s"        # query sql untuk mengambil semua data
                val = (isData, isId)
                cursor.execute(sql, val)
                db.commit()
                print("Successfull update judul")
            elif isOption == 2:
                isData = input("Ingin diganti dengan data \t :")
                sql = "UPDATE `music` SET `album`=%s  WHERE id=%s"              # query sql untuk mengambil semua data
                val = (isData, isId)
                cursor.execute(sql, val)
                db.commit()
                print("Successfull update album")
            elif isOption == 3:
                isData = input("Ingin diganti dengan data \t :")
                sql = "UPDATE `music` SET `artis`=%s  WHERE id=%s"              # query sql untuk mengambil semua data
                val = (isData, isId)
                cursor.execute(sql, val)
                db.commit()
                print("Successfull update artis")
            elif isOption == 4:
                isData = input("Ingin diganti dengan data \t :")
                sql = "UPDATE `music` SET `cover_album`=%s  WHERE id=%s"        # query sql untuk mengambil semua data
                val = (isData, isId)
                cursor.execute(sql, val)
                db.commit()
                print("Successfull update cover")


    def deleteMusic(self):                                     # method delete music
        try:
            isJudul = int(input("Masukan id yang ingin di hapus :"))
            if not isJudul:
                print("Data harus diisi")
                return
        except ValueError as e:
            print(e)
        else:
            isOption = input("Apakah Anda yakin ingin menghapus (Y/N)")
            if isOption == "Y" or isOption == "y":
                cursor = db.cursor()                                # variable untuk akses db
                sql = "DELETE FROM `music` WHERE id=%s"    # query sql untuk mengambil semua data
                val = (isJudul, )
                cursor.execute(sql, val)
                db.commit()
                print("Successfull delete data")
            elif isOption == "N" or isOption == "n":
                print("Data tidak jadi dihapus")
            else:
                print("Anda memasukkan pilihan yang salah")


    def searchJudul(self):                                    # method search judul
        try:
            isData = input("Masukan judul yang ingin di dicari :")
            if not isData:
                print("Data harus diisi")
                return
        except ValueError as e:
            print(e)
        else:
            cursor = db.cursor()                            # variable untuk akses db
            sql = "SELECT * FROM `music` WHERE `judul_musik` LIKE %s"       # query sql untuk mengambil semua data
            val = ("%"+isData+"%", )
            cursor.execute(sql, val)
            results = cursor.fetchall()

            table = BeautifulTable()

            table.column_headers = ['Id', 'Judul Musik', 'Album', 'Artis', 'Cover Album']
            for row in results:
                table.append_row([row[0], row[1], row[2], row[3], row[4]])
            print(table)

    def searchAlbum(self):                                   # method search album
        try:
            isData = input("Masukan judul yang ingin di dicari :")
            if not isData:
                print("Data harus diisi")
                return
        except ValueError as e:
            print(e)
        else:
            cursor = db.cursor()                            # variable untuk akses db
            sql = "SELECT * FROM `music` WHERE `album` LIKE %s"     # query sql untuk mengambil semua data
            val = ("%"+isData+"%", )
            cursor.execute(sql, val)
            results = cursor.fetchall()

            table = BeautifulTable()

            table.column_headers = ['Id', 'Judul Musik', 'Album', 'Artis', 'Cover Album']
            for row in results:
                table.append_row([row[0], row[1], row[2], row[3], row[4]])
            print(table)

    def searchArtis(self):                                  # method search artis
        try:
            isData = input("Masukan judul yang ingin di dicari :")
            if not isData:
                print("Data harus diisi")
                return
        except ValueError as e:
            print(e)
        else:
            cursor = db.cursor()                            # variable untuk akses db
            sql = "SELECT * FROM `music` WHERE `artis` LIKE %s" # query sql untuk mengambil semua data
            val = ("%"+isData+"%", )
            cursor.execute(sql, val)
            results = cursor.fetchall()

            table = BeautifulTable()

            table.column_headers = ['Id', 'Judul Musik', 'Album', 'Artis', 'Cover Album']
            for row in results:
                table.append_row([row[0], row[1], row[2], row[3], row[4]])
            print(table)
    
    
    def convertToBinaryData(self, filename):
        with open(filename, 'rb') as file:                  # open file as path
            binaryData = file.read()                        # Konversi ke binary
        return binaryData                                   # return data binary

    def insertImage(self):                                  # method insert image
        filename = askopenfilename()                        # buka file
        filename = self.convertToBinaryData(filename)       # konversi ke binary

        cursor = db.cursor()                                # variable untuk akses db
        sql = "INSERT INTO `upload`(`cover_album`) VALUES (%s)"
        val = (filename, )

        cursor.execute(sql, val)
        db.commit()
        print("Successfull insert data")

    def openImage(self):
        root = tk.Tk()

        labels = []

        filename = askopenfilename()

        for jpeg in glob.glob(filename)[:5]:
            im = Image.open(jpeg)
            im.thumbnail((96, 170), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(im)
            label = tk.Label(root, image=photo)
            label.pack()    
            label.img = photo 
            labels.append(label)

        root.mainloop()

    def getImage(self):
        root = tk.Tk()

        labels = []

        cursor = db.cursor()
        sql = "SELECT `cover_album` FROM `upload` WHERE id_image=%s"
        val = (8, )
        cursor.execute(sql, val)
        result = cursor.fetchall()

        for jpeg in glob.glob(result)[:5]:
            im = Image.open(jpeg)
            im.thumbnail((96, 170), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(im)
            label = tk.Label(root, image=photo)
            label.pack()    
            label.img = photo 
            labels.append(label)

        root.mainloop()



if __name__ == "__main__":
    print('''
        Menu Music Catalog :

        1. Lihat Daftar Musik
        2. Masukkan Musik
        3. Update Data Musik
        4. Hapus Daftar Musik
        5. Cari musik (judul)
        6. Cari musik (album)
        7. Cari musik (artis)
        8. Upload Image
        9. Open Image
        10. Get image from DB
    ''')


    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="musiccatalog"
        )
    except mysql.connector.Error as er:
        print("Gagal tersambung dengan database", er)
    else:
        musicCatalog = MusicCatalog()

        try:
            isOption = int(input("Masukkan menu \t :"))
        except ValueError:
            print("Menu yang Anda masukkan tidak valid")
        else:
            if isOption == 1:
                musicCatalog.readMusic()
            elif isOption == 2:
                musicCatalog.insertMusic()
            elif isOption == 3:
                musicCatalog.updateMusic()
            elif isOption == 4:
                musicCatalog.deleteMusic()
            elif isOption == 5:
                musicCatalog.searchJudul()
            elif isOption == 6:
                musicCatalog.searchAlbum()
            elif isOption == 7:
                musicCatalog.searchArtis()
            elif isOption == 8:
                musicCatalog.insertImage()
            elif isOption == 9:
                musicCatalog.openImage()
            elif isOption == 10:
                musicCatalog.getImage()
            else:
                print("Menu yang Anda masukkan tidak tersedia")