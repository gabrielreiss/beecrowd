package main

import (
	"fmt"
)

func main() {
	var nome string
	var sal, vendas float64

	fmt.Scan(&nome)
	fmt.Scan(&sal)
	fmt.Scan(&vendas)

	total := sal + vendas*.15

	fmt.Printf("TOTAL = R$ %.2f\n", total)
}
