import tkinter as tk
import re

# Create the main window
root = tk.Tk()
root.title("Password Security Analyzer")
root.geometry("450x500")
root.resizable(False, False)
root.configure(bg="#101820")


# Check password strength
def check_password():

    password = password_entry.get()

    if not password:
        result_label.config(
            text="Please enter a password!",
            fg="orange"
        )
        recommendation_label.config(text="")
        return

    score = 0
    recommendations = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        recommendations.append("Use at least 8 characters.")

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        recommendations.append("Add an uppercase letter.")

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        recommendations.append("Add a lowercase letter.")

    # Check numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        recommendations.append("Add a number.")

    # Check special characters
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        recommendations.append("Add a special character.")

    # Determine password strength
    if score <= 1:
        strength = "Very Weak"
        color = "red"

    elif score == 2:
        strength = "Weak"
        color = "orange"

    elif score == 3:
        strength = "Moderate"
        color = "yellow"

    elif score == 4:
        strength = "Strong"
        color = "lightgreen"

    else:
        strength = "Very Strong"
        color = "lime"

    # Display results
    result_label.config(
        text=f"Password Strength: {strength}",
        fg=color
    )

    score_label.config(
        text=f"Security Score: {score}/5"
    )

    # Display recommendations
    if recommendations:
        recommendation_label.config(
            text="Recommendations:\n" + "\n".join(recommendations),
            fg="white"
        )
    else:
        recommendation_label.config(
            text="Excellent! All security checks passed.",
            fg="lime"
        )


# Show and hide password
def toggle_password():

    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        show_button.config(text="Hide")
    else:
        password_entry.config(show="*")
        show_button.config(text="Show")


# Main heading
heading = tk.Label(
    root,
    text="PASSWORD SECURITY ANALYZER",
    font=("Arial", 16, "bold"),
    bg="#101820",
    fg="cyan"
)

heading.pack(pady=25)


# Password instruction
instruction = tk.Label(
    root,
    text="Enter a password to analyze its strength",
    font=("Arial", 10),
    bg="#101820",
    fg="white"
)

instruction.pack(pady=10)


# Password input
password_entry = tk.Entry(
    root,
    width=30,
    font=("Arial", 14),
    show="*"
)

password_entry.pack(pady=10)


# Show password button
show_button = tk.Button(
    root,
    text="Show",
    command=toggle_password,
    bg="#34495E",
    fg="white"
)

show_button.pack(pady=5)


# Analyze button
analyze_button = tk.Button(
    root,
    text="CHECK PASSWORD",
    command=check_password,
    font=("Arial", 11, "bold"),
    bg="cyan",
    fg="black",
    width=20
)

analyze_button.pack(pady=20)


# Result display
result_label = tk.Label(
    root,
    text="Password Strength: Not Checked",
    font=("Arial", 12, "bold"),
    bg="#101820",
    fg="white"
)

result_label.pack(pady=10)


# Score display
score_label = tk.Label(
    root,
    text="Security Score: 0/5",
    font=("Arial", 11),
    bg="#101820",
    fg="white"
)

score_label.pack(pady=5)


# Recommendations
recommendation_label = tk.Label(
    root,
    text="",
    font=("Arial", 10),
    bg="#101820",
    fg="white",
    justify="left"
)

recommendation_label.pack(pady=20)


# Run application
root.mainloop()