# Python Code Obfuscator
A powerful Python code obfuscation tool that provides multiple layers of protection for your source code through variable renaming, string encoding, and Base64 wrapping techniques.
" -----------------------------------------------------------------------
# Features
- Multi-layer Base64 Encoding: Wrap your code in multiple layers of Base64 encoding for enhanced protection
- Variable Name Randomization: Automatically rename local variables and function names to random strings
- String Obfuscation: Encode string literals using Base64 with runtime decoding
- AST-based Processing: Uses Python's Abstract Syntax Tree for precise code transformation
- Command-line Interface: Easy-to-use CLI for batch processing
- Configurable Layers: Customize the number of obfuscation layers
" -----------------------------------------------------------------------
# Requirements & Installation
- Python 3.7+
- `astor` library for AST to source code conversion

1. Clone or download this repository
2. Install the required dependency
3. pip install astor

        # Dependencies
            - `ast`: Python's built-in Abstract Syntax Tree module
            - `base64`: Standard library for Base64 encoding/decoding
            - `random`: For generating random variable names
            - `string`: String manipulation utilities
            - `pathlib`: Modern file path handling
            - `astor`: Third-party library for AST to source conversion
" -----------------------------------------------------------------------
# Project Structure
```
Code Obfuscator/
├── Obfuscator.py          # Main obfuscation engine
├── README.md             # This file
└── readme.md            # Legacy readme (if exists)
```
" -----------------------------------------------------------------------
# Command Line Interface Usage
```bash
python Obfuscator.py input_file.py output_file.py [options]
``` 
     # Options:
    - `-l, --layers`: Number of Base64 obfuscation layers (default: 3)
    - `-h, --help`: Show help message

        # Examples:
            ```bash
            # Basic obfuscation with default 3 layers
            python Obfuscator.py script.py obfuscated_script.py
            # Custom number of layers
            python Obfuscator.py script.py obfuscated_script.py -l 5
            # Maximum obfuscation
            python Obfuscator.py script.py obfuscated_script.py -l 10
            ```
" -----------------------------------------------------------------------
# Programmatic Usage
```python
from Obfuscator import extreme_obfuscate, obfuscate_file

# Obfuscate code string
source_code = """
def hello_world():
    print("Hello, World!")
    return "success"
"""
obfuscated = extreme_obfuscate(source_code, layers=3)
print(obfuscated)

# Obfuscate file directly
obfuscate_file("input.py", "output.py", layers=3)
```
" -----------------------------------------------------------------------
# How It Works
The obfuscator employs a three-stage process:
1. **Variable Renaming**: Uses AST parsing to identify and rename local variables and function names to random strings
2. **String Encoding**: Converts all string literals to Base64-encoded values with runtime decoding
3. **Multi-layer Wrapping**: Wraps the entire obfuscated code in multiple layers of Base64 encoding

    Original Code → AST Parsing → Variable Renaming → String Encoding → Multi-layer Base64 → Output
" -----------------------------------------------------------------------
# Limitations
- **Complex Code**: May not handle all Python language features
- **Debugging Difficulty**: Obfuscated code is extremely difficult to debug
- **Reverse Engineering**: Determined attackers can still reverse engineer the code
- **Dependencies**: Requires `astor` library which may not be available in all environments

        # Performance Considerations
        - Obfuscation time increases with the number of layers
        - Runtime performance is affected by the decoding overhead
        - Memory usage increases due to multiple encoding layers
        - Consider the trade-off between protection level and performance
" -----------------------------------------------------------------------
# Security & Legal Disclaimer
This tool is intended for legitimate use cases such as intellectual property protection and educational purposes. Users are responsible for ensuring compliance with applicable laws and regulations.

v. While it makes code harder to read and understand, it does not provide cryptographic security.

** This project is open source. **

