using System;

class URI {
    static void Main (string[] args)    {
        var valores_str = Console.ReadLine();
        var valores = new Corrida(
            int.Parse(valores_str.Split(' ')[0]),
            int.Parse(valores_str.Split(' ')[1])
        );
        Console.WriteLine(valores.PontoTermino());
    }

    public class Corrida    {
        public int distancia {get; set;}
        public int comprimento {get; set;}

        public Corrida(int distancia, int comprimento){
            this.distancia = distancia;
            this.comprimento = comprimento;
        }

        public int PontoTermino(){
            return distancia % comprimento;
        }
    }
}