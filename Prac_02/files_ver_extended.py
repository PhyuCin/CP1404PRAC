name = input("Enter your name: ")
out_file = open('name.txt', 'w')
print(name, file=out_file)
out_file.close()


out_file = open('name.txt', 'r')
print("Your name is", out_file.read())


num_file = open('number.txt', 'r')
num_list = num_file.readlines()
sum = 0
for i in range(0, len(num_list)):
    sum += int(num_list[i])
print(sum)