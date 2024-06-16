class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        c = len(image[0])
        flipimage = [[0] * len(image[0]) for _ in range(n)]
        
        for i in range(n):
            for j in range(len(image[0])):
                if image[i][c-j-1] == 0:
                    flipimage[i][j] = 1
                elif image[i][c-j-1] == 1:
                    flipimage[i][j] = 0

        return flipimage
