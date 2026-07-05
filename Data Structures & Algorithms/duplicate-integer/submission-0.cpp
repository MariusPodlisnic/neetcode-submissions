class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        for(auto& num:nums){
            int count = 0;
            count = std::count(nums.begin(),nums.end(),num);
            if(count>1) return true;
        }
        return false;
    }
};