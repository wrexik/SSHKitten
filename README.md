
# Cat SSH Motd 🐾

Welcome to Cat SSH Motd, your ticket to a purr-fectly delightful SSH login experience! 🐱✨

## Installation 🚀

### Prerequisites 🛠️

- Python 3.x
- Pip
- Git

### Clone the Repository

```bash
git clone https://github.com/wrexik/cat-ssh-motd.git
cd cat-ssh-motd
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Your Cat API Key
Get your API key [here](https://thecatapi.com/). Now, let's add a touch of personalization by updating the config:

```bash
nano config.ini
```

Replace `YOUR_API_KEY` with your actual Cat API key. Feel the feline magic! 🪄🐾

## Integration with SSH Motd Script 🛠️

To whisker-ly integrate the program with your SSH MOTD, follow these simple steps:
1. Locate your SSH MOTD scripts, usually nestled in ```/etc/motd.d/YOUR_SCRIPTS```
2. While in the directory, run ```nano myscript.sh``` (don't forget ```sudo``` if needed)
3. Add the following line: ```python3 /YOUR/PATH/TO/login.py```
4. Save and exit
5. Victory lap! 🎉

## Usage 🐱

Once the installation and configuration are complete, let the cat ASCII art give you a warm fuzzy welcome upon SSH login! 🌟

Now, dive into the whimsical world of cats in your terminal! 🐾✨

P.S. Enjoy the kitty company and may your coding sessions be fur-tastic! 🚀🐈
