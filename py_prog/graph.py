def matrix(matX,matY):
	n = len (matX)
	matZ = [[0]*n for _ in range (n)]
	for i in range(n):
		for j in range(n):
			tmp = math.inf
			for k in range(n):
				d = matX[i][k] +matY[k][j]
				tmp= min(tmp,d)
			matZ[i][j] = tmp 
	return matZ


##all pairs shortest path 
def spath (matA):
	n = len(matA)
	matD = [ [ matA[i][j] for j in range(n)]for i in range(n)]
	s= 1
	while :s < n-1:
		matD =  matrix(matD,matA)
		t += 1
	return matD