import re
import getpass


def load_common_passwords(filename="common_password.txt"):
  try:
    with open(filename, "r") as file:
      common_passwords = file.read().splitlines()
    return common_passwords
  except FileNotFoundError:
    return []
  

def check_password_strength(password):
  strength = 0
  remarks = []


  if len(password) >= 8:
    strength += 1
  else:
    remarks.append("Password should be at least 8 characters long.")

  if re.search(r"[A-Z]",password):
    strength += 1
  else: 
    remarks.append("Include at least one uppercase letter.")

  if re.search(r"[a-z]",password):
    strength += 1
  else: 
    remarks.append("Include at least one lowercase letter.")

  if re.search(r"[0-9]",password):
    strength += 1
  else:
    remarks.append("Include at least one digit, eg: 0 - 9")

  if re.search(r"[!@#$%^&*(),.{}|<>?':;\"]",password):
    strength += 1
  else:
    remarks.append("Include at least one special character.")


  common_passwords = load_common_passwords()
  if password in common_passwords:
    remarks.append("Password is too common. Avoid using easily guessable passwords.")
  else:
    strength += 1

  
  if strength >= 5:
    level = "Strong"
  elif 3 <= strength < 5:
    level = "Moderate"
  else:
    level = "Weak"

  return level,remarks


def save_report(password, level, remarks, filename="password_report.txt"):
  with open(filename, "a") as file:
    file.write(f"Password Tested: {'*' * len(password)}\n")
    file.write(f"Strength Level: {level}\n")
    file.write("Remarks:\n")
    for remark in remarks:
      file.write(f"- {remark}\n")
    file.write("-" * 40 + "\n")


def main():
  print("\n=== Password Strength Checker ===\n")


  password = getpass.getpass("Enter your password to check: ")

  level, remarks = check_password_strength(password)

  print(f"\nPassword Strength: {level}")
  if remarks:
    print("Suggestions to Improve:")
    for remark in remarks:
      print(f"- {remark}")


  save = input("\nDo you want to save the password report ? (y/n)").lower()
  if save == 'y':
    save_report(password, level, remarks)
    print("Report saved successfully")
  else:
    print("Report not saved.")


if __name__ == "__main__":
  main()
    

