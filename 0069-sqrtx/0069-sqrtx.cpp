class Solution {
public:
int mySqrt(int x) {
    if (x==1) return 1;
    int lowerBound = 0;
    int upperBound = x;
    int avarage = x/2;
    while (true) {
        double trial = (long long)avarage*avarage;
        cout << lowerBound << endl;
        cout << upperBound << endl;
        if (trial < x) {
            lowerBound = avarage;
        }
        else if (trial > x) {
            upperBound = avarage;
        }
        avarage = (upperBound+lowerBound)/2;
        if (upperBound - lowerBound == 1||trial == x) break;
    }
    return avarage;
}
};