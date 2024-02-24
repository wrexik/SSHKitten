# SSHKitten 🐾

Welcome to Cat SSH Motd, a script that adds a touch of feline flair to your SSH login message of the day (motd).

## Setup

### Prerequisites
- Python 3.x
- Pip
- Git

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/wrexik/SSHKitten.git
    cd cat-ssh-motd
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure your API key:

    - Run the following command to create a default configuration file:
        ```bash
        cp config.ini.example config.ini
        ```

    - Open `config.ini` in a text editor and replace `YOUR_API_KEY` with your actual Cat API key.

## Configuration

To configure the Cat SSH Motd script, you need to set up your Cat API key in the `config.ini` file.

1. Open `config.ini` in a text editor:
    ```bash
    nano config.ini
    ```

2. Replace `YOUR_API_KEY` with your actual Cat API key.

3. Save and exit the editor.

## Usage

Once you have set up and configured the Cat SSH Motd, the cat ASCII art will be displayed in your terminal upon SSH login.

Enjoy the whimsical world of cats in your SSH sessions! 🐱🌟

## Dependencies

The project requires the following Python packages. You can install them using the command:
```bash
pip install -r requirements.txt
