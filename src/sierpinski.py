def replace_char(s , n , c):
        s = s[0:n] + s[n:n+1].replace(s[n] , c) + s[n+1:]
        return s

def replace_interval(a,b,s,c):
	for i in range(a,b+1):
		s = replace_char(s,i,c)
	return s	



def base_triangle(z):
	a = "1"
	b = "_"
	# c = "_"
	j = 1
	n = z
	li = []
	for i in range(0,n - 1):
		li.append(((b) * (n - i - 1) + (a) * (j) + (b ) * (n - i - 2) + b))
		j+=2
	li.append((a) * (j - 1) + a)	
	return li
# lis = []






def positions_to_draw_triangles(r,n):
	s = 0
	iterations = 2 ** (n-1)
	rr = r / iterations
	pos=[]
	for i in range(0,iterations):
		pos.append((i*rr) + (rr/2))
	return pos	



def intermediates(s):
	li=[]
	for i in range(0,len(s)):
		if s[i] == "1":
			li.append(i)
		else:
			li.append(0)
	# print(li)		
	lis=[]		
	lis1=[]		
	l=[]
	l1=[]
	for i in range(1,len(li)):
		if(li[i-1] == 0 ):
			if(li[i] !=0):
				lis.append(li[i])
				# print(lis)
			elif(li[i] == 0):
				pass
		if(li[i-1] != 0):
			if(li[i] !=0):
				pass	
			elif(li[i] == 0):
				lis1.append(li[i-1])
				# print(lis)				
		else:
			l.append(lis)
			l1.append(lis1)	
	l2 = []
	for i in range(0,len(l[0])):
		l2.append((l[0][i], l1[0][i]))
	return l2	


def make_t(n):
	li = base_triangle()
	pos1 = []
	ll = len(li)
	pos1 = positions_to_draw_triangles(ll,n)
	pos = []
	pos.append(pos1[0])
	if(li[pos[0]].count('1') == 2*(pos[0])+1):
			for i in range(0,(li[pos[0]].count('1') - 1)/2):
				# print(i,pos[0]+i , len(li[pos[0]]) - pos[0]-i-1)
				li[pos[0] + i] = replace_interval(pos[0]+i , len(li[pos[0]]) - pos[0]-i-1 , li[pos[0] + i] , '_' )
	return li			

# li is base_triangle() here
def make_ts(n,l):
	li=l
	pos1 = []
	ll = len(li)
	pos1 = positions_to_draw_triangles(ll,n)
	pos = []
	for i in range(0,len(pos1)):
		pos.append(pos1[i])

	for k in range(0,len(pos)):
		if(li[pos[k]].count('1') == 2*(pos[k])+1):
			# print(pos[k],k, li[pos[k]].count('1'), 2*(pos[k])+1)
			for i in range(0,(li[pos[k]].count('1') - 1)/2):
				# print(i,ll-pos[k]+i , ((ll*2)-1)-(ll-pos[k]+i)-1)
				li[pos[k] + i] = replace_interval(ll-pos[k]+i , ((ll*2)-1)-(ll-pos[k]+i+1) , li[pos[k] + i] , '_' )
				# print(li[pos[k] + i])
				# print(".")
		else:
			intm = intermediates(li[pos[k]])
			# offset
			
			# print(intm , k ,pos[k], li[pos[k]])
			# for x1 in range(pos[k], ((pos[k]) + ((intm[0][1]-intm[0][0])/2)) ):
			for x2 in range(0,len(intm)):
				for x3 in range(0,((intm[0][1]-intm[0][0])/2)):
					li[pos[k]+x3] = replace_interval(intm[x2][0]+x3+1, intm[x2][1]-x3-1,li[pos[k]+x3], '_')
					# print(pos[k],intm[x2][0]+x3, intm[x2][1]-x3)
	
	return li

li=[]
	

def log_base2(n):
	i=0
	while True:
		if 2**i == n:
			return i
		else:
			i+=1	


def seirpinski(base_t, a):
	if a == 1:
		return base_triangle(base_t)
	if a <= log_base2(base_t):
		return make_ts(a-1,seirpinski( base_t,a-1))
	else:
		return "Limit can only be reached upto " + str(log_base2(base_t)) + " for given triangle dimensions"
li = seirpinski(int(input()) , int(input()) )				


for item in li:
	print item



























 