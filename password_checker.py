secret = "python123"
attempts = ["cat", "hello", "python123", "test"]

found_correct = False
attempt_count = 0

for attempt in attempts:
    attempt_count = attempt_count + 1

    if attempt == secret:
        found_correct = True
        break

print("Found correct password:", found_correct)
print("Attempts checked", attempt_count)
