- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **GitHub**: https://github.com/ghimiresdp

<h3>[Go to Index](https://github.com/ghimiresdp/python-projects/)</h3><hr>

# SRS: Weight Converter Application

> **Prerequisite**
> - Basic understanding of functions and functional programming
> - Basic data types and operation
> - Understanding how python takes input and prints text
> - String formatting and manipulation

**Table of Contents**

- [SRS: Weight Converter Application](#srs-weight-converter-application)
    - [1. Introduction](#1-introduction)
    - [2. Functional Requirements](#2-functional-requirements)
        - [2.1. Conversion Types](#21-conversion-types)
        - [2.2. User Input](#22-user-input)
        - [2.3. Conversion Calculation](#23-conversion-calculation)
        - [2.4. Output Display](#24-output-display)
    - [3. Non-functional Requirements](#3-non-functional-requirements)
        - [3.1 User Interface](#31-user-interface)
        - [3.2 Accuracy](#32-accuracy)
    - [4. Enhancement](#4-enhancement)

## 1. Introduction

The Weight Converter Application is a console-based software designed to convert
weights between different units of measurement. The application provides a
user-friendly interface that allows users to input a weight value in one unit
and convert it to another unit of their choice. The goal is to provide a
convenient tool for quick and accurate weight conversions.

## 2. Functional Requirements

### 2.1. Conversion Types

The Weight Converter Application should support the following weight conversion
types:

- Kilograms (kg) to Pounds (lbs)
- Pounds (lbs) to Kilograms (kg)
- Kilograms (kg) to Ounces (oz)
- Ounces (oz) to Kilograms (kg)

### 2.2. User Input

The application should prompt the user to input the weight value and the desired
conversion type. The user should be able to enter the weight value as a decimal
number.

**Example:**

```
==================================================
Unit Conversion Application
--------------------------------------------------
1. Kilograms (kg) to Pounds (lbs)
2. Pounds (lbs) to Kilograms (kg)
3. Kilograms (kg) to Ounces (oz)
4. Ounces (oz) to Kilograms (kg)

5. Exit
==================================================

Please Select the option:
```

### 2.3. Conversion Calculation

The application should accurately convert the weight value from the input unit
to the desired output unit using the appropriate conversion formula for each
conversion type.

### 2.4. Output Display

The application should display the converted weight value along with the
original and target units to provide clear and understandable output to the
user.
**Example:**

```
...
==================================================

Please Select the option:  1

--------------------------------------------------
Converting Kilogram to Pounds
--------------------------------------------------

Please Enter Weight in Kilograms: 5

==================================================
5 Kgs is equal to 11.02 Pounds
==================================================
```

## 3. Non-functional Requirements

### 3.1 User Interface

The console-based user interface should be simple, intuitive, and easy to
navigate. Clear instructions and prompts should be provided to guide the user
through the conversion process.

### 3.2 Accuracy

The weight conversion calculations should be accurate, ensuring precision up to
at least two decimal places.

## 4. Enhancement

You can add Enhancement to the application by re-prompting whether we want to
convert another number or not.

**Example: selecting option `yes`**

```
...
==================================================
5 Kgs is equal to 11.02 Pounds
==================================================

Do you want to convert again? [y/n]: y
--------------------------------------------------

Please Enter Weight in Kilograms:

```

**Example: selecting option `no`**

```
...
==================================================
5 Kgs is equal to 11.02 Pounds
==================================================

Do you want to convert again? [y/n]: n
--------------------------------------------------

1. Kilograms (kg) to Pounds (lbs)
2. Pounds (lbs) to Kilograms (kg)
3. Kilograms (kg) to Ounces (oz)
4. Ounces (oz) to Kilograms (kg)

5. Exit
==================================================

Please Select the option:

```
