text = "GGATCGACAAAAATCTTATCCAACGCTTATCGGCCACGGGCAGCCGTATGGGGAAAACGTGGGCTATAATCCGCAATCAACATCCATGGCAATCGCATCTGTAATCCCCTTGTGAAGGAGCGATTCTACGCAGTTCATTATTGCGGTGGACAGAATGAGCGATATCCGACTATGTTTGCCACAGAGGGTCCAAGGGTTGGTTGTACTACGAGCACGCCTTCGTATTAATGTACTGAGTTTTCGGTCAATCATACGAGGGAAACCACCTCCTGGACTGCGGTGCCCGGTCCATGAGTGGGTCCGCATTATACCATTTAACCACAGTGTGACAGTGTTGCCGGTCTGCACAATCCTGTTTGGGCTAGGACGTTCGTAAAGACAAAAGTTGCATGGCGGAATCTGTCAGTTCAGGCTCATACTCACTTGAACTGGCCTGCGATCCATGCCTTCTCCGGCAGCCGCTGCGAGAGTTGTATTTTAGTGCGGCGTGGAACTGTCTGCTTCGTCGTAACGCTATATTATATAGGCGGTGCAGCAATCAGGGAAAGGCTCTGGTTCGAGATATTATTCCACGGAAAGTGGCTTGGTCCGATATACAAACCCGACCTCTGGGATTGTTAGGTGTTGTCCGCAAAACGGGGCATCATGGCCATCTAATGAGGAGGCCAAGTTGCTCTTGCGTGTTACACTAAGGCCTTCCCAATGCCCAGAGATTGGGGTCTCCCTATCACACCGTGACACTCAGTATGGCGCGATTGTTAATCATCTAACCCGGGTCACTACGACCGTGTAGTCGCTATCTCTCGCTTGGTATTGTGTAATGACCCACTACGCTTAAGCAAATCATAGGGAGCGCCCTATGGTGGCCCGCTGTCGCTGCACAGGTGAACAACTTAGCCATAGCCCATCTCTAAAAGTTTGGCTGTCATTGGACAAAGGCACCATATAGACTACGCAGTCAGCCACCAGTT"
num_c=0
num_g = 0
num_t = 0
num_a = 0

for i in text:
	if i == "C":
		num_c +=1
	elif i == "A":
		num_a +=1
	elif i == "G":
		num_g +=1
	else:
		num_t +=1

print("a", num_a)
print("c", num_c)
print("g", num_g)
print("t", num_t)
