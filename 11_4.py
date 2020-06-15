import random


def rund_sum():
    while True:
        rund_num = random.randrange(1, 1000000)
        # That's cool however I prefer shorter lines so I would write
        if rund_num % 7  != 0: next
        if rund_num % 13 != 0: next
        if rund_num % 15 != 0: next
        return rund_num


rund_num_end = rund_sum()
print("rund num: ", rund_num_end)
