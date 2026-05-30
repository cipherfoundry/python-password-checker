# Password Checker (Python)

This is a simple Python script that simulates checking login attempts against a secret password.

It shows how to use:

- a **counter** to track how many attempts were checked
- a **flag** (`found_correct`) to remember if the correct password was found
- `break` to **stop the loop early** once the correct password is entered

## How it works

- `secret` stores the correct password (e.g. `"python123"`).
- `attempts` is a list of password attempts.
- The script loops through each attempt:
  - increases `attempt_count` by 1
  - compares the attempt to `secret`
  - if it matches, sets `found_correct = True` and uses `break` to stop
- At the end it prints:
  - whether the correct password was found
  - how many attempts were checked

## Example

For this input:

```python
secret = "python123"
attempts = ["cat", "hello", "python123", "test"]
