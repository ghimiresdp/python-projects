- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **GitHub**: https://github.com/ghimiresdp

<h3>[Go to Index](https://github.com/ghimiresdp/python-projects/)</h3><hr>

# SRS: A Console-based Contact Book

**Table of Contents**


> This project aims programmer to create a basic contact book that is capable
> of adding, editing, viewing and listing contacts in the terminal.

**Prerequisites**
- Basic understanding of an object-oriented programming
- Knowledge on file and exception handling
- knowledge on either json or csv library


## Instructions

1. create a class for a contact that should be able to store name, email, and
   phone number
2. create a class for a contact book, that should be able to store multiple
   contacts and display in 2 different views:
   - List View
   - Table View
4. add methods `add_contact`, `view_contacts` and `display_table` to the class
   `ContactBook`
5. add relevant attributes and methods if required

## List View

A List view should facilitate user to view contacts in a list with pagination
that should support 3 users per view.

**Example:**
```
+------------------------------------------------+
|  🙍 JOHN DOE                                   |
|  📧 johndoe@example.com                        |
|  📞 +1234567890123                             |
+------------------------------------------------+
+------------------------------------------------+
|  🙍 JANE DOE                                   |
|  📧 janedoe@example.com                        |
|  📞 +1234567890124                             |
+------------------------------------------------+
+------------------------------------------------+
|  🙍 JOHN JANE                                  |
|  📧 johnjane@example.com                       |
|  📞 +1234567890125                             |
+------------------------------------------------+

    << Prev [P]      Exit[E]        Next [N]>>
```

## Table View
A Table view should facilitate user to view contacts in a table that should show
all contacts.

**Example:**
```
SN  |  Name                 |  Email                   |  Phone
----+-----------------------+--------------------------+------------------------
1   |  John Doe             |  johndoe@example.com     |  +1234567890123
2   |  Jane Doe             |  janedoe@example.com     |  +1234567890123
3   |  John Jane            |  johnjane@example.com    |  +1234567890123

```
