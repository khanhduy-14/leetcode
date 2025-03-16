class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r, m_rank = 0, cars, min(ranks)
        while l < r:
            m = (l + r) // 2
            count = 0
            time = m*m * m_rank
            for rank in ranks:
                c_car = floor(sqrt(time/rank))
                count+=c_car
            if count >= cars:
                r = m
            else:
                l = m + 1
        l = m_rank * (r-1) * (r-1)
        r = m_rank * r * r
        while l < r:
            count = 0
            m = (l + r) // 2
            for rank in ranks:
                c_car = floor(sqrt(m/rank))
                count+=c_car
              
            if count >= cars:
                r = m
            else:
                l = m + 1
        return l

        
        