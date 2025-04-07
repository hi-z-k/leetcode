class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> ans;
        int len = nums.size();
        int idx{};
        for (int i = 0; i < 2*len; i++){
            idx = i % len;
            ans.push_back(nums.at(idx));
            cout << ans.at(i) << endl;
        }
        return ans;
    }
};