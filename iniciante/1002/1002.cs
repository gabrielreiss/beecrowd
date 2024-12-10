using System; 

class URI {

    static void Main(string[] args) { 

        double pi = 3.14159;

        double raio = float.Parse(Console.ReadLine());

        double area = pi * Math.Pow(raio, 2);

        Console.WriteLine("A={0:F4}",area);
    }

}