numbers = [35, 16, 10, 34, 37, 25]

# Refactoriza usando List Comprehension 👇

even_numbers = []

for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)

print(even_numbers)