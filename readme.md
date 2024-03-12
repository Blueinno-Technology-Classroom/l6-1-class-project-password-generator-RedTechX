# 404B Lesson 6 Class Project - Password Generator

## Explore the `string` module

```python
import string

print(string.digits)
# 0123456789

print(string.ascii_letters)
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

print(string.punctuation)
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


print(string.printable)
# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

```

## Picking a random item from a sequence

```python
import string
import random

item = random.choice(string.digits)
print(item)
```

## Your Task

Write a password generator program accepts a number input from user, then return a password with the length of that number.

You may follow the steps below:

1. Create a variable, `pw`, as an empty *str* or *list*.
2. Create a variable, `pw_len`, which will be the length of the password from user input.
3. Convert `pw_len` from *str* to *int*.
4. Import modules: `random` & `string`.
5. Create a loop that will cycle `pw_len` times.
6. In each cycle, append a random character from `string.printable` to `pw`.
7. Print the `pw` in console window.

## Sample Input

`password length: 15 ⏎`

## Sample Output

`_y8kRh>:;i8e?)T`

## Submitting Your Work

1. Make sure the assignment repository is opened in VS Code.

2. Make sure you have completed all the tasks.

3. (First time only)
Use Command + J to open the Terminal tab and config your git username and email:

    ```bash
    git config user.name "Your Name"
    git config user.email "Your GitHub Email"
    ```

4. Click on the "Source Control" icon on the left. Source Control

    ![1](https://github.com/BlueinnoClassroom/404B-L2.1-Template/assets/155412668/2c31026e-c14d-484f-bb9e-dc87189a0216)

5. Enter a commit message and click on the "Commit" button.

6. Click on the "Sync Changes" button.
