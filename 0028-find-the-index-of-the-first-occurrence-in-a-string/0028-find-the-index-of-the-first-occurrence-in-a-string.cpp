class Solution {
public:
    int strStr(string haystack, string needle) {

        string word = "";
        word = haystack[0];
        int a = 0;
        int b = 1;
        if(haystack.size() < needle.size()) return -1;
        while (a <= haystack.size()-needle.size()) {
            char letter  = haystack[b];
            if (b == a+needle.size()) {
                if (word == needle) return a;
                a++;
                word = "";
                word += haystack[a];
                b = a + 1;
            }
            else {
                word += letter;
                b++;
            }
        }
    return -1;
    }
};