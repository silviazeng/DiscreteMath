# Imagine we have only 5- and 7-coins. One can prove that any large enough integer amount can be paid using only such coins. Yet clearly we cannot pay any of numbers 1, 2, 3, 4, 6, 8, 9 with our coins. What is the maximum amount that cannot be paid?

def can_pay(amount, coins=[5, 7], memo=None):
    if memo is None:
        memo = {}
    if amount == 0:
        return True
    if amount < 0:
        return False
    if amount in memo:
        return memo[amount]
    
    memo[amount] = any(can_pay(amount - coin, coins, memo) for coin in coins)
    return memo[amount]

def find_max_unpayable():
    amount = 1
    while True:
        if can_pay(amount):
            amount += 1
        else:
            if all(can_pay(i) for i in range(amount + 1, amount + max(coins) + 1)):
                return amount
            amount += 1

coins = [5, 7]
result = find_max_unpayable()
print(f"The maximum amount that cannot be paid is: {result}")