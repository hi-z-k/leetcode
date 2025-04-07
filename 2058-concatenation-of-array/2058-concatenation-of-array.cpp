class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> ans;
        int len = nums.size();
        for (int i = 0; i < 2*len; i++){
            ans.push_back(nums.at(i % len));
        }
        return ans;
    }
};