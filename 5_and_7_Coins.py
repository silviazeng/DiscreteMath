# Recursion/Dynamic Programming
# Question: Imagine we have only 5- and 7-coins. One can prove that any large enough integer amount can be paid using only such coins. Yet clearly we cannot pay any of numbers 1, 2, 3, 4, 6, 8, 9 with our coins. What is the maximum amount that cannot be paid?

def can_pay(amount, coins=[5, 7], memo=None):
    if amount == 0:
        return True
    if amount <0:
        return False
    else:
        return can_pay(amount-5) or can_pay(amount-7)

def find_max_unpayable(coins):
    amount = 100
    while True:
        # while True: is a loop that runs indefinitely until it encounters a break or an exception occurs.In this case a return statement is encountered, which effectively breaks out of the loop.
        if not can_pay(amount):
            return amount
        else:
            amount -=1

coins = [5, 7]
result = find_max_unpayable(coins)
print(f"The maximum amount that cannot be paid is: {result}")