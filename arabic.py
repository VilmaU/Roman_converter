from data import arabic_roman

def read_arabic():
  num = int(input("Enter number not bigger than 3999 and bigger than 0: "))
  while num > 3999 or num < 1:
    num = int(input("Enter number not bigger than 3999 and bigger than 0: "))

  print("Your entered number is: ", num)
  return num

def to_roman(input):
  result=""
  for key, value in arabic_roman.items():
    if key <= input:
      result += value
      input -= key
  return result