class Solution:

    def encode(self, strs: List[str]) -> str:
        sentence = []
        for s in strs:
            length = str(len(s))
            sentence.append(length)
            sentence.append("#")
            sentence.append(s)
            #for loop跑完長這樣
            #["5", "#", "Hello", "5", "#", "World"]

        return "".join(sentence)#join裡面放的是list讓他自己去接

    def decode(self, s: str) -> List[str]:
        answer = []
        i = 0
        while i < len(s): #用!=可能會跳過頭
            j = s.find("#", i)
            length = int(s[i: j]) #字串轉整數
            answer.append(s[j+1: j+1+length])
            i = i + 1 + (j - i) + length
        return answer