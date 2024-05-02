## Tidal-AutoDL

Tools for exporting Tidal links from a file and storing them, deleting duplicates, and automatically downloading media with [tidal-dl](https://github.com/yaronzz/Tidal-Media-Downloader).

For example, from a Whatsapp chat export, or a messaging system where you self-send links, from the share option on the Tidal application.

![Screenshot--01](https://github.com/SunL0w/Tidal-AutoDL/blob/main/Screenshot/Screenshot-01.png)

You have two tools at your disposal:  
tidal-auto\_export.py \<- To extract Tidal links and put them in a file. 

tidal-auto\_dl.py \<- To automatically download each link contained in the final "clean\_tidal\_export.txt" file.

## :loudspeaker: Disclaimer

*   Private use only.
*   Need a Tidal-HIFI subscription.
*   You should not use this method to distribute or pirate music. :underage:
*   It may be illegal to use this in your country, so be informed.

## Installation

Clone the repository :

```bash
git clone https://github.com/SunL0w/Tidal-AutoDL
```

```bash
cd Tidal-AutoDL
```

```bash
sudo python3 -m pip install -r requirements.txt
```

## Launch

:exclamation: Your **source file** must be placed in the **same directory** as Tidal-AutoDL, and **named** "source.txt".

```bash
python3 tidal-auto_export.py
```

:warning: You need to **configure** tidal-dl first, read the documentation [here](https://doc.yaronzz.com/post/tidal_dl_installation/).

```bash
tidal-auto_dl.py
```

## Screenshots

![Screenshot--02](https://github.com/SunL0w/Tidal-AutoDL/blob/main/Screenshot/Screenshot--02.png)

![Screenshot--03](https://github.com/SunL0w/Tidal-AutoDL/blob/main/Screenshot/Screenshot--03.png)

![Screenshot--04](https://github.com/SunL0w/Tidal-AutoDL/blob/main/Screenshot/Screenshot--04.png)

---

## 🤝 Grateful thanks to :

[Yaronzz](https://github.com/yaronzz) The creator of [tidal-dl](https://github.com/yaronzz/Tidal-Media-Downloader/tree/master).

___

## Lead Developper :
<a href="https://github.com/SunL0w/" alt="SunLow GitHub Link">
<img src="https://img.shields.io/badge/SunL0w-Dind%20Thibault-blue"  alt="Developper SunL0w"/></a>
