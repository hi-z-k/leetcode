//loop through the elements
// start adding if it is a 1, otherwise initialize it to zero

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int count = 0;
        int temp{};
        for(int n:nums){
            if (n==1) count +=1;
            else{
                temp = (count>temp)?count:temp;
                count = 0;
            }
        }
        temp = (count>temp)?count:temp;
        return temp;
}
};