package main

import (
	"fmt"
)

func main() {
	var n, r int

	fmt.Scan(&n)

	r = ((n + 1) * (n + 2)) / 2

	fmt.Println(r)
}
