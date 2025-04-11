class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
  int len = m+n;
  vector<int> merged;
  int idx = 0;
  //ensures that nums1 is always smaller than num2
  if (m>n) {
    vector<int> temp = nums2;
    int t = n;
    nums2=nums1;
    n = m;
    nums1 = temp;
    m=t;
  }


  int a = 0;
  int b = 0;
  while(idx<len){
    int aNum = (a<m)?nums1.at(a):1'000'000'0001;
    int bNum = (b<n)?nums2.at(b):bNum;
    if(aNum < bNum){
      if (a<m) {
        merged.push_back(aNum);
        a++;
      }
      else if (b<n) {
        merged.push_back(bNum);
        b++;
      }
    }
    else if (aNum > bNum){
      if (b<n) {
        merged.push_back(bNum);
        b++;
      }
      else if (a<m) {
        merged.push_back(aNum);
        a++;
      }
    }
    else {
      merged.push_back(aNum);
      a++;

      if(len > a + b){
        merged.push_back(bNum);
        b++;
      }

    }
    idx++;
    if (len <= a+b) break;
  }
  nums1 = merged;
}
};

