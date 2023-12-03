import os

# Get the absolute path of the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, "List_elfs.txt")

# max_calories = 0
# current_calories = 0

# with open(file_path) as my_file:
#     for line in my_file.readlines():
#         line = line.rstrip("\n")
#         if len(line) == 0:
#             # Check if the current elf's calories exceed the maximum calories found so far
#             if current_calories > max_calories:
#                 max_calories = current_calories
#             # Reset current_calories for the next elf
#             current_calories = 0
#         else:
#             # Add the calories of the current item to the total for the current elf
#             current_calories += int(line)

# # Check the calories of the last elf after the loop
# if current_calories > max_calories:
#     max_calories = current_calories

# # Part 1: Find the elf with the most calories and display the total calories they carry
# print(f"The Elf with the most calories is carrying a total of {max_calories} calories.")

max_calories = 0
current_calories = 0
all_food = []  # List to store the total calories for each elf

with open(file_path) as my_file:
    for line in my_file.readlines():
        line = line.rstrip("\n")
        if len(line) == 0:
            # Add the total calories of the current elf to the list
            all_food.append(current_calories)
            # Check if the current elf's calories exceed the maximum calories found so far
            if current_calories > max_calories:
                max_calories = current_calories
            # Reset current_calories for the next elf
            current_calories = 0
        else:
            # Add the calories of the current item to the total for the current elf
            current_calories += int(line)

# Include the calories of the last elf in the calculation
all_food.append(current_calories)

# Sort the list in descending order to find the elf with the most calories
all_food = sorted(all_food, reverse=True)

# Part 1: Find the elf with the most calories and display the total calories they carry
print(f"The Elf with the most calories is carrying a total of {all_food[0]} calories.")

# Part 2: Calculate the total calories carried by the top three elves
top_three_food = all_food[0] + all_food[1] + all_food[2]
print(f"The top three Elves carry {top_three_food} calories.")