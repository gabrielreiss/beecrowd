using System; 

class URI {

    static void Main(string[] args) { 

        /*
        Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.
         */
        float comissao = 0.15f;

        string vendedor = Console.ReadLine();
        double fixo = float.Parse(Console.ReadLine());
        double vendas = float.Parse(Console.ReadLine());

        double total = fixo + vendas * comissao;

        Console.WriteLine("TOTAL = R$ {0:F2}", total);
        Console.ReadLine();
    }

}