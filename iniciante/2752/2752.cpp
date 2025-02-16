#include <iostream>
#include <iomanip> // Para manipuladores como setw() e setprecision()

int main() {
    std::string str(50, ' ');  // String de 50 espaços
    str = "AMO FAZER EXERCICIO NO URI";

    std::cout << "<" << str << ">\n";
    std::cout << "<" << std::setw(30) << str << ">\n";
    std::cout << "<" << str.substr(0, 20) << ">\n";
    std::cout << "<" << std::left << std::setw(20) << str << ">\n";
    std::cout << "<" << std::left << std::setw(30) << str << ">\n";
    std::cout << "<" << str.substr(0, 30) << ">\n";
    std::cout << "<" << std::right << std::setw(30) << str.substr(0, 20) << ">\n";
    std::cout << "<" << std::left << std::setw(30) << str.substr(0, 20) << ">\n";

    return 0;
}