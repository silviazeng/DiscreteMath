# Develop a Python method change(amount) that for any integer amount in the range from 24 to 1000 returns a list consisting of numbers 5 and 7 only, such that their sum is equal to amount. For example, change(28) may return [7, 7, 7, 7], while change(49) may return [7, 7, 7, 7, 7, 7, 7] or [5, 5, 5, 5, 5, 5, 5, 7, 7] or [7, 5, 5, 5, 5, 5, 5, 5, 7].

def can_pay(amount, coins=[5, 7]):
    if amount == 0:
        return True
    if amount <0:
        return False
    else:
        return can_pay(amount-5) or can_pay(amount-7)

def change(amount):
	if can_pay(amount-5):
		result.append(5)
		change(amount-5)
	elif can_pay(amount-7):
		result.append(7)
		change(amount-7)
	return result

result = []
print(change(26))