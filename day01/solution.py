with open("calories.txt", "r") as f:
    calories_str = f.read()
    calories_list = [calories.strip().split('\n') for calories in calories_str.split('\n\n')]
    calories_sums = [sum(list(map(int, calories))) for calories in calories_list]
    calories_sums.sort(reverse=True)
    print("Top calories elf: {} (task 1)".format(calories_sums[0]))
    print("Top 3 calories elves sum: {} (task 2)".format(sum(calories_sums[:3])))
