from roman import to_arabic, read_roman
from arabic import to_roman, read_arabic

def main ():
  print("Hello, lets test your numbers")
  skaiciukas = read_arabic()
  atsakymas = to_roman (skaiciukas)
  print("Your Roman number: ", atsakymas)

  raides = read_roman()
  atsakymas = to_arabic(raides)
  print("Your Arabic number: ", atsakymas)

if __name__ == '__main__':
    main()