class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
  int last = nums.size()-1;
  int first = 0;
  int mid{};
  if (target < nums.at(0)) return 0;
  if (target > nums.at(last)) return last+1;
  while (first <= last) {
    mid = (last + first) / 2;
    int num = nums.at(mid);
    if (target > num) {
      first = mid+1;
    }
    else if (target < num) {
      last = mid-1;
    }
    else return mid;
  }
  return first;
}
};