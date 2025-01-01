#include<iostream>
#include<vector>

using namespace std;

int main(){
    vector<char> v = {'A', 'B', 'C', 'D', 'E'};
    int a = 7; int b = -1;
    char c = ' ';

    for(int i = 0; i < 5; i++){
        std::string comeco(a, c);
        std::string fim = b > 0 ? std::string(b,c) : "";
        
        if(i == 0){
            std::cout << comeco << v[i] << endl;
        } else{
            std::cout << comeco << v[i] << fim << v[i] << endl;
        }
        a--; b+= 2;
    }

    a = 4; b = 5;
    for(int i = 3; i >= 0; i--){
        std::string comeco(a, c);
        std::string fim = b > 0 ? std::string(b,c) : "";
        
        if(i == 0){
            std::cout << comeco << v[i] << endl;
        } else{
            std::cout << comeco << v[i] << fim << v[i] << endl;
        }
        a++; b-= 2;
    }
}