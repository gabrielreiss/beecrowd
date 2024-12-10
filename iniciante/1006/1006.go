package main

import (
	"fmt"
)

func Media(a float64, b float64, c float64) float64 {
	return (a*2 + b*3 + c*5) / 10
}

func main() {
	var a, b, c float64
	fmt.Scan(&a)
	fmt.Scan(&b)
	fmt.Scan(&c)
	fmt.Printf("MEDIA = %.1f\n", Media(a, b, c))
}
