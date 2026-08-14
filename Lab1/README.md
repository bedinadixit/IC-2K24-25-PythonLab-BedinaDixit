# Python Lab 1

## 1. Variable and Identifier Practice

### Aim

To declare variables for name, age, height, and student status and display each variable along with its data type.

### Logic

The program creates variables of different data types: string, integer, float, and Boolean.
The `type()` function is used to check and display the data type of each variable.

### Sample Input / Output

No input is required.

**Sample Output:**

```text
Name: Bedina Type: <class 'str'>
Age: 20 Type: <class 'int'>
Height: 5.4 Type: <class 'float'>
Student: True Type: <class 'bool'>
```

---

## 2. Greeting Program

### Aim

To take the user's name, age, and city as input and display them in one sentence using an f-string.

### Logic

The program takes the user's name, age, and city using `input()`.
It combines all three values into one sentence using an f-string.

### Sample Input / Output

**Sample Input:**

```text
Enter your name: Bedina Dixit
Enter your age: 20
Enter your city: Indore
```

**Sample Output:**

```text
Hello Bedina Dixit, you are 20 years old and you live in Indore.
```

---

## 3. Arithmetic Operations

### Aim

To perform basic arithmetic operations on two numbers.

### Logic

The program takes two numbers as input and performs addition, subtraction, multiplication, division, and modulus operations.
Each result is displayed with a clear label.

### Sample Input / Output

**Sample Input:**

```text
Enter first number: 29
Enter second number: 78
```

**Sample Output:**

```text
Sum: 107.0
Difference: -49.0
Product: 2262.0
Quotient: 0.3717948717948718
Remainder: 29.0
```

---

## 4. Celsius to Fahrenheit

### Aim

To convert temperature from Celsius to Fahrenheit.

### Logic

The program takes the temperature in Celsius as input and converts it into a number.
It applies the formula `F = (C × 9/5) + 32` and displays the Fahrenheit value.

### Sample Input / Output

**Sample Input:**

```text
Enter temperature in Celsius: 56
```

**Sample Output:**

```text
Temperature in Fahrenheit: 132.8
```

---

## 5. String Manipulation

### Aim

To perform different string operations on a full name.

### Logic

The program takes a full name as input and converts it into uppercase and lowercase forms.
It also reverses the string, calculates its length, and uses different string methods such as `upper()`, `lower()`, `title()`, and `capitalize()`.

### Sample Input / Output

**Sample Input:**

```text
Enter your full name: Bedina Dixit
```

**Sample Output:**

```text
Uppercase: BEDINA DIXIT
Lowercase: bedina dixit
Reversed: tixiD anideB
Length: 12
Title Case: Bedina Dixit
Capitalized: Bedina dixit
```

---

## 6. Escape Sequence Practice

### Aim

To print a simple table using the `\t` and `\n` escape sequences.

### Logic

The program uses `\t` to create spacing between the item name and price.
It uses `\n` to move the output to a new line.

### Sample Input / Output

No input is required.

**Sample Output:**

```text
Item    Price
Pen     20
Notebook        50
Pencil  10
```
