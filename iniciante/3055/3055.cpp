#include<iostream>

using namespace std;

int reverse_mean(int a, int m){
    return (m * 2) - a;
}

int main(){
    int a, m;

    std::cin >> a;
    std::cin >> m;

    std::cout << reverse_mean(a, m) << endl;

    return 0;
}


