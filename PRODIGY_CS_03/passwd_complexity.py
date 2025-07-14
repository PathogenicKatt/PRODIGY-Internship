import string
#--
def check_passwd(passwd):
  feedback = []
  score = 0
  # Length check
  if len(passwd) < 8:
      feedback.append("Password should be at least 8 characters long.")
  else:
      score += 1
  # Lowercase check
  if not any(k in string.ascii_lowercase for k in passwd):
      feedback.append("Add at least one lowercase letter.")
  else:
      score += 1
  # Uppercase check
  if not any(k in string.ascii_uppercase for k in passwd):
      feedback.append("Add at least one uppercase letter.")
  else:
      score += 1
  # Digit check
  if not any(k in string.digits for k in passwd):
      feedback.append("Add at least one digit.")
  else:
      score += 1
  # Special character check
  if not any(k in string.punctuation for k in passwd):
      feedback.append("Add at least one special character.")
  else:
      score += 1
  # Strength rating
  if score == 5:
      strength = "Strong"
  elif score >= 3:
      strength = "Medium"
  else:
      strength = "Weak"
  #--
  return strength, feedback
#--
if __name__ == "__main__":
  pwd = input("Enter a password to check: ")
  strength, feedback = check_passwd(pwd)
  print(f"Strength: {strength}")
  if feedback:
      print("Feedback:")
      for f in feedback:
          print("-", f)
