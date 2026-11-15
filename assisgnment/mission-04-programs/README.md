# Mission 4: How programs run

## Task 4.1: Create and run a Python program

File: [hello.py](hello.py)

```python
print("Hello from Python")
```

Command used (from inside this folder):

```
python3 hello.py
```

Output:

```
Hello from Python
```

Result: the message appeared in the Terminal, so the program works.

## Task 4.2: Compare compiler and interpreter

| Point | Compiler | Interpreter |
|---|---|---|
| When translation / execution happens | The whole program is translated into machine code first, before it runs | The program is read and run line by line while it is running |
| Typical output | A separate executable file (like `a.out` or `app.exe`) that can run on its own | No separate file; the output of the program appears straight away |
| One example | C / C++ (gcc), Go, Rust | Python, JavaScript (in the browser), Bash |
| One advantage | The finished program runs very fast because it is already in machine code | Easy to test and fix quickly because there is no separate build step |

**Explanation:** A compiler translates the whole source code into machine code before the program runs, and gives a separate file that can be run again and again without translating again, so it is fast (like C). An interpreter reads the code and carries it out line by line while the program is running, so I can run `python3 hello.py` straight away without building anything. Compiled programs usually run faster, but interpreted programs are quicker to write and test. Python actually uses both ideas: it first turns the code into bytecode and then its interpreter runs that bytecode.

## Tools and commands used

VS Code (to write hello.py), Terminal, Python 3. Commands: `python3 hello.py`, `python3 --version`.

## What I understood

Computers only understand machine code, so the code we write must be translated. A compiler does this all at once before running, and an interpreter does it while running. Python is run by an interpreter, which is why I can run my file directly with `python3`.

## Difficulty faced

No difficulty. I only had to make sure I was inside the mission folder before running `python3 hello.py`.
