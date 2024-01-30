def do_something(input):
    if len(input) <= 1:
        return input
    return do_something(input[1:]) + input[0]

Result = do_something('hello')

print(Result)

#predict the output before running it
#explain the recursion
#explain the memory effiency
#explain the space efficiency