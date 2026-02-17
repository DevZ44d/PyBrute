<p align="center">
    <img align="center" width="300" src="https://github.com/user-attachments/assets/06a24597-888c-4813-8577-60f7951bfbe9" />
    <h3 align="center"></h3>
</p>

<p align="center">
  <a href="https://pypi.org/project/PyBrute/">
    <img src="https://img.shields.io/pypi/v/PyBrute.svg?logo=python&logoColor=blue&label=pypi&labelColor=%23282f37">
  </a>
  
  <a href="https://t.me/PyCodz">
    <img src="https://img.shields.io/badge/Telegram-Channel-blue.svg?logo=telegram">
  </a>
    
  <a href="https://t.me/PyCodz_Chat" target="_blank">
    <img alt="Telegram-Discuss" src="https://img.shields.io/badge/Telegram-Discuss-blue.svg?logo=telegram" />
  </a>
</p>

<p align="center">

  <a href="https://pepy.tech/projects/PyBrute/">
    <img src="https://static.pepy.tech/personalized-badge/pybrute?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=blue&left_text=downloads">
  </a>

  <a href="https://pepy.tech/projects/PyBrute/">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg">
  </a>
</p>


### PyBrute - Hash & ZIP BruteForce Tool .
> **_PyBrute_** is a lightweight yet powerful CLI tool for performing brute-force attacks on **Hashes** and **ZIP files** using custom wordlists.

### 🚀 Features:

- 🔐 Crack multiple hashes at once .
- 📦 Brute-force password protected ZIP files .
- 📂 Support multiple wordlists .
- ⚡ Fast and lightweight .
- 🚀 Random Banners .
- 🎨 Colored terminal output .
- 🧠 Clean and simple CLI interface .


### 📦 Installation

- Clone the project:
```shell
git clone https://github.com/DevZ44d/PyBrute.git
```

- Via PyPi
```shell
pip install PyBrute -U
```
### 🧠 Usage Example (_Class Hash_)
- 🔑 Crack Hash (Coding) .

```python
from pybrute.Hashing import BruteForce

def main():
    response = BruteForce()
    response.brute(
        hashes=[
            "5f4dcc3b5aa765d61d8327deb882cf99",  # password
            "e10adc3949ba59abbe56e057f20f883e",  # 123456
            "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"  # SHA-256 "abc"
        ],
        wordlists=[
            "../wordlists/wardlist.txt",
            "../wordlists/rockyou.txt"
        ]
    )

if __name__ == "__main__":
    main()
```

### 🧠 Usage Example (_Class Zip_)
- 📦 Crack ZIP File (Coding) .

```python
from pybrute.Ziping import BruteForce

def main():
    cracker = BruteForce()
    cracker.start(zip_files=[
            "deep.zip"
        ],
        wordlists=["../wordlists/wardlist.txt"]
    )

if __name__ == "__main__":
    main()
```

### Class Terminal 🧠
```shell
PyBrute - Advanced Hash & ZIP BruteForce Tool
Usage:
        PyBrute -[OPTIONS] "[FOR-OPTION]"

Options:
  -H, --hash          Hash to crack (can be used multiple times).
  -Z, --zip           ZIP file to crack (can be used multiple times).
  -w, --wordlist      Wordlist file (can be used multiple times).
  -v, --version       Show PyBrute version.
  -h, --help          Show this help message.
```

### 🚀 Usage (_Class Terminal_)
- 🔑 Crack Hash with wordlist (required):

```shell
PyBrute -H "5f4dcc3b5aa765d61d8327deb882cf99" -w wordlists/rockyou.txt # you can add wordlist but that's working
```

- 🔹Multiple Hashes:
```shell
PyBrute -H "5f4dcc3b5aa765d61d8327deb882cf99" -H "e10adc3949ba59abbe56e057f20f883e" -w wordlists/rockyou.txt -w wordlists/wardlist.txt

```

- 📦 Crack ZIP File:
```shell
PyBrute -Z secret.zip -w wordlista/rockyou.txt # Make sure add file (zip) in the directory
```

- 🔹 Multiple ZIP Files:
```shell
PyBrute -Z file1.zip -Z file2.zip -w wordlists/rockyou.txt -w wordlists/wordlist.txt
```

- 🔹 Show version:
```shell
PyBrute -v
```
- 🔹 Show help:
```shell
PyBrute -h
```

### 💬 Help & Support .
- Follow updates via the **[Telegram Channel](https://t.me/Pycodz)**.

- For general questions and help, join our **[Telegram chat](https://t.me/PyCodz_Chat)**.



