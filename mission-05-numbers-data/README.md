# Mission 5 — Numbers and data

## 1. Task / objective

Convert decimal, binary and hexadecimal values by hand, verify them with Python, build a small converter and explain text encoding.

## 2. Work completed

### Task 5.1: Convert numbers by hand

| Question | My working and answer |
|---|---|
| Convert decimal 13 to binary | 13 ÷ 2 = 6 r **1**, 6 ÷ 2 = 3 r **0**, 3 ÷ 2 = 1 r **1**, 1 ÷ 2 = 0 r **1**. Read remainders bottom to top → **1101** |
| Convert decimal 25 to binary | 25 ÷ 2 = 12 r **1**, 12 ÷ 2 = 6 r **0**, 6 ÷ 2 = 3 r **0**, 3 ÷ 2 = 1 r **1**, 1 ÷ 2 = 0 r **1**. Bottom to top → **11001** |
| Convert binary 1010 to decimal | (1×8) + (0×4) + (1×2) + (0×1) = 8 + 0 + 2 + 0 = **10** |
| Convert binary 1101 to decimal | (1×8) + (1×4) + (0×2) + (1×1) = 8 + 4 + 0 + 1 = **13** |
| Convert hexadecimal A to decimal | A stands for 10, so A = **10** |
| Convert hexadecimal 1F to decimal | (1×16) + (F×1) = 16 + 15 = **31** |
| Convert binary 1111 to hexadecimal | 1111 = 8 + 4 + 2 + 1 = 15, and 15 in hex is **F** |

### Task 5.2: Verify using Python

Opened the Python interactive environment with `python3` and typed:

| Expression I tested | Result | Matches my manual answer? |
|---|---|---|
| `bin(13)` | `'0b1101'` | Yes |
| `bin(25)` | `'0b11001'` | Yes |
| `int('1010', 2)` | `10` | Yes |
| `int('1101', 2)` | `13` | Yes |
| `int('A', 16)` | `10` | Yes |
| `int('1F', 16)` | `31` | Yes |
| `hex(int('1111', 2))` | `'0xf'` | Yes |

Note: Python adds `0b` in front of binary and `0x` in front of hex to show which number system it is.

### Task 5.3: Build a small number converter

File: [number_converter.py](number_converter.py)

Run with: `python3 number_converter.py`

| Test number | Binary output | Hexadecimal output |
|---|---|---|
| 13 | 1101 | D |
| 25 | 11001 | 19 |
| 255 | 11111111 | FF |
| 1000 | 1111101000 | 3E8 |

How it works:
- `input()` asks the user to type a number. It comes in as text.
- `int()` changes the text into a whole number.
- `bin()` converts the number to binary, like `'0b1101'`. I used `[2:]` to remove the `0b`.
- `hex()` converts the number to hexadecimal, like `'0xff'`. I removed the `0x` with `[2:]` and used `.upper()` to get capital letters.

### Task 5.4: How is text stored?

- ASCII decimal code for uppercase **A** = **65**, lowercase **a** = **97** (checked with `ord('A')` and `ord('a')` in Python).
- A computer can only store numbers (bits), so it needs an encoding standard that gives every character a fixed number. That way the same text looks the same when it is opened on another computer.
- A character that is not part of basic ASCII: **₹** (Indian Rupee sign), or an emoji like 😀. UTF-8 can store these.

## 3. Commands / tools used

Terminal, Python 3 interactive mode, VS Code. Commands/functions: `python3`, `bin()`, `hex()`, `int()`, `ord()`, `input()`, `python3 number_converter.py`.

## 4. My understanding

Decimal is base 10, binary is base 2 and hexadecimal is base 16. To go from decimal to binary I divide by 2 and read the remainders backwards, and to go back I multiply each digit by its place value. Hex is a short way of writing binary because one hex digit = 4 bits. Text is also stored as numbers using ASCII or UTF-8.

## 5. Difficulties faced

Remembering to read the remainders from bottom to top when converting to binary. Also Python's `0b` and `0x` prefixes confused me at first.

## 6. How I resolved them

I wrote down every division step and its remainder in a column, then read it from the bottom. For the prefixes, I learned `0b` means binary and `0x` means hex, and removed them with `[2:]`.

## 7. Evidence / files

- [number_converter.py](number_converter.py) — the decimal to binary/hexadecimal converter
- `README.md` (this file) with manual working, Python checks, test results and encoding notes.

## 8. Commit details

Commit message: `Build number converter and practise data representation` — pushed to GitHub.
