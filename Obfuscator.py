# Import all primary tools for the source code (Parsing code, Encoding Strings, randomizer, and the abilityl to read/write).
import ast
import base64
import random
import string
from pathlib import Path

# Used to all functions in the code
def random_name(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

# Wraps code in a Base64 string encoding (Exec statement).
def obfuscate_code_layer(code, layer=1):
    encoded = base64.b64encode(code.encode()).decode()
    return f"exec(base64.b64decode('{encoded}').decode())"

# Main Randomizer.
def rename_locals(tree):
    class Renamer(ast.NodeTransformer):
        def visit_FunctionDef(self, node):
            node.name = random_name()  
            self.generic_visit(node)
            return node
        
        def visit_Name(self, node):
            if isinstance(node.ctx, (ast.Store, ast.Load)):
                node.id = random_name()
                return node
    return Renamer().visit(tree)

# Randomize all string literals in a Base64, then partnered with a "helper" function to decode at runtime. 
def string_obfuscator(tree):
    class str0bf(ast.NodeTransformer):
        def visit_Constant(self, node):
            if isinstance(node.value, str) and node.value:
                encoded = base64.b64encode(node.value.encode()).decode()
                return ast.Call(func=ast.Name(id="__s", ctx=ast.Load()), args=[ast.Constant(value=encoded)], keywords=[])
            return node
    return str0bf().visit(tree)

# Whenever a string is used it calls the function to decode it "asap".
HELPER = """
import base64
def __s(x): return base64.b64decode(x.encode()).decode()
"""

# Used to parse the source code, rename variables, obfuscate strings, and wrap the entire code/project in multiple layers of Base64.
def extreme_obfuscate(source, layers=3):
    tree = ast.parse(source)
    tree = rename_locals(tree)
    tree = string_obfuscator(tree)
    
    import astor
    code = HELPER + "\n" + astor.to_source(tree)
    for _ in range(layers):
        code = obfuscate_code_layer(code)
    return code

# Applies maximum obfuscation then rewrite the output into a seperate and new file.
def obfuscate_file(input_file, output_file, layers=3):
    src = Path(input_file).read_text()
    obf = extreme_obfuscate(src, layers)
    Path(output_file).write_text (obf)
    print(f"[+] Written extreme obfuscated code to {output_file}")

# Commandline interface, making the program universal compatibility to all potential python files.
if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="Extreme multi-layer Python obfuscator")
    ap.add_argument("input", help="Input Python file")
    ap.add_argument("output", help="Output obfuscated file")
    ap.add_argument("-l", "--layers", type=int, default=3, help="Number of Base64 layers")
    args = ap.parse_args()
    obfuscate_file(args.input, args.output, args.layers)

# Additional security measures.
import os
import sys
from pathlib import Path

# Add input validation.
def validate_file_path(file_path):
    path = Path(file_path).resolve()
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    if not path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")
    return path

# Add file size limits.
MAX_FILE_SIZE = 10 * 1024 * 1024 
def check_file_size(file_path):
    size = os.path.getsize(file_path)
    if size > MAX_FILE_SIZE:
        raise ValueError(f"File too large: {size} bytes (max: {MAX_FILE_SIZE})")
    return size