# Antrian Wisuda untuk Prosesi Pindah Kuncir
nahh... kalau https://github.com/nurrachmat-nr/aplikasiantrian berbasis PHP, kali ini berbasis node.js dan Python..
Aplikasi ini belum menggunakan basisdata DBMS, melainkan sekedar file json saja.
Kedepannya bisa kalian kembangkan sendiri jika ingin menggunakan DBMS.

Aplikasi ini dijamin mengurangi beban MC pada hari H Wisuda. Karena suara panggilan wisudawaan bisa disiapkan terlebih dahulu jauh-jauh hari.
Tapi jika masih tetap menggunkan cara lama dalam  pemanggilan wisudawan, itu selera PT masing-masing ya..
Oiya, suara panggilan harus disimpan dengan format .mp3, kl mau format lain silakan koding sendiri.. 

# Installasi (Windows)
Pastikan gunakan Python 2.7 dan node.js udah diinstall.  
1. copy file websocketd-0.2.11-windows_386 ke folder windows/system32
2. buka cmd kemudian ketik websocketd --staticdir=./view --dir=./bin --port=8080
3. buka chrome pertama kemudian ketik alamat localhost:8080
4. buka chrome kedua kemudian ketik alamat localhost:8080/control.html

# Tampilan UI
![alt text](https://i.ibb.co/FKJ3w4S/pindahkuncir.png)
