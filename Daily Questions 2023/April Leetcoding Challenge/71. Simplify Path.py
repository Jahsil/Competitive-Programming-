class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        N = len(path)
        for i in range(N):
            if len(stack) > 0 and path[i] == ".." :
                stack.pop()
            elif path[i] not in [".." , "." , ""]:
                stack.append(path[i])
        return "/" + "/".join(stack)
       
