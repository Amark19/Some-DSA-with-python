class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        vis = set(wordList)
        alp = "abcdefghijklmnopqrstuvwzxyz"
        que = []
        que.append([beginWord])
        used_on_level = [beginWord]
        ans = []
        level = 0
        while que:
            element = que[0]
            last_element = element[-1]
            del que[0]
            if len(element) > level:
                level += 1
                # print(used_on_level)
                for val in used_on_level:
                    if val in vis:
                        vis.remove(val)
                # used_on_level = []

            if last_element == endWord:
                if len(ans) == 0:
                    ans.append(element)
                elif len(ans[0]) == len(element):
                    ans.append(element)
            for i in range(len(last_element)):
                for a in alp:
                    char_arr = list(last_element)
                    char_arr[i] = a
                    mod_val = "".join(char_arr)
                    if mod_val in vis:
                        temp = element.copy()
                        temp.append(mod_val)
                        que.append(temp)
                        used_on_level.append(mod_val)
            # print(que)
        return ans