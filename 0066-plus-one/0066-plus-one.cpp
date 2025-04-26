class Solution {
public:
    vector<int> plusOne(vector<int>& digits){
    int Idx = digits.size()-1;
    while(digits.at(Idx)==9){
        digits[Idx] = 0;
        Idx--;
        if(Idx == -1){
            digits.insert(digits.begin(), 1);
            break;
        }
    }
    if(Idx>=0) digits[Idx] = digits[Idx]+1;
    return digits;
}

};