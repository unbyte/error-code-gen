package main

import (
	"encoding/csv"
	"os"
	"path/filepath"
	"strconv"
	"strings"
	"text/template"
)

type Record struct {
	Code int
	En   string
	Zh   string
}

type handler struct {
	Records []Record
}

func newHandler() handler {
	return handler{Records: make([]Record, 0, 20)}
}

func (h *handler) read(path string) error {
	file, err := os.Open(path)
	if err != nil {
		return err
	}
	defer file.Close()
	reader := csv.NewReader(file)
	reader.LazyQuotes = true
	data, err := reader.ReadAll()
	if err != nil {
		return err
	}
	for _, row := range data {
		if row[2] != "" && row[3] != "" && row[4] != "" {
			if code, err := strconv.Atoi(row[2]); err == nil {
				h.Records = append(h.Records, Record{
					Code: code,
					En:   strings.TrimSpace(row[3]),
					Zh:   strings.TrimSpace(row[4]),
				})
			}
		}
	}
	return nil
}

func (h *handler) render(templatePath, outputPath string) error {
	t, err := template.ParseFiles(templatePath)
	if err != nil {
		return err
	}
	if err = os.MkdirAll(filepath.Dir(outputPath), os.ModePerm); err != nil {
		return err
	}
	file, err := os.Create(outputPath)
	defer file.Close()
	if err != nil {
		return err
	}
	return t.Execute(file, h.Records)
}
