- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **GitHub**: https://github.com/ghimiresdp

<h3>[Go to Index](https://github.com/ghimiresdp/python-projects/)</h3><hr>

# SRS: Password Generator

> **Prerequisite**
> - Basic understanding of functions and functional programming
> - Understanding of `modules and packages`
> - Basic understanding of a python [random](https://docs.python.org/3/library/random.html) module


**Table of Contents**

- [SRS: Password Generator](#srs-password-generator)
    - [1. Introduction](#1-introduction)
    - [2. Functional Requirements](#2-functional-requirements)
        - [2.1 Password Generation](#21-password-generation)
        - [2.2 Password Strength](#22-password-strength)
    - [3. Non-functional Requirements](#3-non-functional-requirements)
        - [3.1. User Interface](#31-user-interface)
    - [4. Enhancement](#4-enhancement)
    - [References:](#references)

## 1. Introduction

The Password Generator Application is a software tool designed to generate
random and secure passwords for users. The application aims to provide users
with strong and customizable passwords to enhance their online security.

## 2. Functional Requirements

### 2.1 Password Generation

The Password generator should provide the following functional features for
password generation:

1. specify the length of the password
2. generate password
3. display the generated password

### 2.2 Password Strength

In order to generate strong passwords, you can add the following requirements:

1. Upper case characters
2. Lower case characters
3. numbers
4. special characters

## 3. Non-functional Requirements

### 3.1. User Interface

The application should ask user for the length of password to be generated
and show the password generated from the application.

```
PASSWORD GENERATOR

Enter the number of characters to be displayed: 12

The generated password is:

-----------------------------
|        `Mv6ZgS9Msth       |
-----------------------------
```

## 4. Enhancement

Optionally, you can also check the strength of the generated password
in percentage or show bars for the strength.
Example:

- `Weak   [===      ]`
- `Medium [======   ]`
- `Strong [=========]`

## References:

- **Python Notes:
  ** [chapter 8 Modules and Packages](https://github.com/ghimiresdp/python-notes/blob/main/c08_modules_packages/chapter%208.4%20random.md)
- **Official Documentation**: [Random Module](https://docs.python.org/3/library/random.html)
