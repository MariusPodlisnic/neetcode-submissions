class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        nums.erase(std::remove(nums.begin(), nums.end(), val), nums.end());
        int k = static_cast<int>(nums.size());
        return k;
    }
};