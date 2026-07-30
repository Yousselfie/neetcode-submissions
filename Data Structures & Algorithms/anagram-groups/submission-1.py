class Solution:
    #what if i made a dictionary
    
    
    
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # the keys are all the unique, sorted words in strs
        dictionaries = {}

        # for loop through strs
        for word in strs:
            sorted_word=''.join(sorted(word))
            current_keys = dictionaries.keys()

            # if the sorted i str in strs is not a key in the dict, add a new key, and add the original word to the key's value list. whether it is or isn't, append to the value
            if(sorted_word not in current_keys):
                dictionaries[sorted_word] = ([])
            dictionaries[sorted_word].append(word)   

        #form the lists object to return
        lists=[]
        for key in dictionaries:
            lists.append(dictionaries[key])


        return(lists)
