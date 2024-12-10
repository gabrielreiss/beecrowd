package main

import (
	"fmt"
)

func main() {
	var n, qnt_horas int
	var vl_hora float64

	fmt.Scan(&n)
	fmt.Scan(&qnt_horas)
	fmt.Scan(&vl_hora)

	sal := float64(qnt_horas) * vl_hora

	fmt.Println("NUMBER =", n)
	fmt.Printf("SALARY = U$ %.2f\n", sal)
}
