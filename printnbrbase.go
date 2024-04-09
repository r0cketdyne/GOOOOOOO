package piscine

import (
	"github.com/01-edu/z01"
)

func PrintNbrBase(nbr int, base string) {
	if len(base) < 2 {
		z01.PrintRune(rune('N'))
		z01.PrintRune(rune('V'))
		return
	}

	for i := 0; i < len(base); i++ {
		if rune(base[i]) == rune('-') || rune(base[i]) == rune('+') {
			z01.PrintRune(rune('N'))
			z01.PrintRune(rune('V'))
			return
		}
		count := 0
		for i2 := 0; i2 < len(base); i2++ {
			if base[i] == base[i2] {
				count++
			}
		}
		if count > 2 {
			z01.PrintRune(rune('N'))
			z01.PrintRune(rune('V'))
			return
		}
	}

	store := 0
	isneg := false
	if nbr == 0 {
		z01.PrintRune(rune(base[0]))
	}
	if nbr < 0 {
		isneg = true
		if nbr < -100000000000 {
			store += 1
			nbr += 1

		}
		nbr = -nbr
	}
	if isneg == true {
		z01.PrintRune(rune('-'))
	}

	result := ""
	for nbr > 0 {
		result = string(base[nbr%len(base)]) + result
		nbr /= len(base)
		if store > 0 {
			nbr += 1
			store -= 1
		}
	}
	for i := 0; i < len(result); i++ {
		z01.PrintRune(rune(result[i]))
	}
}
