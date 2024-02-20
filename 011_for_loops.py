# for loops used to repeat code set amount of times

# for i in range(start, stop, step) 
# start = starting number
# stop = ending number (not including) final number
# step = incremental number (can use negatives)

i=0
for i in range(3, -1, -1):
    print(i)

print('')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i, element in enumerate(alphabet):
    print(i + 1)
