sample_output = []

D = input("Enter number: ")
place = D.split(",")

print(place)
for num in place:
    Q = f"{(2 * 50 * D) / 30}"

    Q1 = Q ** 0.5



sample_output.append(Q1)


print(sample_output)
