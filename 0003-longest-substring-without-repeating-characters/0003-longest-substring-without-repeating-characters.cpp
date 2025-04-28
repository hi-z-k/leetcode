class Solution {
public:
    int lengthOfLongestSubstring(string s) {
    int wordL = 1;
    vector<int> lengths;
    map<char,int> letters;
    int a = 0;
    int b = 1;
    letters[s[a]] = 1;
    while (a < s.size()) {
        char letter  = s[b];
        if (letters[letter] == 1 || b == s.size()) {
            lengths.push_back(wordL);
            a++;
            wordL = 1;
            b = a + 1;
            letters = {};
            letters[s[a]] = 1;
        }
        else {
            letters[letter] = 1;
            wordL += 1;
            b++;
        }
    }
    int maxLength = 0;
    for (int i: lengths) {
        if (maxLength < i) maxLength = i;
    }
    cout << maxLength << endl;
    return maxLength;
}

};