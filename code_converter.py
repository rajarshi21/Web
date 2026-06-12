"""
main.py - Example usage of ollama chat and simple list addition
This code helps to convert a code snippet to python
This can be enhanced further
"""

from ollama import chat

code = (
    "using System;\n"
    "namespace HelloWorld\n"
    "{\n"
    "    class Program\n"
    "    {\n"
    "        static void Main(string[] args)\n"
    "        {\n"
    "            Console.WriteLine(\"Hello, World!\");\n"
    "        }\n"
    "    }\n"
    "}\n"
)

import sys
from pathlib import Path

def load_code_from_file(path: Path) -> str:
    return path.read_text(encoding='utf-8')

source_file = Path(sys.argv[1]) if len(sys.argv) > 1 else None
if source_file and source_file.exists():
    code = load_code_from_file(source_file)
else:
    if source_file:
        print(f'Warning: source file {source_file} not found, using built-in sample code.')
    source_file = None

what_to_ask = f'Convert the below c# code to python: {code}'

response = chat(
    model='nemotron-3-super:cloud',
    messages=[{'role': 'user', 'content': what_to_ask}],
)
print(response.message.content)
