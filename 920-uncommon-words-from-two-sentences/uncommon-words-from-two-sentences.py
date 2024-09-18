class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        uncommon = []
        s1 = s1.split(" ")
        s2 = s2.split(" ")
        for word in s1:
            s1_ = s1.copy()
            s1_.remove(word)
            if word not in s2 and word not in s1_:
                uncommon.append(word)
                
        for word in s2:
            s2_ = s2.copy()
            s2_.remove(word)
            if word not in s1 and word not in s2_:
                uncommon.append(word)
        
        return uncommon