import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(a+'+'*55)
print(a+'\t     SECRET KEY TERMUX BY SANTRI CYBER')
print(b+'\t Follow IG: santri.cyberteam')
print(b+'\t blog     : https://santricoder.blogspot.com')
print(a+'\t Github   : https://github.com/SantriCyber')
print(a+'+'*55)
print(b+'\t Coding by: santri kaliwungu eL 4ZzKUrY 4sY4')
print(a+'+'*55)
os.system('xdg-open https://www.instagram.com/santri.cyberteam')
print(a+'\t|\   >| +-----\  +++++++++++  #--\.')
print(a+'\t| \   | |             +       #    \.')
print(a+'\t|  \  | |   *\        +       #     |')
print(a+'\t|   \ | |  *  \|      +       #    ./')
print(a+'\t|>   \| +______|      +       #----/awokawokawok')
print('\nProses..')
sleep(1)
print(b+'\n[!] making termux properties directory..')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Success !')
sleep(1)
print(b+'\n[!] Making setup file..')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[!] Success !')
sleep(1)
print(b+'\n[!] Setting up..')
sleep(2)
os.system('termux-reload-settings')
print(a+'[!] Successfully !! ^^'+c+'\n\n[!]https://santricoder.blogspot.com \n++++++++++++++++++++++++++++++++ \nuntuk requests atau pertanyaan dll. [!] hubungi: \n++++++++++++++++++++++++++++++++ \nIG author: Santri-Cyber \n++++++++++++++++++++++++++++++++ \nJangan lupa follow instagram saya: \nhttps://www.instagram.com/santri.cyberteam \nThanks :*\n\n')
os.system('xdg-open https://santricoder.blogspot.com')

# ini cuma shortcut buat bantu para nub
# AZZKURY AL ASYA
