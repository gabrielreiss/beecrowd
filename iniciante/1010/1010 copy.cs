using System; 

class URI {

    static void Main(string[] args) { 
        /*
        Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago
         */

       Compra compra1 = new Compra();
       compra1.leitura(Console.ReadLine());
       Compra compra2 = new Compra();
       compra2.leitura(Console.ReadLine());

        double total = compra1.qnt * compra1.valor + compra2.qnt * compra2.valor;
        Console.WriteLine("VALOR A PAGAR: R$ {0:F2}", total);
        Console.ReadLine();
    }

    public class Compra{
        public int cod;
        public int qnt;
        public double valor;

        public void leitura(string line){
            var arguments = line.Split(' ');
            cod = int.Parse(arguments[0]);
            qnt = int.Parse(arguments[1]);
            valor = float.Parse(arguments[2]);
        }
    }

}