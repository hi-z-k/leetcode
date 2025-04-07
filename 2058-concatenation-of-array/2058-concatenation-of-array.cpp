//the code runs twice the number of the provided vector
// add the elements to vector ans
// modulo operator is implemented so that when i exceeds the index of num, it restarts the index from 0 

class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> ans;
        for (int i = 0; i < 2*nums.size(); i++){
            ans.push_back(nums.at(i % (nums.size())));
        }
        return ans;
    }
};