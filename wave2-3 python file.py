while True:  
  oddSet = ['a', 'c', 'e', 'g']
  evenSet = ['b', 'd', 'f', 'h']
  oddnumbers = [1, 3, 5, 7]
  evennumbers = [2, 4, 6, 8]
  letter = input("Enter the letter:\n")
  while True:  
    try:
      number = int(input("Enter the number:\n"))
      break
    except ValueError:
      print("Number has to be an integer.\n")
  if letter.lower() in oddSet and number in oddnumbers:
    print("The square is black.\n")
  elif letter.lower() in evenSet and number in oddnumbers:
    print("The square is white.\n")
  elif letter.lower() in evenSet and number in evennumbers:
    print("The square is black.\n")
  elif letter.lower() in oddSet and number in evennumbers:
    print("The square is white.\n")
  else:
    print("Letter has to be a letter.\n")