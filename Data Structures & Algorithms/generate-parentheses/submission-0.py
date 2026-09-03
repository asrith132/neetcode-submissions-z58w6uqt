class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #either put a paranthese inside or put it beside

        res = []
        max_open = n

        def dfs(i, curr, open_par, close_par):
            if i == (n * 2):
                res.append(curr)
                return
            if open_par < n:
                dfs(i + 1, curr + "(", open_par + 1, close_par)
            if close_par < open_par:
                dfs(i + 1, curr + ")", open_par, close_par + 1)
    
        dfs(0, "", 0, 0)
        return res