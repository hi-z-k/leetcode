class Solution {
public:
    int lengthOfLastWord(string s) {
        int idx = s.length()-1;
    int count = 0;
    for(int i=idx; i>=0;i--){
        if (!isspace(s.at(i))) {
            count++;
        }
        if (isspace(s[i]) && count > 0) break;
    }
    return count;
    }
};