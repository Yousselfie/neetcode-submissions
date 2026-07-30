class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for num in nums:
            current_keys=dictionary.keys()
            if num not in current_keys:
                dictionary[num] = 0
            dictionary[num]+=1

        #sort the dictionary
        sorted_dictionary_keys = [k for k, v in sorted(dictionary.items(), key=lambda item:item[1], reverse=True)]

        top_k_results=[]
        for i in range(k):
            top_k_results.append(sorted_dictionary_keys[i])

        return top_k_results

        