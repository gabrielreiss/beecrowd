#include<iostream>


using namespace std;

int main(){
    int n;

    std::cin >> n;

    if(n <= 1){
        std::cout << "Top 1" << endl;
    }else if(n <= 3){
        std::cout << "Top 3" << endl;
    }else if(n <= 5){
        std::cout << "Top 5" << endl;
    }else if(n <= 10){
        std::cout << "Top 10" << endl;
    }else if(n <= 25){
        std::cout << "Top 25" << endl;
    }else if(n <= 50){
        std::cout << "Top 50" << endl;
    }else if(n <= 100){
        std::cout << "Top 100" << endl;
    }
}