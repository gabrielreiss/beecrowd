#include<iostream>
#include<iomanip>

using namespace std;

int main(){
    double a, b, c;
    cin >> a >> b >> c;

    double media = (a * 2 + b * 3 + c * 5) / 10.0;

    cout << "MEDIA = " << setprecision(1) << fixed << media << endl;

    return 0;
}