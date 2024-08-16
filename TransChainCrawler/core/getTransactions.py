"Secaa Keseluruhan program untuk mengumpulkan transaksi dari alamat blockchain tertentu dan memproses informasi ini untuk dianalisis lebih lanjut."


from re import findall  # Mengimpor fungsi findall dari modul re untuk mencari pola dalam string
from core.utils import pageLimit  # Mengimpor fungsi pageLimit dari modul core.utils untuk menentukan batas halaman
from core.requester import requester  # Mengimpor fungsi requester dari modul core.requester untuk melakukan permintaan HTTP

def getTransactions(address, processed, database, limit):
    addresses = [] # Daftar untuk menyimpan alamat-alamat yang ditemukan
    increment = 0 # Inisialisasi variabel untuk menghitung kenaikan offset
    database[address] = {} # Inisialisasi entri baru dalam basis data untuk alamat yang diberikan
    pages = pageLimit(limit) # Menentukan jumlah halaman yang perlu diproses berdasarkan batas transaksi
    for i in range(pages):
        if pages > 1 and increment != 0:
            trail = '?offset=%i' % increment  # Membuat string jejak untuk mengatur offset jika lebih dari satu halaman
        response = requester(address) # Melakukan permintaan HTTP ke alamat yang diberikan
        matches = findall(r'"addr":".*?"', response)  # Mencari semua pola alamat dalam respons
        for match in matches:
            found = match.split('"')[3] # Mengekstrak alamat dari string yang cocok
            if found not in database[address]:
                database[address][found] = 0 # Jika alamat belum ada di basis data, inisialisasi dengan nilai 0
            database[address][found] += 1 # Menambahkan jumlah kemunculan alamat
            addresses.append(found) # Menambahkan alamat ke daftar alamat_lain
        increment += 50 # Menambahkan 50 ke offset untuk halaman berikutnya
        processed.add(address) # Menandai alamat sebagai sudah diproses
    return addresses # Mengembalikan daftar alamat yang ditemukan
