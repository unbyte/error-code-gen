package main

import (
	"flag"
	"fmt"
	"os"
)

var (
	templatePath string
	inputPath    string
)

func init() {
	flag.StringVar(&templatePath, "t", "", "path of the template to be used.")
	flag.StringVar(&templatePath, "template", "", "path of the template to be used.")
	flag.StringVar(&inputPath, "i", "", "path of the template to be used.")
	flag.StringVar(&inputPath, "input", "", "path of the template to be used.")
	flag.Usage = usage
}

func main() {
	flag.Parse()
	outputPath := flag.Arg(0)
	if outputPath == "" {
		fmt.Println("Argument Error: missing output path.")
		os.Exit(1)
	}
	h := newHandler()
	if err := h.read(inputPath); err != nil {
		fmt.Printf("Read Error: %v\n", err)
		os.Exit(1)
	}
	if err := h.render(templatePath, outputPath); err != nil {
		fmt.Printf("Render Error: %v\n", err)
		os.Exit(1)
	}
}

func usage() {
	fmt.Printf(`usage: error-code-gen -i INPUT -t TEMPLATE OUTPUT

  -i, --input string
        path of the template to be used.
  -t, --template string
        path of the template to be used.
  output
        path of the rendered file.

`)
}
