class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        version1 = version1.split('.')
        version2 = version2.split('.')

        while len(version1) < len(version2):
            version1.append('0')
        
        while len(version2) < len(version1):
            version2.append('0')
        
        for i in range(len(version1)):
            if int(version1[i]) > int(version2[i]):
                return 1
            elif  int(version1[i]) < int(version2[i]):
                return -1
        
        return 0
