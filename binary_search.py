#Searching algorithm, deler dataen op til den finder targetet

#functions that takes list and target

def sortalgo(list, target):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start<=end):
        print("Step", steps, ":", str(list[start:end+1]))

        steps = steps+1
        middle = (start + end) // 2

        if target == list[middle]: 
            return middle
        if target < list[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sortalgo(my_list, 2)
#multiple values : middle, start, end number of splits/steps
#recursion og while to 
#increase steps each time a split done
#conditions to track target pos



