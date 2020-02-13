from data import arabic_roman

def read_roman():
  num = input("Enter Roman number: ").upper()

  print("Your Roman number is: ", num)
  return num

def to_arabic(input):
  result=0
  for key, value in arabic_roman.items():
    if input.startswith(value):
      result += key
      ilgis = len(value)
      input  = input[ilgis:]
  return result