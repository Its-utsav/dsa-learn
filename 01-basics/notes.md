# Variables

Got it! Let's dive into some core Python concepts that are essential for becoming proficient in the language:

<!-- ### Basic Concepts
1. **Variables and Data Types**: Understanding and using different data types like integers, floats, strings, lists, tuples, dictionaries, and sets.
2. **Operators**: Arithmetic, relational, logical, bitwise, assignment, and special operators.

### Control Flow
1. **Conditional Statements**: `if`, `elif`, `else` statements for decision-making.
2. **Loops**: `for` and `while` loops, including the use of `break` and `continue` statements.

### Functions
1. **Defining Functions**: Using the `def` keyword, understanding function parameters, and returning values.
2. **Lambda Functions**: Creating small anonymous functions using the `lambda` keyword.
3. **Decorators**: Functions that modify the behaviour of other functions.

### Data Structures
1. **Lists**: Creation, indexing, slicing, appending, and other list methods.
2. **Tuples**: Immutable sequences and their uses.
3. **Dictionaries**: Key-value pairs, dictionary methods, and dictionary comprehensions.
4. **Sets**: Unordered collections of unique elements and set operations.

### String Manipulation
1. **String Methods**: Common string methods like `split()`, `join()`, `replace()`, `find()`, and more.
2. **Formatting Strings**: Using f-strings, `format()` method, and old-style `%` formatting.

### File Handling
1. **Reading and Writing Files**: Using `open()`, `read()`, `write()`, and `with` statement for file operations.

### Exception Handling
1. **Try-Except Blocks**: Catching and handling exceptions using `try`, `except`, `else`, and `finally` blocks.
2. **Custom Exceptions**: Defining your own exceptions using the `raise` keyword.

### Modules and Packages
1. **Importing Modules**: Using `import`, `from ... import ...`, and `import ... as ...` statements.
2. **Creating and Using Packages**: Organizing code into modules and packages.

### Object-Oriented Programming (OOP)
1. **Classes and Objects**: Defining classes, creating objects, and understanding `self`.
2. **Inheritance**: Implementing inheritance, understanding `super()`, and method overriding.
3. **Polymorphism**: Using method overriding and operator overloading.

### Advanced Topics
1. **Generators**: Using `yield` to create generators and understanding their use cases.
2. **Comprehensions**: List, dictionary, and set comprehensions for concise code.
3. **Context Managers**: Using the `with` statement and defining custom context managers.

These concepts will provide you with a strong foundation in Python, enabling you to write efficient, effective, and elegant code. If you need more details or examples on any of these topics, feel free to ask!

 -->

## number

```python
num = 10
floatVal = 3.14
complexVal = 3.14j
```

- `int()`, `float()`, `complex()` for conversion

- Normal arithmetic operation like `+ , - , * , / , % , //`

- float have unlimited precision , store double-precision

- Complex Numbers: Stored as pairs of floating-point numbers, representing the real and imaginary parts.

- math module with more work with number
- random module for random number generation between 0 - 1

## string

- store one or more character inside `" "` or `' '`
- for multiline string we can use `""" """"`

```python
string = "Utsav"
char = "u"
```

- `len()` return the length of object

- `+` for combine multiple string
- `*` for repetition
- `[startVal:endVal]` for slicing

> Python try to reuse same string (if exits in memory) for the similar string
> Python internally check is same string exits and if so , it reuse
