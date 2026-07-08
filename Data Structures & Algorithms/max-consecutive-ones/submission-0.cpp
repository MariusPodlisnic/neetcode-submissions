class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int count = 0;
        int max = 0;
        for(auto& num:nums){
            if(num == 1){
             count++;
             max = std::max(max,count);
            }
            else count = 0;          
    }
    return max;
    }
};