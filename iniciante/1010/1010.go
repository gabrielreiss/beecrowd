package main

import (
	"fmt"
)

type cad struct {
	cod int
	num int
	vl  float64
}

func entrada() cad {
	var cod, num int
	var vl float64
	fmt.Scanf("%d %d %f\n", &cod, &num, &vl)
	return cad{cod, num, vl}
}

func Total(cad1 cad, cad2 cad) float64 {
	total := float64(cad1.num)*cad1.vl + float64(cad2.num)*cad2.vl
	return total
}

func main() {

	cad1 := entrada()
	cad2 := entrada()

	total := Total(cad1, cad2)

	fmt.Printf("VALOR A PAGAR: R$ %.2f\n", total)
}
