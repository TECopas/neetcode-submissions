class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map_dict = {}
        for i in range(len(nums2)):
            map_dict[nums2[i]] = i
        
        ans_list = []
        for i in nums1:
            ans_list.append(map_dict[i])

        return ans_list