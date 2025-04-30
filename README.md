# 💱 nprxchange - Nepal Rastra Bank Currency Converter CLI

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

🧑‍💻 Contributing
Contributions are welcome! To contribute:

Fork this repository

Create your feature branch (git checkout -b feature-name)

Commit your changes (git commit -m 'Add feature')

Push to the branch (git push origin feature-name)

Open a pull request

Please follow clean code practices and test your changes before submitting.

👤 Author
Name: Munal Poudel

Email: munalpoudel3@gmail.com

GitHub: github.com/munal777

# NPRXchange

[![PyPI version](https://img.shields.io/pypi/v/nprxchange.svg)](https://pypi.org/project/nprxchange/)
[![Python Versions](https://img.shields.io/pypi/pyversions/nprxchange.svg)](https://pypi.org/project/nprxchange/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A command-line tool for converting Nepalese Rupees (NPR) to foreign currencies using official Nepal Rastra Bank exchange rates.

## Features

- Get up-to-date exchange rates from Nepal Rastra Bank
- Convert NPR to any available foreign currency
- View all available currencies with their codes
- Interactive currency selection menu
- Fallback to cached data when offline
- Beautiful terminal output with rich formatting

## Installation

```bash
pip install nprxchange
```

## Usage

```bash
# View all available currencies
nprxchange --view-currencies

# Convert amount in NPR to another currency
nprxchange --convert 1000 --to-currency USD

# Force refresh rates from NRB API
nprxchange --refresh

# Launch interactive mode to select currency and view rates
nprxchange --interactive
```

### Command Line Arguments

| Argument | Short | Description |
|----------|-------|-------------|
| `--view-currencies` | `-v` | View all available currencies with their codes |
| `--convert AMOUNT` | `-c AMOUNT` | Amount in NPR to convert to foreign currency |
| `--to-currency CODE` | `-t CODE` | Target currency code (e.g., USD, EUR, INR) |
| `--refresh` | `-r` | Force refresh rates from the NRB API |
| `--interactive` | `-i` | Launch interactive mode to select currency |

## Development

To contribute to this project:

```bash
# Clone the repository
git clone https://github.com/yourusername/nprxchange.git
cd nprxchange

# Install in development mode
pip install -e .
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Munal Poudel (munalpoudel3@gmail.com)

