class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1 = list(map(int,version1.split('.')))
        arr2 = list(map(int,version2.split('.')))
        for a,b in zip_longest(arr1,arr2,fillvalue = 0):
            if a>b:
                return 1
            elif b>a:
                return -1
        return 0