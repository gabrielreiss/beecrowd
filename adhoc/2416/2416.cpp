#include<iostream>

using namespace std;

int main(){

    int entrada[2];
    for(int i=0; i<2; i++){
        cin >> entrada[i];
    }

    int ponto_termino = entrada[0] % entrada[1];

    cout << ponto_termino << endl;

    return 0;
}