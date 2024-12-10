using System;

class URI
{

    static void Main(string[] args)
    {

        /**
        Faça um programa que leia três valores e apresente 
        o maior dos três valores lidos seguido da mensagem “eh o maior”.
         */


        var listaStr = Console.ReadLine();
        var lista = new Valores(
            int.Parse(listaStr.Split(' ')[0]),
            int.Parse(listaStr.Split(' ')[1]),
            int.Parse(listaStr.Split(' ')[2])
            );

        Console.WriteLine($"{lista.Maior()} eh o maior");
        Console.ReadLine();
    }

    class Valores
    {
        private int a { get; set; }
        private int b { get; set; }
        private int c { get; set; }

        public Valores(int a, int b, int c)
        { 
            this.a = a;
            this.b = b;
            this.c = c;
        }

        public int Maior() 
        {
            int maior = (a + b + Math.Abs(a - b)) / 2;
            maior = (maior + c + Math.Abs(maior - c)) / 2;

            return maior;
        }
    }


}