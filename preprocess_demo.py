

def preprocess():
	a = {}
	a['block1'] = [[1], [2], [3], [1,2], [2,3]]
	a['block2'] = [[1], [2], [3], [4], [2,3], [3,4]]


	for key, l in a.items():
		len_l = len(l)
		i = 0
		while i < (len_l - 1):
		    for j in range(i + 1, len_l):

		        # i,j iterate over all pairs of l's elements including new 
		        # elements from merged pairs. We use len_l because len(l)
		        # may change as we iterate
		        i_set = set(l[i])
		        j_set = set(l[j])

		        if len(i_set.intersection(j_set)) > 0:
		            # Remove these two from list
		            l.pop(j)
		            l.pop(i)

		            # Merge them and append to the orig. list
		            ij_union = list(i_set.union(j_set))
		            l.append(ij_union)

		            # len(l) has changed
		            len_l -= 1

		            # adjust 'i' because elements shifted
		            i -= 1

		            # abort inner loop, continue with next l[i]
		            break

		    i += 1
		print(l)


if __name__ == "__main__":
	preprocess()