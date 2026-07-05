class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen_nums;
        for(auto& num:nums){
            if(seen_nums.count(num)) return true;
            seen_nums.insert(num);
        }
        return false;
    }
};