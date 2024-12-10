using System;

class URI
{

    static void Main(string[] args)
    {

        /**
        Dois carros (X e Y) partem em uma mesma direção. O carro X sai com velocidade constante de 60 Km/h e o carro Y sai com velocidade constante de 90 Km/h.

        Em uma hora (60 minutos) o carro Y consegue se distanciar 30 quilômetros do carro X, ou seja, consegue se afastar um quilômetro a cada 2 minutos.

        Leia a distância (em Km) e calcule quanto tempo leva (em minutos) para o carro Y tomar essa distância do outro carro.
         */
        int distancia = int.Parse(Console.ReadLine());
        Carro carroX = new Carro(60);
        Carro carroY = new Carro(90);
        CarroCompara compara = new CarroCompara(carroX, carroY);

        Console.WriteLine($"{compara.Distancia(distancia)} minutos");

    }

    class Carro
    {
        public double velocidade { get; set; }

        public Carro(int velocidade)
        {
            this.velocidade = velocidade;
        }
    }
    class CarroCompara
    {
        private Carro carro1 { get; set; }
        private Carro carro2 { get; set; }

        public CarroCompara(Carro carro1, Carro carro2)
        {
            this.carro1 = carro1;
            this.carro2 = carro2;
        }

        public double Distancia(double distancia) {
            
            double resultado = distancia / (carro2.velocidade - carro1.velocidade) * 60;

            return resultado;
        }
    }
}