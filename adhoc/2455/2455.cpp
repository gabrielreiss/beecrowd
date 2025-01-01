#include<iostream>
#include<vector>
#include<sstream>

using namespace std;

std::vector<int> input_dados(){
    std::string input;
    char delimiter = ' ';
    std::string t;
    int count = 0;
    std::vector<int> resultado;

    std::getline(cin, input);

    std::stringstream ss(input);

    while(std::getline(ss, t, delimiter)){
       resultado.push_back(std::stoi(t));
       count++;
    }
    return resultado;
}

int main(){
    vector<int> c = input_dados();

    if(c[0] * c[1] == c[2] * c[3]){
        cout << 0 << endl;
    } else if(c[0] * c[1] > c[2] * c[3]){
         cout << -1 << endl;
    } else{
        cout << 1 << endl;
    }
}