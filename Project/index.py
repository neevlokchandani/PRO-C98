def swapFileData():
  file1 = input("Enter the original file anme:- ")
  file2 = input("Enter the second file name:- ")
  with open(f'{file1}.txt', 'r') as a:
    data_a = a.read()
  with open(f'{file2}.txt', 'r') as b:
    data_b = b.read()
  with open(f'{file1}.txt', 'w+') as a:
    a.write(data_b)
  with open(f'{file2}.txt', 'w+') as b:
    b.write(data_a)
  print("Your file has been swapped. Check it!")

swapFileData()