- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **GitHub**: https://github.com/ghimiresdp

<h3>[Go to Index](https://github.com/ghimiresdp/python-projects/)</h3><hr>

# SRS: To Do List

> **Prerequisite**
> - Understanding of Basic data types as well as complex data types
> - Basic understanding of functional and Object-oriented programming
> - Understanding of `modules and packages`
> - Understanding of a `json` module.
> - Understanding of `Files and I/O`
> - Understanding of Exception handling.

**Table of Contents**

- [SRS: To Do List](#srs-to-do-list)
    - [1. Introduction](#1-introduction)
    - [2. Functional Requirements](#2-functional-requirements)
        - [2.1 Task Management](#21-task-management)
        - [2.2 Task Storage](#22-task-storage)
        - [2.3 BONUS: Task sorting and filtering](#23-bonus-task-sorting-and-filtering)
    - [3. Non Functional Requirements](#3-non-functional-requirements)
        - [3.1. User Interface](#31-user-interface)
        - [Example Screens](#example-screens)
    - [References:](#references)

## 1. Introduction

The To-Do List Application is a software tool designed to help users manage
their tasks and stay organized. The application allows users to create, update,
and track their to-do items, ensuring efficient task management and improved
productivity.

## 2. Functional Requirements

### 2.1 Task Management

The application should provide the following features for task management.

1. **add a task**: ask user to input title, description and deadline
2. **list tasks**: list all tasks by title, status, and deadline
    - filter by `open` status
    - filter by `completed` status
3. **view detail of the task**
4. **complete the task**
5. **view completed tasks**

### 2.2 Task Storage

The task can be stored in a json file with different key-value pairs. The basic
format to store to-do list is as follows:

```json
[
    {
        "title": "Buy 5 drinks",
        "description": "Buy 5 250 ml soda cans from Family Mart.",
        "date": "2023-01-01",
        "completed": true
    },
    {
        "title": "Complete the assignment",
        "description": "Complete Chemistry assignment and send email to the professor",
        "date": "2023-01-05",
        "completed": false
    }
]
```

### 2.3 BONUS: Task sorting and filtering

You can also add the interface to allow users to sort and filter tasks with
respect to `title`, `date`, and `completed` status

## 3. Non Functional Requirements

### 3.1. User Interface

The application should have a basic CLI that should prompt user to list, add,
update, and complete the task. you can emulate completed and incomplete item by
adding `[ ]` and `[x]` before the title of the task.

### Example Screens

**Welcome Screen:**

```
TO DO LIST
-------------------------------------------------------

1. list tasks
2. add a new task

3. save and exit
4. exit without saving
-------------------------------------------------------
Enter a number:

```

**List Screen:**

```
TO DO LIST
-------------------------------------------------------
1. [x]  Buy 5 drinks                        2023-01-01
-------------------------------------------------------
2. [ ]  Complete the assignment             2023-01-05
-------------------------------------------------------
Enter Number to view details [0 to go back]:
```

**Detail Screen**

```
-------------------------------------------------------
BUY 5 DRINKS
-------------------------------------------------------
DESCRIPTION : Buy 5 250 ml soda cans from Family Mart.
DEADLINE    : 2023-01-01

STATUS      : INCOMPLETE
-------------------------------------------------------
Options:

1. Complete the task
2. Go Back

Enter option:
```

## References:

- **Python Notes**: <https://github.com/ghimiresdp/python-notes/>
    - Chapter 2, 3, 6, 7, 8, 9, 10
