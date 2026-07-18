class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hash_s = {}
        hash_t = {}
        for x,y in zip(s,t):
            hash_s[x]=1 + hash_s.get(x,0)
            hash_t[y]=1 + hash_t.get(y,0)
        for key in hash_s:
            if hash_s[key] != hash_t.get(key,0):
                return False
        return True