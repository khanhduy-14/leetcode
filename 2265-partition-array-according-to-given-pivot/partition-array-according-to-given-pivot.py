class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res,sn, ln, cp =[], [], [], 0
        for i in nums:
            if i == pivot:
                cp+=1
            elif i > pivot:
                ln.append(i)
            else:
                sn.append(i)
        
        for i in sn:
            res.append(i)
        
        while cp > 0:
            res.append(pivot)
            cp-=1
        for i in ln:
            res.append(i)
        

        return res