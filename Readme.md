# Introduction Programming with Python
buka powershell dengan run administrator

setelah itu ketikkan wsl --update

tunggu sampai proses selesai

ketikkan Ubuntu config --default-user root

jika sudah buka terminal dan pilih ubuntunya

ketikkan apt install zsh -y terus enter

setelah itu ketikkan sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

ketikkan clear terus enter

ketikkan git clone https://github.com/zsh-users/zsh-autosuggestions.git $ZSH_CUSTOM/plugins/zsh-autosuggestions

ketikkan git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting

ketikkan nano /root/.zshrc terus enter

terus tekan ctrl+w ketikkan plugin terus enter dan tekan panah bawah sehingga menjadi

plugins=(git zsh-autosuggestions zsh-syntax-highlighting)

setelah selesai tekan ctrl+x terus y terus enter setelah itu ketikkan source /root/.zshrc

buka browser kalian dan masuk ke akun github masing-masing 
setelah itu ambil setting account kalian dan cari SSH dan GPG Keys terus add new ssh key

balik ke terminal ubuntunya ketikkan ssh-keygen
terus enter saja sampai selesai dan keluar text gambar

setelah itu cat /root/.ssh/id_rsa.pub terus enter
copykan semua itu ke dalam github masing-masing

buat new repository di github masing-masing
dan di teminal ketikkan mkdir bp terus enter
ketikkan cd bp enter terus ketikkan mkdir pert1 enter dan ketikkan touch Readme.md terus enter
dan selesai itu ketikkan code .

ketikkan git init enter
git add . enter
git commit -m "test"
git branch -M main
git remote ssh ambil di github masing-masing
git push -u origin main


di terminal ubuntu ketikkan apt install g++ gcc -y
buat file test.cpp di folder pert1
dan file python.py di folder pert1
isi file test.cpp seperti dibawah ini
#include <iostream>
using namespace std;

int main(){
cout << "hello";
return 0;
}


isi file python.py seperti dibawah ini
a = 1
b = 2
c = a+b
print(c)

balik ke terminal ubuntu lakukan perintah gcc test.cpp -o test
ketikkan ./test (untuk running c++)

ketikkan python3 python.py 


buka terminal ubuntunya 
ketikkan cd bp/pert1

lakukan perintah 
git add .
git commit -m "perubahan"
git push -u origin main
























