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
    int resultado;

    for(int i = 0; i < c.size(); i++){
        if(c[i] == 1){
            resultado = i + 1;
        }
    }
    cout << resultado << endl;
}