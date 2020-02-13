from data import arabic_roman

roman_digit_set = {"I", "V", "X", "L", "C", "D", "M"}
def is_valid_roman_numb(numb):
  result = True
  for  elem in numb:
    if elem not in roman_digit_set:
        result = False
  return result


def read_roman():
  num = input("Enter Roman number: ").upper()
  while not is_valid_roman_numb(num):
    num = input("Your number is not correct, enter Roman number: ").upper()
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