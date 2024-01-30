def fizzbuzz(num):

    for i in range(1, num+1):
        output = ''
        if i % 3 == 0:
            output += 'Fizz'
        if i % 5 == 0:
            output += "Buzz"
        if output == '':
            output = i
        print(output)


fizzbuzz(50)



#attempt2
# def fizzbuzz(num):
#     for i in range(1, num+1):
#         output = ""
#         if i % 3 == 0:
#             output += "fizz"
#         if i % 5 == 0:
#             output += "buzz"
#         if output == "":
#             output = i
#         print(output)

# fizzbuzz(100)




# attempt 1
# def fizzbuzz(num):
#     for i in range(1,num+1):
#         if i % 3 == 0:
#             print("fizz")
#         if i % 5 == 0:
#             print("buzz")
#         if i % 3 == 0 and i % 5 == 0:
#             print("fizzbuzz")
#         else:
#             print(i)


# fizzbuzz(50)



