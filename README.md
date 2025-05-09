# Description

This is a small program that retrieves an animated GIF from Giphy, given a text, and saves it to a file.

# Requirements

  - uv package manager (https://docs.astral.sh/uv/)
  - python 3.13 or higher

# Configuration

The program expects `GIPHY_API_KEY` to be present as an environment variable or in a local dotenv file.

# Install dependencies

```
uv sync
```

# Usage

```
uv run main.py <text query>
```
For complete usage instructions:
```
uv run main.py --help
```

# Integration testing

Warning: this actually calls the live API
```
uv run pytest
```

# Directory structure

  - `/giphy/` The GIPHY adapter
  - `/tests/` Integration tests
  - `/main.py` The main file
