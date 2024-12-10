using System; 

class URI {

    static void Main(string[] args) { 

        /* Leia dois valores inteiros. A seguir, calcule o produto entre estes dois valores e atribua esta operação à variável PROD. A seguir mostre a variável PROD com mensagem correspondente. */

        int a = int.Parse(Console.ReadLine());
        int b = int.Parse(Console.ReadLine());

        Console.WriteLine("PROD = "+(a * b));
        Console.ReadLine();
    }

}