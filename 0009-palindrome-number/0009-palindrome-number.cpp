class Solution {
public:
int power(int num, int count) {
    if (num % 10 == num) return count;
    return power(num/10, count+1);
}
double reverse(int num, int power) {
    if (power == 0) return num;
    return (num%10)* pow(10,power) + reverse(num/10, power-1);
}
    bool isPalindrome(int x) {
        if(x<0) return false;
        int exponent = power(x,0);
        double rev = reverse(x, exponent);
        return x == rev;
    }
};