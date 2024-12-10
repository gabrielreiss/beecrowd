using System; 

class URI {

    static void Main(string[] args) { 
        /*
        Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, 
        o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2.
         Após, calcule e mostre o valor a ser pago
         */

        Console.WriteLine("Digite as informações da compra 1");
        var compraStr = Console.ReadLine();
        var compra1 = new Compra(
            int.Parse(compraStr.Split(' ')[0]),
            int.Parse(compraStr.Split(' ')[1]),
            float.Parse(compraStr.Split(' ')[2]));


        Console.WriteLine("Digite as informações da compra 2");
        compraStr = Console.ReadLine();
        var compra2 = new Compra(
            int.Parse(compraStr.Split(' ')[0]),
            int.Parse(compraStr.Split(' ')[1]),
            float.Parse(compraStr.Split(' ')[2]));

        Console.WriteLine("VALOR A PAGAR: R$ {0:F2}", compra1.TotalDaCompra() + compra2.TotalDaCompra());
        Console.ReadLine();
    }

    public class Compra {
        
        public int Cod { get; set; }
        public int Qnt { get; set; }
        public double Valor { get; set; }
        
        public Compra(int cod, int qnt, double valor)
        {
            this.Cod = cod;
            this.Qnt = qnt;
            this.Valor = valor;
        }

        public double TotalDaCompra() {
            return this.Qnt * this.Valor;
        }
    }

}