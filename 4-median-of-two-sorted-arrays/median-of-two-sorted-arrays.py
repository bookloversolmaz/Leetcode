class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge the lists to make a new list and sort into ascending order
        merged_list = sorted(nums1 + nums2)
        # find the middle value
        middle_value = len(merged_list)
        if middle_value % 2 != 0:
            # if the list is an odd number of values, take the middle values
            # return float to 5 decimal place
            return round(float(merged_list[(middle_value // 2)]),5)
        else:
            # if even number of values in list, return average of two middle values
            mid1 = merged_list[(middle_value // 2) -1]
            mid2 = merged_list[(middle_value // 2)]
            return round((mid1 + mid2) / 2,5)
        