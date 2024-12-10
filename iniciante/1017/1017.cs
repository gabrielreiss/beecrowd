using System;

class URI
{

    static void Main(string[] args)
    {

        /**
        Joaozinho quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem, ao utilizar um automóvel que faz 12 KM/L. Para isso, ele gostaria que você o auxiliasse através de um simples programa. Para efetuar o cálculo, deve-se fornecer o tempo gasto na viagem (em horas) e a velocidade média durante a mesma (em km/h). 
        Assim, pode-se obter distância percorrida e, em seguida, calcular quantos litros seriam necessários. Mostre o valor com 3 casas decimais após o ponto.
         */
        int tempo = int.Parse(Console.ReadLine());
        int velocidade = int.Parse(Console.ReadLine());

        Viagem viagem = new Viagem(tempo, velocidade);

        Console.WriteLine("{0:F3}", viagem.Consumo());
        Console.ReadLine();
    }
    class Viagem {
        public int tempo { get; set; }
        public int velocidade { get; set; }
        public int rendimento = 12;

        public Viagem(int tempo, int velocidade) { 
            this.tempo = tempo;
            this.velocidade = velocidade;
        }
        public double Consumo() { 
            double distancia = tempo * velocidade;
            double consumo = distancia / rendimento;
            return consumo;
        }
    }
}