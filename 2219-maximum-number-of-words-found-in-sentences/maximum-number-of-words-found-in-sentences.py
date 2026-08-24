class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        result = 0
        buffer_list = []
        for i in range(len(sentences)):
            buffer_list.append(sentences[i].strip().split(" "))
            len_words = len(buffer_list[i])
            result = max(result,len_words)
        return (result)
