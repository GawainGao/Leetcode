class Solution(object):

   def simplifyPath(self, path):
       """
       :type path: str
       :rtype: str
       """
       stack = []
       i = 0
       res = ''
       path_len = len(path)
       while i < path_len:
           j = i+1
           while j < path_len and path[j] !="/":
                j += 1
           subpath = path[i+1:j]
           if len(subpath) > 0:
                if subpath == "..":
                    if stack != []:
                        stack.pop()
                elif subpath != ".":
                    stack.append(subpath)
           i = j
       if stack == []:
           return "/"
       for character in stack:
           res += "/"+ character
       print(res)
       return res
S = Solution()
S.simplifyPath("/a/./b/../../c/") 