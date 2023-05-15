def main():
  intro()

  try:
    cups_ounces = int(input('Enter the number of cups:'))

    cups_to_ounces(cups_ounces)

  except:
    print("An exception occurred, try again by entering only a number")
    print()
    main()

def intro():
    print('This program converts measurements')
    print('in cups to fluid ounces. For your')
    print('1 cup = 8 fluid ounces')
    print()

def cups_to_ounces(cups):
    ounces = cups * 8
    print('That converts to ', ounces, 'ounces.')

main()