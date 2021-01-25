# TUCIL 1 IF2211: Cryptarithmetic Solver dengan Algoritma Brute Force
<div align = "center"><img src = "bin/New folder/Untitled-2.png" width = 200px></div>
Program ini dibuat untuk memenuhi tugas kecil dari mata kuliah IF2211 Strategi Algoritma Semester 2 tahun 2020/2021. Program memiliki fungsi mencari solusi dari suatu persoalan cryptarithmetic dengan menggunakan algoritma <b>Brute Force</b>. 
<br><br>Secara sederhana, pertama program membuka file berisi persoalan cryptarithmetic. Kemudian program <b>membuat himpunan</b> huruf yang muncul dalam persoalan tersebut. Lalu, program menghasilkan <b>permutasi</b> dari 10 digit yang mungkin, kemudian himpunan huruf sebelumnya dibuat <b>mapping</b> ke hasil permutasi tadi. Terakhir, program meng<b>kalkulasi</b> hasil substitusi terhadap operand dan hasil. Jika hasilnya sama, akan ditampilkan mapping yang digunakan, jika tidak, dicari mapping permutasi yang lain hingga seluruh permutasi selesai.

## Program berjalan normal dengan spesifikasi:
* Windows 10 64-bit
* Python 3.9.1 64-bit

## Cara menggunakan:
Dikarenakan program tidak berhasil dikonversi ke dalam satu executable file, maka program perlu dijalankan dalam command prompt untuk memastikan berhasil bekerja.<br>
1. Akses folder src, pastikan terdapat cryp_solver.py
2. Akses folder test, pastikan terdapat file uji, dengan format sampeX.txt (X adalah angka 0 - 9)
3. Buka command prompt, lalu ganti direktori ke dalam folder src tadi
4. Tuliskan perintah: py cryp_solver.py
5. Program akan berjalan dengan sendirinya, sampai seluruh file dalam folder test dibaca

## Tentang Pembuat
Program ini dibuat oleh Aurelius Marcel Candra (NIM 13519198) sebagai mahasiswa semester 4 IF ITB pada Januari 2021. Program ini bebas untuk digunakan. Terima kasih atas perhatiannya.
<br><br>
Logo yang disertakan tidak memiliki maksud apapun (~~kecuali Anda adalah penikmat siksaan gacha~~). Sebatas kreasi penulis dikarenakan tidak ada ketentuan untuk logo dalam laporan. Diduga penulis tidak berniat menampilkan wajahnya  dan gajah kemungkinan besar bukan hewan favorit penulis.
