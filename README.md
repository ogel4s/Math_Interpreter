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


# Operators & Functions
The symbols of the operators used in the program are as follows:

| Operators | Symbol |
| ------------- |:-------------:|
| *Power* | **`^`** or **`**`** |
| *Multiplication* | **`*`** |
| *Division* | **`/`** |
| *Sum* | **`+`** |
| *Subtraction* | **`-`** |
||


You can also use trigonometric functions and inverse trigonometric functions:

*Note: Functions are not case sensitive .*

*Note: The default trigonometric calculation mode is **`deg`**, if you want to change it to rad, enter the **`config.ini`** file and change the mode value to **`rad`** .*

| Functions |
|:---------:|
| **`sin, cos, tan, cot, csc, sec`** |
| **`arcsin, arccos, arctan, arccot, arccsc, arcsec`** |
| **`sinh, cosh, tanh, coth, csch, sech`** |
| **`arcsinh, arccosh, arctanh, arccoth, arccsch, arcsech`** |
|**`pi or PI (number)`**|

example:
```
2 * 2 + pi / pi ** (-0.5 - (-1) ** 0.5) ** sin(cos(tan(arcsinh(sinh(10 ** (sin((-1) ** 0.5) - 1)) / 2))) / (1.2+3.4j)) - sin((1.2+3.4j)) / cos((((-1))) ** (((0.5)))) + 221 * PI - (PI+pij)
```

numbers:

| Number         | from          |
| ---------------| :------------:|
| *Complex number* | **`(real+kj)`**|
| *Infinity number*| **`inf`** or **`-inf`**|

# Example
An input item:
```
1 + ( 2 ** 0.5 * (1/2/3/((((-1)))) ** (((0.5))*10)+12.39347) ) * 2 / (-2) ** 0.5 + inf + 2 * 2 + pi / pi ** (-0.5 - (-1) ** 0.5) ** sin(cos(tan(arcsinh(sinh(10 ** (sin((-1) ** 0.5) - 1)) / 2))) / (1.2+3.4j)) - sin((1.2+3.4j)) / cos((((-1))) ** (((0.5)))) + 221 * PI - (PI+pij)
```
 

**Enjoy...**

🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹
