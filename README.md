# Task 3: Password Strength Checker
This task checks the strength of a password based on length and character variety.
-assess_password_strength(password): This function checks if a password
meets five criteria:
- At least 8 characters long.
- Contains uppercase letters.
- Contains lowercase letters.
- Contains numbers.
- Contains special characters.
The function outputs which criteria are met and calculates a `strength_score` based
on how many criteria are satisfied, providing a rating from "Very Weak" to "Very
Strong".
- main(): The main function prompts the user to enter a password and calls
`assess_password_strength` to evaluate its strength and provide feedback.
