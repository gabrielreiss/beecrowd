#include<iostream>

using namespace std;

int input_dados(){
    int n;
    std::string input;
    cin >> input;
    n = std::stoi(input);
    return n;
}

int main(){
    int r, n = input_dados();
    r = ((n+1)*(n+2)) / 2;
    cout << r << std::endl;
}