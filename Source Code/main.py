import argparse
import os

try :
    parser = argparse.ArgumentParser()
    parser.add_argument("save_data")
    args = parser.parse_args()
except :
    print("Tidak ada nama folder yang diberikan!")
    print()
    exit()

users = []
candi = []
bahan_bangunan = []

# Prosedur awal saat program pertama kali dijalankan
def Start() -> None :
    command = [["login", "Untuk masuk menggunakan akun"], ["load", "Untuk memuat file eksternal ke dalam permainan"], ["save", "Untuk menyimpan progress permainan ke file eksternal"], ["exit", "Untuk keluar dari program"]]
    print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil.")
    while True :
        prompt = input(">>> ")
        if (prompt == "login") : # Memanggil prosedur Login()
            Login()
            break
        if (prompt == "load") :
            Load()
            continue
        if (prompt == "save") :
            Save()
            continue
        if (prompt == "help") :
            Help(command)
            continue
        if (prompt == "exit") :
            Exit()
            break
        print(f"Command \"{prompt}\" tidak dikenali.")

# Prosedur Save :
def Save() -> None :
    dir = input("Masukkan nama folder: ")
    if not os.path.exists(dir):
        os.mkdir(dir)
    SaveTo(dir)

# Prosedur Save To :
def SaveTo(dir: str) -> None :
    # Membuka file .csv dengan akses write
    save_user = open(dir + "/user.csv", "w")
    save_candi = open(dir + "/candi.csv", "w")
    save_bahan_bangunan = open(dir + "/bahan_bangunan.csv", "w")

    # Merubah matriks ke dalam bentuk CSV
    string_user = ""
    for i in range(Length(users)) :
        for j in range(Length(users[0])) :
            string_user += users[i][j]
            if (j != Length(users[0]) - 1) :
                string_user += ";"
            else :
                string_user += "\n"
    
    string_candi = ""
    for i in range(Length(candi)) :
        for j in range(Length(candi[0])) :
            string_candi += candi[i][j]
            if (j != Length(candi[0]) - 1) :
                string_candi += ";"
            else :
                string_candi += "\n"
    
    string_bahan_bangunan = ""
    for i in range(Length(bahan_bangunan)) :
        for j in range(Length(bahan_bangunan[0])) :
            string_bahan_bangunan += bahan_bangunan[i][j]
            if (j != Length(bahan_bangunan[0]) - 1) :
                string_bahan_bangunan += ";"
            else :
                string_bahan_bangunan += "\n"

    # Menyimpan data dalam file
    save_user.write(string_user)
    save_candi.write(string_candi)
    save_bahan_bangunan.write(string_bahan_bangunan)

# Prosedur Load
def Load() -> None :
    dir = input("Masukkan nama folder: ")
    LoadTo(dir)

# Prosedur Load To
def LoadTo(dir: str) -> None :
    # Membuka file .csv dengan akses read
    try :
        load_user = open(dir + "/user.csv", "r")
        load_candi = open(dir + "/candi.csv", "r")
        load_bahan_bangunan = open(dir + "/bahan_bangunan.csv", "r")
    except :
        print()
        print(f"Folder \"{dir}\" tidak ditemukan.")
        exit()

    print("Loading...")

    # Menyimpan data dalam matriks ke variabel global
    global users
    global candi
    global bahan_bangunan
    users = ParseToMatrix(load_user.read(), ";")
    candi = ParseToMatrix(load_candi.read(), ";")
    bahan_bangunan = ParseToMatrix(load_bahan_bangunan.read(), ";")

    # Menutup file .csv
    load_user.close()
    load_candi.close()
    load_bahan_bangunan.close()

    print("Selamat datang di program “Manajerial Candi”")
    Start()

# Fungsi parser CSV to Matrix
def ParseToMatrix(str: str, split: str) -> list[list[str]] :
    a = ParseToArray(str, "\n")
    for i in range(Length(a)) :
        a[i] = ParseToArray(a[i], split)
    return a

# Fungsi parser CSV to Array
def ParseToArray(str: str, split: str) -> list[str] :
    split_length = Length(split)
    index = 0
    row = 0
    column = 0

    # Loop untuk menentukan ukuran list
    for i in range(Length(str)) :
        if (str[i] == split[index]) :
            index += 1
        else :
            index = 0
        
        if (index == split_length or i == Length(str) - 1) :
            row += 1
            index = 0
    
    # Mendefinisikan list
    list_data = [0 for j in range(row)]

    # Loop untuk assign value pada list
    x = 0
    index_temp = 0
    for i in range(Length(str)) :
        if (str[i] == split[index]) :
            index += 1
        else :
            index = 0
            
        row_value = ""
        if (index == split_length or i == Length(str) - 1) :
            if (index == split_length) :
                for j in range(index_temp, i - split_length + 1) :
                    row_value += str[j]
            else :
                for j in range(index_temp, i + 1) :
                    row_value += str[j]
            list_data[x] = row_value
            x += 1
            index_temp = i + split_length
            index = 0
        
    return list_data

# Fungsi untuk mencari panjang objek
def Length(object) -> int:
    count = 0
    for i in object :
        count += 1
    return count

# Prosedur untuk meminta input login
def Login() -> None:
    # Mengambil input username dan password
    username = input("Username: ")
    password = input("Password: ")

    # Mengambil data username dan password dari matriks users
    user_data = [users[i][0] for i in range(1, Length(users))]
    pass_data = [users[i][1] for i in range(1, Length(users))]

    # Validasi
    for i in range(len(user_data)) :
        if (username == user_data[i] and password == pass_data[i]) : # Jika username dan password sesuai
            print("")
            print(f"Selamat datang, {username}!")
            MainMenu(users[i + 1][2])
        elif (username == user_data[i]) : # Jika username sesuai namun password salah
            print("")
            print("Password salah!")
            Start()
        elif (i == len(user_data) - 1) : # Jika seluruh list username telah dicek dan tidak ditemui username dari input
            print("")
            print("Username tidak terdaftar!")
            Start()

# Prosedur menu utama
def MainMenu(role: str) -> None:
    print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil.")
    while True :
        prompt = input(">>> ")

        # Command yang dapat diakses role bandung_bondowoso
        if (role == "bandung_bondowoso") :
            command = [["logout", "Untuk keluar dari akun yang digunakan sekarang"], ["save", "Untuk menyimpan progress permainan ke file eksternal"], ["summonjin", "Untuk memanggil jin"]]

        # Command yang dapat diakses role roro_jonggrang
        if (role == "roro_jonggrang") :
            command = [["logout", "Untuk keluar dari akun yang digunakan sekarang"], ["save", "Untuk menyimpan progress permainan ke file eksternal"], ["hancurkancandi", "Untuk menghancurkan candi yang tersedia"]]

        # Command default
        if (prompt == "logout") : # Kembali ke prosedur awal jika logout
            Start()
            break
        if (prompt == "save") :
            Save()
            continue
        if (prompt == "help") :
            Help(command)
            continue

        print(f"Command \"{prompt}\" tidak dikenali.")

# Prosedur help
def Help(command: list[list[str]]) -> None : # Menerima argumen berupa list of list of string
    print("=========== HELP ===========")
    for i in range(len(command)) :
        print(f"{i + 1}. {command[i][0]}")
        print(f"   {command[i][1]}")

# Prosedur exit
def Exit() -> None :
    while True :
        prompt = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if (prompt == "y") :
            Save()
            exit()
        if (prompt == "n") :
            exit()

# Menjalankan prosedur awal
LoadTo(args.save_data)