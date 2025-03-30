// prepare two pointers at first initially pointing to index a= 0 and b=1
//if the two elements getting pointed are the same, a doesn't change, indx(b) gets erased
// if they are different, you make a point to b and b to the next element by incrementing
// this code terminates when b reaches last pointer
// return nums.length

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int a = 0;
        int b = 1;
        while (b < nums.size()){

            if (nums[a] == nums[b]){
                nums.erase(nums.begin()+b);

            }
            else{
                a++;
                b++;
            }
        }
        return nums.size();
    }
};