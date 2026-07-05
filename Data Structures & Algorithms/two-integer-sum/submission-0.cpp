class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> set;
        for(int i = 0;i<nums.size();i++){
            set[nums[i]] = i;
        }
        for(int i = 0;i<nums.size();i++){
            int difference = target - nums[i];
            if (set.count(difference) && set[difference] != i) {
                return {i, set[difference]};
            }
        }
        return {};
    }
};
