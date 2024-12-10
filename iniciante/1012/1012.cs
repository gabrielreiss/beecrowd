using System;

class URI
{

    static void Main(string[] args)
    {

        /**
        Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
        a) a área do triângulo retângulo que tem A por base e C por altura.
        b) a área do círculo de raio C. (pi = 3.14159)
        c) a área do trapézio que tem A e B por bases e C por altura.
        d) a área do quadrado que tem lado B.
        e) a área do retângulo que tem lados A e B.
         */

        //Console.WriteLine("Digite as informações dos pontos a, b e c");
        var pontosStr = Console.ReadLine();
        var pontos = new Pontos(
            double.Parse(pontosStr.Split(' ')[0]),
            double.Parse(pontosStr.Split(' ')[1]),
            double.Parse(pontosStr.Split(' ')[2])
            );

        Console.WriteLine("TRIANGULO: {0:F3}", pontos.Triangulo());
        Console.WriteLine("CIRCULO: {0:F3}", pontos.Circulo());
        Console.WriteLine("TRAPEZIO: {0:F3}", pontos.Trapezio());
        Console.WriteLine("QUADRADO: {0:F3}", pontos.Quadrado());
        Console.WriteLine("RETANGULO: {0:F3}", pontos.Retangulo());
        Console.ReadLine();
    }

    public class Pontos
    {

        private double a { get; set; }
        private double b { get; set; }
        private double c { get; set; }

        public Pontos(double a, double b, double c)
        {
            this.a = a;
            this.b = b;
            this.c = c;
        }

        public double Triangulo() {
            return a * c / 2;
        }

        public double Circulo() {
            double pi = 3.14159f;
            return pi * Math.Pow(c, 2);
        }

        public double Trapezio() {
            return ((a + b) * c) / 2;
        }

        public double Quadrado() {
            return Math.Pow(b, 2);
        }

        public double Retangulo() {
            return a * b;
        }
    }
}