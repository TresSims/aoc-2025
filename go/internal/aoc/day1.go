package aoc

import (
	"bufio"
	"fmt"
	"log"
	"log/slog"
	"os"
	"strconv"
)

const MIN int = 0
const MAX int = 99
const START int = 50

var zeroes int = 0

func init() {
	Solutions = append(Solutions, dayOne)

}

func dayOne() {

	counter := START

	f, err := os.Open("inputs/day1.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		value, err := strconv.ParseInt(scanner.Text()[1:], 10, 0)
		if err != nil {
			log.Fatal(err)
		}
		clicks := int(value)

		switch scanner.Text()[0] {
		case 'R':
			for clicks > 0 {
				counter++
				clicks--
				if counter > MAX {
					counter = MIN
					zeroes++
				}

			}
		case 'L':
			for clicks > 0 {
				counter--
				clicks--
				if counter == MIN {
					zeroes++
				}
				if counter < MIN {
					counter = MAX
				}
			}
		default:
			slog.Error("Day 1 - Puzzle 1: Improper Read")
			return
		}

		slog.Debug(fmt.Sprintf("Zeroes: %d", zeroes))
	}

	slog.Info(fmt.Sprintf("Day 1 - Puzzle 1 result: %d", zeroes))
}
