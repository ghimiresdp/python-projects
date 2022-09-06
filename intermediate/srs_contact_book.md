# Project: A Contact Book

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
   - Detail View


## List View

A List view should facilitate user to view contacts in a list with pagination
that should support 3 users per view.

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
