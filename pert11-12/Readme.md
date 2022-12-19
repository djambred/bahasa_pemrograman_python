1. INSTALL XLAUNCH <br/>
bisa download di https://sourceforge.net/projects/vcxsrv/

2. masuk ke terminal ketikkan <br/>
apt-get install x11-xserver-utils

3. nano /root/.zshrc
tambahkan paling bawah <br/>
export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2; exit;}'):0 <br/>
export LIBGL_ALWAYS_INDIRECT=1 <br/>
export GDK_SYNCHRONIZE=1 <br/>
sudo /etc/init.d/dbus start &> /dev/null <br/>
export DISPLAY=$(echo $(grep nameserver /etc/resolv.conf | sed 's/nameserver //'):0.0) <br/>
export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2; exit;}'):0 <br/>
terus ctrl + x <br/>
terus y <br/>
terus enter <br/>

4. source /root/.zshrc

5. running xlaunch yang sudah di install <br/>
langsung di next aja <br/>
pilih start no client terus di next <br/>
jangan lupa centang Disable access control terus di next <br/>
terus di finish aja langsung <br/>

6. JIKA ADA YANG INGIN DITANYAKAN LANGSUNG HUBUNGI KETRIN di GROUP WAG BUKAN DI JAPRI TERIMA KASIH


# UNTUK GRAPH
pip install dash matplotlib numpy dash-bootstrap-components
