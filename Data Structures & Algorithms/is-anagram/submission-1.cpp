class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length()) return false;
        unordered_map<char,int> set_s;
        unordered_map<char,int> set_t;
        for(size_t i = 0;i<s.size();i++){
            set_s[s[i]]++;
            set_t[t[i]]++;
        }
        return set_s == set_t;
    }
};
