package main

import (
	"fmt"
	"math"
)

func main() {
	var raio, circulo float64

	fmt.Scanf("%f", &raio)

	circulo = math.Pi * math.Pow(raio, 2)

	fmt.Printf("A=%.4f\n", circulo)
}
