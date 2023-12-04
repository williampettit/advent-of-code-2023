# day1 p1

with open('1.in') as f:
  data = f.read()

lines = data.splitlines()

total = 0

for line in lines:
  # get first and last digit
  first_digit = None
  last_digit = None
  for c in line:
    if not c.isdigit():
      continue
    
    if first_digit == None:
      first_digit = int(c)

    last_digit = int(c)

  full_digit_str = f"{first_digit}{last_digit}"
  full_digit = int(full_digit_str)

  total += full_digit

print(f"{total = }")
