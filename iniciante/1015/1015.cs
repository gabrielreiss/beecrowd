using System;

class URI
{

    static void Main(string[] args)
    {

        /**
        Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgul
         */

        var valores1Str = Console.ReadLine();
        var valores2Str = Console.ReadLine();
        Pontos pontos = new Pontos(
            float.Parse(valores1Str.Split(' ')[0]),
            float.Parse(valores1Str.Split(' ')[1]),
            float.Parse(valores2Str.Split(' ')[0]),
            float.Parse(valores2Str.Split(' ')[1])
            );

        Console.WriteLine("{0:F4}",pontos.Distancia());
        Console.ReadLine();
    }
    class Pontos 
    {
        public double x1 { get; set; }
        public double y1 { get; set; }
        public double x2 { get; set; }
        public double y2 { get; set; }

        public Pontos(double x1, double y1, double x2, double y2)
        {
            this.x1 = x1;
            this.y1 = y1;
            this.x2 = x2;
            this.y2 = y2;
        }
        public double Distancia() 
        {
            return Math.Sqrt(Math.Pow(x2 - x1,2) + Math.Pow(y2 - y1,2));
        }
    }
}