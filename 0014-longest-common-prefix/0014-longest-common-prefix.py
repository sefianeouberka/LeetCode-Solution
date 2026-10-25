class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_length = max(len(i) for i in strs)
        matrix = []
        liste = []
        if strs == [""] : return ""
        if len(strs) == 1 : return "".join(strs)
        if max_length == 0 : return ""
        for i in strs :
            row = list(i)
            gap = max_length - len(row)
            row.extend([""]*gap)
            matrix.append(row)
        for n in range(max_length) :
            for m in range(len(strs)-1) :
                if matrix[m][n] != matrix[m+1][n] :
                    return "".join(liste)
            liste.append(matrix[0][n])
        return "".join(liste)

            

            
        