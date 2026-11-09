import re

print("================================")
print("     PASSWORD STRENGTH CHECKER")
print("================================")

password = input("Enter your password: ")

score = 0

if len(password) >= 8:
    score += 1

if re.search(r"[A-Z]", password):
    score += 1

if re.search(r"[a-z]", password):
    score += 1

if re.search(r"[0-9]", password):
    score += 1

if re.search(r"[^A-Za-z0-9]", password):
    score += 1

if score == 1:
    strength = "Very Weak"
elif score == 2:
    strength = "Weak"
elif score == 3:
    strength = "Moderate"
elif score == 4:
    strength = "Strong"
else:
    strength = "Very Strong"

print("\nPassword Strength:", strength)
print("Score:", score, "/ 5")