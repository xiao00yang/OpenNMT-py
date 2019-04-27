# could filter some comments, eg. garbige or short comments
from collections import Counter
sourcePath = "/Users/xiao0_0yang/Documents/commentGeneration/dataset/generation_CHN/seq2seq_with_title_team_preprocessed_Test.txt"
srcPath = "/Users/xiao0_0yang/Documents/commentGeneration/git/OpenNMT-py/data/toutiao/noShort_withTitle/src-test.txt"
tgtPath = "/Users/xiao0_0yang/Documents/commentGeneration/git/OpenNMT-py/data/toutiao/noShort_withTitle/tgt-test.txt"

sourceFile = open(sourcePath, "r", encoding = "utf-8")
srcFile = open(srcPath, "w", encoding = "utf-8")
tgtFile = open(tgtPath, "w", encoding = "utf-8")

commentsLenList = []
index = 0
skip = False
for line in sourceFile:
	line = line.strip()
	length = len(line.split())
	commentsLenList.append(length)
	if index%2 == 0:

		if "万博" in line:
			index += 1
			skip = True
			continue
		elif length < 3:
			index += 1
			skip = True
			continue
		tgtFile.write(line+"\n")
	else:
		if skip:
			index += 1
			skip = False
			continue
		srcFile.write(line+"\n")
	index += 1

counter = Counter(commentsLenList)
sum_of_numbers = sum(number*count for number, count in dict(counter).items())
count = sum(count for n, count in dict(counter).items())
mean = sum_of_numbers / count

print("The histogram of comment length is: ", counter)
print("Average length is: ", mean)