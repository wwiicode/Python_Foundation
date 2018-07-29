def zhuzhu_Diamond(karat):
	l,r = '/', '\\'
	rad = karat // 2
	s = ''
	for row in range(karat):
		if row == rad:
			l,r = r,l
		if row < rad:
			nchar = row + 1
		else:
			nchar = karat - row
		left = (l*nchar).rjust(rad)
		right = (r*nchar).ljust(rad)
		s += left + right + '\n'
	return s[:-1]

karat = int(input("Please enter how many karat of diamond you want\n"))
print(zhuzhu_Diamond(karat))