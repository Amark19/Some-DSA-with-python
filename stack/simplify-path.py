class Solution:
    def simplifyPath(self, path: str) -> str:
        # Trim out extra slashes
        # split an array by slash
        # push all values in stack from an arr
        # compare top element of stack & current element
        # if cureent element ".." then pop last element if there are any
        # if current element is . then pass
        i = 0
        path_arr = list(path)
        while i < len(path_arr):
            if i < len(path_arr) - 1:
                if path_arr[i] == path_arr[i+1] == "/":
                    path_arr.pop(i)
                    i += 1
            i += 1
        path = "".join(path_arr)
        path_splitted_arr = path.split("/")
        st = []
        for val in path_splitted_arr:
            if val =="":continue
            if val == "..":
                if st:st.pop()
            elif val == ".":
                continue
            else:
                st.append(val)
        ans_string = ""
        for val in st:
            ans_string += "/"
            ans_string += val
        return "/" if len(st)==0 else ans_string
