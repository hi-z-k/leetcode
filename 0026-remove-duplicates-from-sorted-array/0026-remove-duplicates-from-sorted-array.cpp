
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
    int a = 0;
    int b = 1;
    while(true){
        if (b==nums.size()) break;
        if (nums[a] == nums[b]){
            nums.erase(nums.begin()+b);
        } else{
            a++;
            b++;
        }
    }
    return nums.size();
    }
};