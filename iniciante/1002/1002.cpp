#include<iostream>
#include <stdio.h>
#include <math.h>
#include <iomanip>

using namespace std;

int main(){
    double raio;
    cin >> raio;

    double area = 3.14159 * pow(raio, 2.0);
    
    cout << "A=" << setprecision(4) << fixed << area << endl;
}