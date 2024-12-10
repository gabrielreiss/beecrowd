package main

import (
	"fmt"
)

func Diferenca(a, b int, c int, d int) int {
	return a*b - c*d
}

func main() {
	var a, b, c, d int

	fmt.Scan(&a)
	fmt.Scan(&b)
	fmt.Scan(&c)
	fmt.Scan(&d)

	dif := Diferenca(a, b, c, d)

	//fmt.Printf("DIFERENCA = %d\n", dif)
	fmt.Println("DIFERENCA =", dif)
}
