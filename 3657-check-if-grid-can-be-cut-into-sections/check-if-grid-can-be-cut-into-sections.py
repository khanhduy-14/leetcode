class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        rectangles.sort(key=lambda x: x[1])
        m_rec = [rectangles[0]]
        

        for i in range(1, len(rectangles)):
            if rectangles[i][1] < m_rec[-1][3]:
                m_rec[-1][3] = max(rectangles[i][3], m_rec[-1][3])
            else:
                m_rec.append(rectangles[i])

        if len(m_rec) >= 3:
            return True
            
        rectangles.sort(key=lambda x: x[0])
        m_rec = [rectangles[0]]
        
        for i in range(1, len(rectangles)):
            if rectangles[i][0] < m_rec[-1][2]:
                m_rec[-1][2] = max(rectangles[i][2], m_rec[-1][2])
            else:
                m_rec.append(rectangles[i])
        if len(m_rec) >= 3:
            return True
        return False



        