package main

import (
	"fmt"
)

func media(a float64, b float64, pesos []float64) float64 {
	return (a*pesos[0] + b*pesos[1]) / (pesos[0] + pesos[1])
}

func main() {
	var a, b float64

	pesos := []float64{3.5, 7.5}

	fmt.Scan(&a)
	fmt.Scan(&b)

	x := media(a, b, pesos)

	fmt.Printf("MEDIA = %.5f\n", x)
}
