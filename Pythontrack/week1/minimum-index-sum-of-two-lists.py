class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_index = len(list1) + len(list2)
        common_strings = []

        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if i + j < min_index:
                        common_strings = []
                        common_strings.append(list1[i])
                        min_index = i + j
                    elif i + j == min_index:
                        common_strings.append(list1[i])
        
        return common_strings
