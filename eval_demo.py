import itertools


def eval():
	a = [ [1,2,3], [4,5], [6]]
	b = [ [1,2], [3,4], [5,6]]

	new_a = pair_wise_comparision(a)
	new_b = pair_wise_comparision(b)

	precision = len(set(new_a).intersection(new_b)) / len(new_a)
	recall = len(set(new_a).intersection(new_b)) / len(new_b)
	f_score = (2*precision*recall) / (precision+recall)

	print(precision)
	print(recall)
	print(f_score)
	print(new_a)
	print(new_b)



def pair_wise_comparision(a):
	gold_pair = []
	for item in a:
		gold_pair.append(list(itertools.combinations(item, 2)))
	
	flat_list = [item for sublist in gold_pair for item in sublist]
	return flat_list

def cluster_level():
	pass

if __name__ == "__main__":
	eval()