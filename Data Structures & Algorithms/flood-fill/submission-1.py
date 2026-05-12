class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        originalColor = image[sr][sc]
        if originalColor == color:
            return image 
        
        self.dfs(image,sr,sc,originalColor, color)
        return image
    
    def dfs(self, image, sr,sc,originalColor,color):

        if (sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or originalColor != image[sr][sc]):
            return
        image[sr][sc] = color
        self.dfs(image,sr+1,sc,originalColor, color)
        self.dfs(image,sr-1,sc,originalColor, color)
        self.dfs(image,sr,sc+1,originalColor, color)
        self.dfs(image,sr,sc-1,originalColor, color)

