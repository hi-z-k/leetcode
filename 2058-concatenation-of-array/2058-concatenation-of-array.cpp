class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> ans;
        int idx{};
        for (int i = 0; i < 2*nums.size(); i++){
            idx = i % nums.size();
            ans.push_back(nums.at(idx));
            cout << ans.at(i) << endl;
        }
        return ans;
    }
};