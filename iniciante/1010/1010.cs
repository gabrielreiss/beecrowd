using System; 

class URI {

    static void Main(string[] args) { 
        /*
        Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago
         */

       var tuple1 = leitura(Console.ReadLine());
       var tuple2 = leitura(Console.ReadLine());

        double total = tuple1.Item2 * tuple1.Item3 + tuple2.Item2 * tuple2.Item3;
        Console.WriteLine("VALOR A PAGAR: R$ {0:F2}", total);
        Console.ReadLine();
    }

    static Tuple<int,int,double> leitura(string line)
    {
        //transformar isto em uma classe
        var arguments = line.Split(' ');
        int cod = int.Parse(arguments[0]);
        int qnt = int.Parse(arguments[1]);
        double valor = float.Parse(arguments[2]);
        return new Tuple<int, int, double>(cod,qnt,valor);
    }

}