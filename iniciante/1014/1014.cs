using System;

class URI
{

    static void Main(string[] args)
    {

        /**
        Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).
         */

        int a = int.Parse(Console.ReadLine());
        double b = float.Parse(Console.ReadLine());

        var consumo = new Consumo(a, b);

        Console.WriteLine("{0:F3} km/l", consumo.ConsumoMedio());
        Console.ReadLine();
    }

    class Consumo
    {
        private int distancia { get; set; }
        private double combustivel { get; set; }

        public Consumo(int a, double b)
        {
            this.distancia = a;
            this.combustivel = b;
        }
        public double ConsumoMedio() 
        {
            return distancia / combustivel;
        }
    }
}