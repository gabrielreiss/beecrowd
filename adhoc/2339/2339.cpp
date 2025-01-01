/*
    regra de negocio: C * F <= P
*/

#include<iostream>
#include<sstream>
#include<tuple>

using namespace std;

std::tuple<int, int, int> input_dados(){
    std::string input;
    char delimiter = ' ';
    std::string t;
    int count = 0; int C; int P; int F;

    std::getline(cin, input);

    std::stringstream ss(input);

    while(std::getline(ss, t, delimiter)){
        if(count==0){
            C = std::stoi(t);
        } else if(count==1){
            P = std::stoi(t);
        } else if(count==2){
            F = std::stoi(t);
            break;
        }
        count++;
    }
    return std::make_tuple(C,P,F);
}

int main(){
    auto [C, P, F] = input_dados();

    if((C * F) <= P){
        std::printf("S\n");
    } else {
        std::printf("N\n");
    }

    return 0;
}