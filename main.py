x = 666

atas = 1000
bawah = 0

selisih = [atas]
tmp_i = 0
while True:
	tmp = selisih[len(selisih)-1]
	if tmp < 10:
		break
	else:
		selisih.append(int(selisih[tmp_i]/2))
	tmp_i += 1

for selisih_ in selisih:
	if selisih_ < 10:
		for i in range(bawah, (atas+1)):
			if i == x:
				print(i)
				break
	else:
		if x<=(atas-selisih_):
			atas = int(atas-selisih_)
		elif x>=(atas-selisih_):
			bawah = int(atas-selisih_)