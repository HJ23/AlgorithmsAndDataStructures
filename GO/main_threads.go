package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

func apiCall(input int) string {
	rand.Seed(time.Now().UnixNano())
	time.Sleep(time.Second * time.Duration(2))
	return fmt.Sprintf("Ok! --> %d", input)
}

func threadWrapper(inputs []int, results chan string, wg *sync.WaitGroup) {
	for _, input := range inputs {
		results <- apiCall(input)
	}
	wg.Done()
}

func main() {

	inputs := []int{}

	for x := 0; x < 12; x++ {
		inputs = append(inputs, x)
	}

	threads := 3
	coeff := int(len(inputs) / threads)

	results := make(chan string, len(inputs)-6)

	start := time.Now()

	var wg sync.WaitGroup

	wg.Add(threads)

	for x := 0; x < threads; x++ {
		go threadWrapper(inputs[x*coeff:(x+1)*coeff], results, &wg)
	}

	final := []string{}

	for x := 0; x < len(inputs); x++ {
		result := <-results
		final = append(final, result)
	}

	close(results)

	wg.Wait()

	fmt.Println("#Ellapsed time : ", time.Since(start))

	for _, x := range final {
		fmt.Println(x)
	}

}
