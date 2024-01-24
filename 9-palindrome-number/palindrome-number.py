class Solution:
    def isPalindrome(self, x: int) -> bool:
        # convert x to string
        str_num = str(x)
        # convert x to list
        number_list = list(str_num)
        #use the reverse method of the list to reverse the list
        number_list.reverse()
        #convert the list into number again
        reversed_x = "".join(number_list)
        # create an if function that compare x to reverse x, if the same retrun true
        # otherwise return false
        if str_num != reversed_x:
            return False
        else:
            return True