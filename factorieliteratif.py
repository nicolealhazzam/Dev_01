def factorieliteratif(n):
	i = 1
	reponse = 1
	while(i<=n):
		reponse = reponse*i
		i += 1
	return reponse

print(factorieliteratif(7))
