#include<iostream>
#include<string>
#include<functional>
#include<tuple>
#include <sstream>

using namespace std;

enum class Acoes {
    fechou,
    clicou,
    unknown
};

Acoes hashString(const std::string& str){
    if(str == "fechou") return Acoes::fechou;
    if(str == "clicou") return Acoes::clicou;
    return Acoes::unknown;
}

std::tuple<int, int> input_dados(){
    string input;
    char delimiter = ' ';
    string t;
    int count = 0; int first = 0; int second = 0;

    getline(cin, input);
    
    stringstream ss(input);

    while(std::getline(ss, t, delimiter)){
        if (count == 0){
            first = std::stoi(t);
        } else if (count == 1){
            second = std::stoi(t);
            break;
        }
        count++;
    }

    return std::make_tuple(first, second);
}

class Browser{
    public:
        Browser(int abas) : _abas(abas) {}

        void acao(const std::string& acoes){
            switch (hashString(acoes)){
                case Acoes::fechou:
                    _abas += 1;                
                    break;
                
                case Acoes::clicou:
                    _abas -=1;
                default:
                    break;
            }
        }

        int getAbas() const {
            return _abas;
        }

    private:
        int _abas;
};

int main(){
    auto [abas_inicial, sequencia] = input_dados();

    Browser browser(abas_inicial);

    for (int i = 0; i < sequencia; i++){
        string acao;
        cin >> acao;
        browser.acao(acao);
    }

    cout << browser.getAbas() << endl;

    return 0;
}