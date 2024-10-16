s = [1000]
i = 0
while s[i] <= 1000000:
	s.append(s[i] * (1 + 0.10))
	i += 1
print(f"You will have more than $1,000,000 on day {i+1}.")