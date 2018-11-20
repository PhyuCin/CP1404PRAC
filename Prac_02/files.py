name = input("Enter your name: ")
out_file = open('name.txt', 'w')
print(name, file=out_file)
out_file.close()


out_file = open('name.txt', 'r')
print("Your name is", out_file.read())


num_file = open('number.txt', 'r')
first_num = int(num_file.readline())
second_num = int(num_file.readline())
sum = first_num + second_num
print(sum)