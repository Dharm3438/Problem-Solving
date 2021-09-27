'''
2001. Number of Pairs of Interchangeable Rectangles

You are given n rectangles represented by a 0-indexed 2D integer array rectangles, where rectangles[i] = [widthi, heighti] denotes the width and height of the ith rectangle.

Two rectangles i and j (i < j) are considered interchangeable if they have the same width-to-height ratio. More formally, two rectangles are interchangeable if widthi/heighti == widthj/heightj (using decimal division, not integer division).

Return the number of pairs of interchangeable rectangles in rectangles.
'''

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        n = len(rectangles)
        m = len(rectangles[0])
        store = dict()
        arr = [0]*((10**5)+1)
        ct = 1
        for i in range(1,len(arr)):
            arr[i] = arr[i-1] + ct
            ct+=1
        
        print(arr[:7])
        
        for i in range(n-1,-1,-1):
            if(rectangles[i][0]/rectangles[i][1] in store):
                store[rectangles[i][0]/rectangles[i][1]] += 1
            else:
                store[rectangles[i][0]/rectangles[i][1]] = 1
                

        sumi=0
        print(store)
        for key in store:
            sumi += arr[store[key]-1]
        
        return sumi