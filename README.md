# 💱 nprxchange

**nprxchange** is a modern and easy-to-use command-line tool that converts Nepali Rupees (NPR) to other major currencies using the official exchange rates published by the Nepal Rastra Bank (NRB).

It supports both interactive and non-interactive (direct CLI arguments) modes, with beautiful terminal output powered by [Rich](https://github.com/Textualize/rich).

---

## 📌 Features

- 🏦 Uses **official NRB exchange rates**
- 🌐 Works **online and offline** (uses cache if offline)
- 🎨 Clean and stylish CLI output using `rich`
- 📋 View available currencies and their codes
- 💬 Interactive currency selection using `InquirerPy`
- 🔁 Refresh latest exchange rates manually

---

## 🛠️ Installation

### 📦 Install via `pip`:
```bash
pip install nprxchange
```
### 🧪 Usage Examples:
```bash
# Show help
nprxchange --help

# View all supported currencies
nprxchange -v

# Convert 1000 NPR to USD directly
nprxchange -c 1000 -t USD

# Convert 5000 NPR to EUR with full command
nprxchange --convert 5000 --to-currency EUR

# Refresh latest exchange rates
nprxchange -r

# Launch interactive mode
nprxchange -i
```

### 🔍 Command Line Arguments

| Argument | Short | Description |
|----------|-------|-------------|
| `--view-currencies` | `-v` | View all available currencies with their codes |
| `--convert AMOUNT` | `-c AMOUNT` | Amount in NPR to convert to foreign currency |
| `--to-currency CODE` | `-t CODE` | Target currency code (e.g., USD, EUR, INR) |
| `--refresh` | `-r` | Force refresh rates from the NRB API |
| `--interactive` | `-i` | Launch interactive mode to select currency |

## 🧑‍💻 Contributing
Contributions are welcome! To contribute:
- Fork this repository
- Create your feature branch (git checkout -b feature-name)
- Commit your changes (git commit -m 'Add feature')
- Push to the branch (git push origin feature-name)
- Open a pull request

Please follow clean code practices and test your changes before submitting.

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 👤 Author
Name: Munal Poudel

Email: munalpoudel3@gmail.com

GitHub: github.com/munal777

