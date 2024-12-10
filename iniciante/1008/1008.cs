using System; 

class URI {

    static void Main(string[] args) { 

        /*
        Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.
         */

        int funcionario = int.Parse(Console.ReadLine());
        int horas = int.Parse(Console.ReadLine());
        double ValorHora = float.Parse(Console.ReadLine());

        double salario = horas * ValorHora;

        Console.WriteLine("NUMBER = " + funcionario);
        Console.WriteLine("SALARY = U$ {0:F2}", salario);

        Console.ReadLine();
    }

}