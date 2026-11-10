class Solution:
    def confusingNumber(self, n: int) -> bool:
        list_n = list(str(n))
        invalids = ("2", "3", "4", "5", "7")
        ans_list = []

        for i in list_n:
            if i in invalids: return False
            if i == "0": ans_list.insert(0,"0")
            if i == "1": ans_list.insert(0,"1")
            if i == "6": ans_list.insert(0,"9")
            if i == "8": ans_list.insert(0,"8")
            if i == "9": ans_list.insert(0,"6")

        ans_str = "".join(ans_list)

        if  "".join(list_n) == ans_str: return False

        return True
        