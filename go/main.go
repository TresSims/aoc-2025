package main

import (
	"flag"
	"log/slog"
	"os"
	"tsims-aoc/internal/aoc"
)

func main() {

	debug := flag.Bool("debug", false, "Debug logs")
	flag.Parse()

	if *debug {
		opts := &slog.HandlerOptions{
			Level: slog.LevelDebug,
		}
		handler := slog.New(slog.NewTextHandler(os.Stdout, opts))
		slog.SetDefault(handler)
	}

	for _, fn := range aoc.Solutions {
		fn()
	}
}
