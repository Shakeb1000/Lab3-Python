# Author: Shakeb Siddiqui
# Collaborator: Samarth Tehri sqt5555@psu.edu
# Collaborator: James Mattison jwm6532@psu.edu
# Collaborator: Gabriel Charpentier gbc5202@psu.edu
# Section: 10
# Breakout: 4

def run():
  num = int(input("Enter an int: "))
  sum = sum_n(num)
  print(f"sum is {sum}.")
  word = input("Enter a string: ")
  print_n(word, num)

def sum_n(n):
  if n <= 0:
    return 0
  return n + sum_n(n-1)

def print_n(s, n):
  if n <= 0:
    return
  print(f"{s}")
  print_n(s, n-1)

if __name__ == "__main__":
  run()