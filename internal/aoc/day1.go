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
	gap := MAX - MIN + 1

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

		switch scanner.Text()[0] {
		case 'R':
			counter = (counter + int(value)) % gap
			slog.Debug(fmt.Sprintf("Spinning right %d to %d", value, counter))
		case 'L':
			counter = (counter - int(value)) % gap
			if counter < MIN {
				counter = gap + counter
			}
			slog.Debug(fmt.Sprintf("Spinning left %d to %d", value, counter))
		default:
			slog.Error("Day 1 - Puzzle 1: Improper Read")
			return
		}

		if counter == 0 {
			zeroes += 1
			slog.Debug("Day 1 - Puzzle 1: Got a zero!")
		}
	}

	slog.Info(fmt.Sprintf("Day 1 - Puzzle 1 result: %d", zeroes))
}
