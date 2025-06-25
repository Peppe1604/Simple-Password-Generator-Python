# 🔐 Advanced Password Generator

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6%2B-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Version-2.0-orange.svg" alt="Version">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20MacOS-lightgrey.svg" alt="Platform">
</p>

<p align="center">
  <strong>A secure and user-friendly password generator with colorful terminal interface</strong>
  <br />
  <em>✨ Now with automatic installation for all platforms! ✨</em>
  <br /><br />
  <a href="#-installation">Quick Installation</a> •
  <a href="#-demo">Demo</a> •
  <a href="#-features">Features</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-contributing">Contributing</a>
</p>

---

## 🚀 Quick Start

```bash
# Linux/macOS
./install.sh

# Windows
install.bat
```

---

## 📋 Table of Contents

- [Quick Start](#-quick-start)
- [What's New in v2.0](#-whats-new-in-v20)
- [Demo](#-demo)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Uninstallation](#️-uninstallation)
- [Code Structure](#-code-structure)
- [Available Options](#-available-options)
- [Security](#-security)
- [FAQ](#-faq)
- [Contributing](#-contributing)
- [Author](#-author)
- [License](#-license)

## 🆕 What's New in v2.0

- ✅ **Automatic installation scripts** for all platforms
- ✅ **Colorful interface** with ASCII art and animations
- ✅ **Real-time security evaluation** with visual strength bar
- ✅ **Customizable passwords** with interactive character selection
- ✅ **Loading animations** during generation
- ✅ **Decorative boxes** for more readable output
- ✅ **Uninstallation scripts** included

## 🎬 Demo

<p align="center">
  <img src="demo.gif" alt="Password Generator Demo" width="600">
</p>

> *Example of generating a secure password with strength evaluation*

## ✨ Features

### 🎨 User Interface
- **Colorful output**: Terminal interface with ANSI colors for better readability
- **ASCII Art**: Attractive banner at startup
- **Animations**: Loading animations during generation
- **Decorative boxes**: Organized output in boxes and tables

### 🔐 Security Features
- **Cryptographic generation**: Uses the `secrets` module for secure generation
- **Strength evaluation**: Real-time password security analysis
- **Customizable passwords**: Choose exactly which characters to include
- **Character guarantee**: Secure passwords always include all character types

### 💾 Password Management
- **Optional saving**: Save generated passwords with custom labels
- **Timestamp logging**: Each saved password includes generation date and time
- **Output file**: All saved passwords in `passwords_generate.txt`

### 📦 Installation and Portability
- **Automatic installation scripts**: One-click setup for Windows, Linux and macOS
- **Zero dependencies**: Uses only Python standard libraries
- **Cross-platform**: Works on all operating systems
- **Clean uninstallation**: Removal scripts included

## 🛠️ Requirements

### Minimum Requirements
- **Python**: 3.6 or higher
- **Operating System**: Windows, Linux, macOS
- **Terminal**: With ANSI color support (most modern terminals)

### Dependencies
The project uses only Python standard libraries:
- `string` - Character handling
- `secrets` - Cryptographic generation
- `time` - Animations and timestamps
- `os` - System operations
- `sys` - System information
- `datetime` - Date and time handling

## 📦 Installation

### 🚀 Automatic Installation (Recommended)

The project includes automatic installation scripts for all platforms:

#### 🐧 Linux / macOS

```bash
# 1. Clone the repository
git clone https://github.com/Peppe1604/Simple-Password-Generator-Python.git
cd Simple-Password-Generator-Python

# 2. Make the script executable
chmod +x install.sh

# 3. Run the installation
./install.sh
```

The `install.sh` script:
- ✅ Automatically verifies Python
- ✅ Creates installation directory in `~/.local/share/password-generator`
- ✅ Installs the `passgen` command in PATH
- ✅ Creates uninstallation script

#### 🪟 Windows

```batch
# 1. Clone the repository (or download ZIP)
git clone https://github.com/Peppe1604/Simple-Password-Generator-Python.git
cd Simple-Password-Generator-Python

# 2. Run the installer (double click or from prompt)
install.bat
```

The `install.bat` script:
- ✅ Automatically verifies Python
- ✅ Installs in `%LOCALAPPDATA%\PasswordGenerator`
- ✅ Creates Desktop shortcut
- ✅ Option to add to system PATH
- ✅ Creates uninstallation script

### 📝 Manual Installation

If you prefer manual installation:

#### 1. Clone the Repository

```bash
git clone https://github.com/Peppe1604/Simple-Password-Generator-Python.git
cd Simple-Password-Generator-Python
```

#### 2. Verify Python

```bash
python --version
# or
python3 --version
```

Make sure you have Python 3.6 or higher.

#### 3. Run the Program

```bash
python Password_Generator.py
# or
python3 Password_Generator.py
```

## 🚀 Usage

### Quick Start

#### If you installed with scripts:

**Linux/macOS:**
```bash
# Use one of these commands from any directory
passgen
# or
password-generator
```

**Windows:**
- Use the Desktop shortcut "Password Generator"
- Or open command prompt and type: `passgen`

#### If using manual execution:

```bash
# From the project directory
python Password_Generator.py
# or
python3 Password_Generator.py
```

### How to Use the Program

1. **Choose an option from the menu**
   - Type a number from 1 to 5 for options
   - Type 0 to exit

2. **Set the length**
   - Enter a number between 4 and 128

3. **Get your password**
   - View the generated password
   - Check the security evaluation
   - Choose whether to save it

## 🗑️ Uninstallation

### Linux/macOS
```bash
# If you installed with install.sh
~/.local/share/password-generator/uninstall.sh
```

### Windows
```batch
# If you installed with install.bat
# Go to %LOCALAPPDATA%\PasswordGenerator and run:
uninstall.bat

# Or use Control Panel → Programs
```

### Usage Example

```
🔐 MAIN MENU
──────────────────────────────────────────────────
  1. 📝 Letters only password
  2. 🔢 Numbers only PIN
  3. 🔤 Alphanumeric password
  4. 🛡️  Secure password (all characters)
  5. ⚙️  Custom password
  0. 🚪 Exit

👉 Choose an option: 4

📏 Desired length (4-128): 16

⠏ Generating secure password...
✓ Secure password generation completed!

════════════════════════════════════════════════════════════
║                                                          ║
║  ✅ SECURE PASSWORD GENERATED SUCCESSFULLY!             ║
║                                                          ║
════════════════════════════════════════════════════════════

┌────────────────────┐
│  K9@mP#xL2$nQ7&w  │
└────────────────────┘

📊 STATISTICS:
  • Length: 16 characters
  • Generated: 15:42:33

🔒 SECURITY ANALYSIS:
  ✓ Length ≥ 8
  ✓ Length ≥ 12
  ✓ Contains lowercase
  ✓ Contains uppercase
  ✓ Contains numbers
  ✓ Contains symbols

💪 Strength:
  [████████████████████████████████████████] STRONG
```

## 📁 Code Structure

### 📂 Project Files

```
Simple-Password-Generator-Python/
├── Password_Generator.py    # Main script
├── README.md               # Documentation
├── install.sh              # Linux/macOS installer
├── install.bat             # Windows installer
└── passwords_generate.txt  # Output file (created after first save)
```

### 🏗️ Main Code Structure

```
Password_Generator.py
├── Class Colors          # ANSI color definitions
├── Class PasswordGenerator
│   ├── __init__()       # Initialization
│   ├── clear_screen()   # Cross-platform screen clearing
│   ├── print_colored()  # Colored text printing
│   ├── print_box()      # Create decorative boxes
│   ├── print_banner()   # Show ASCII art
│   ├── print_loading()  # Loading animation
│   ├── get_lunghezza()  # Validated length input
│   ├── mostra_menu()    # Main menu
│   ├── genera_password_base()     # Basic generation
│   ├── genera_password_sicura()   # Secure generation
│   ├── genera_password_personalizzata() # Custom
│   ├── mostra_risultato()  # Formatted output
│   ├── valuta_sicurezza()  # Security analysis
│   ├── salva_password()    # Optional saving
│   └── esegui()           # Main loop
└── Main execution
```

## 🔧 Available Options

### 1. Letters Only Password
- Generates passwords containing only letters (uppercase and lowercase)
- Ideal for systems that don't accept special characters

### 2. Numbers Only PIN
- Generates numeric PINs
- Perfect for access codes, credit cards, etc.

### 3. Alphanumeric Password
- Combines letters and numbers
- Good compromise between security and compatibility

### 4. Secure Password
- Includes letters, numbers and special symbols
- Guarantees at least one character of each type
- Maximum security

### 5. Custom Password
- Choose exactly which character types to include
- Complete control over composition

## 🔒 Security

### Evaluation Criteria

The generator evaluates security based on:

| Criterion | Points | Description |
|-----------|--------|-------------|
| Length ≥ 8 | +1 | Recommended minimum |
| Length ≥ 12 | +1 | Optimal length |
| Lowercase letters | +1 | Character variety |
| Uppercase letters | +1 | Greater entropy |
| Numbers | +1 | Additional complexity |
| Special symbols | +1 | Maximum security |

### Security Levels

- **🔴 WEAK** (0-2 points): Not recommended
- **🟡 MEDIUM** (3-4 points): Acceptable for non-critical uses
- **🟢 STRONG** (5-6 points): Recommended for all uses

## ❓ FAQ

### Is the program secure?
Yes! It uses Python's `secrets` module, designed specifically for secure cryptographic generation.

### Where are passwords saved?
In the `passwords_generate.txt` file in the same directory as the program. **Note**: this file is not encrypted!

### How do I install the program?
Use the automatic installation scripts:
- **Linux/macOS**: `./install.sh`
- **Windows**: Double click on `install.bat`

### Can I use it on Windows?
Yes! The program is cross-platform and works on Windows, Linux and macOS. Use `install.bat` for automatic installation on Windows.

### Colors don't work?
Some terminals might not support ANSI colors. The program will still work, just without colors. On Windows 10+ colors should work automatically.

### How do I uninstall the program?
- **Linux/macOS**: Run `~/.local/share/password-generator/uninstall.sh`
- **Windows**: Run `uninstall.bat` from the installation folder

### Do I need to install additional dependencies?
No! The program uses only Python standard libraries. No pip or extra installations needed.

### Can I modify the special characters used?
Yes! Modify the `self.speciali` variable in the `PasswordGenerator` class.

### Are the installation scripts safe?
Yes! The scripts:
- Don't require administrator privileges (unless you want to install globally)
- Don't modify critical system files
- Always create an uninstallation script
- Are completely open source and verifiable

## 🤝 Contributing

Contributions are always welcome! Here's how you can help:

1. **Fork** the project
2. Create a **branch** for your feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. Open a **Pull Request**

### Ideas for Contributions

- [ ] Add multi-language support
- [ ] Implement GUI with tkinter
- [ ] Add clipboard copy functionality
- [ ] Output file encryption
- [ ] Passphrase generator
- [ ] Export in different formats (JSON, CSV)
- [ ] Password manager integration
- [ ] Profile support for password configurations (save settings)
- [ ] Batch mode for generating multiple passwords
- [ ] REST API for integration with other tools
- [ ] Web version of the generator
- [ ] Support for pronounceable passwords
- [ ] Usage statistics and reports

## 👨‍💻 Author

**Giuseppe Maglione**

- GitHub: [@Peppe1604](https://github.com/Peppe1604)
- Email: [giuseppe.maglione@example.com](mailto:giuseppe.maglione@example.com)

## 📄 License

This project is distributed under the MIT license. See the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Made with ❤️ by Giuseppe Maglione
  <br>
  ⭐ If you like this project, leave a star on GitHub! ⭐
</p>
