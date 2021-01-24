class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        DNA = []
        for i in range(len(s)-9):          
            seq = s[i:i+10]
            for j in range(i+1,len(s)-9):
                if seq == s[(j):(j+10)] and seq not in DNA: 
                    DNA.append(seq)
        return DNA


class Solution2(object):
    def findRepeatedDnaSequences(self, s):
        ht = {}
        DNA = []
        for i in range(len(s)-9):
            seq = s[i:i+10]
            if seq not in ht: ht[seq]=1
            else: ht[seq] += 1
        for j in ht:
            if ht[j]>1: DNA.append(j)
        return DNA 