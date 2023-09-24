# Math Interpreter
A program to calculate the result of mathematical expressions.\
Also, this program works with complex numbers, concepts related to infinity, as well as ambiguous expressions.\
In terms of grammar, the input statements are similar to Python grammar, such as:
2 ** 2, 2 * 2, (-1) ** 0.5, (1.2+3.4j) * 10 etc.

# Installation & Usage
1. Clone the repo:
    ```bash
    git clone https://github.com/ogel4s/Math_Interpreter.git
    ```

2. cd to Math_Interpreter folder

3. Run **`evaluator.py`**:
    ```bash
    python evaluator.py
    ```

You can also use it as CLI:
```bash
python evaluator.py (-1) ** 0.5
```

# Operators
The symbols of the operators used in the program are as follows:

| Operators        | Symbol           |
| ------------- |:-------------:|
| *Power*      | **`^`** or **`**`** |
| *Multiplication*      | **`*`**      |
| *Division* | **`/`**      |
| *Sum* | **`+`**      |
| *Subtraction* | **`-`**      |


numbers:

| Number         | from          |
| ---------------| :------------:|
| *Complex number* | **`(real+kj)`**|
| *Infinity number*| **`inf`** or **`-inf`**|

# Example
An input item:
```
1 + ( 2 ** 0.5 * (1/2/3/((((-1)))) ** (((0.5))*10)+12.39347) ) * 2 / (-2) ** 0.5 + inf
```
 

🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹
