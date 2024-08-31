package main

import (
	"fmt"
	"sync"
	"time"
)

var rwmutex sync.Mutex
var balance int
var wg sync.WaitGroup
var once sync.Once

func increment(wg *sync.WaitGroup) {
	defer wg.Done()
	defer rwmutex.Unlock()
	rwmutex.Lock()
	balance++
}

func read(wg *sync.WaitGroup) {
	defer rwmutex.Unlock()
	defer wg.Done()
	rwmutex.Lock()
	fmt.Println("Current balance is: ", balance)
}

func main1() {
	for x := 0; x <= 10; x++ {
		wg.Add(4)
		go read(&wg)
		go read(&wg)
		go read(&wg)
		go increment(&wg)
	}
	wg.Wait()
}

func run(pool *sync.Pool, wg *sync.WaitGroup) {
	defer wg.Done()
	memoryAddress := pool.Get().(*[]int)
	//time.Sleep(time.Second)
	pool.Put(memoryAddress)
}

func main2() {

	memorySize := 0

	memoryPool := sync.Pool{New: func() any {
		memorySize++
		a := make([]int, 100)
		return &a
	}}

	wg1 := sync.WaitGroup{}
	wg1.Add(100)

	for x := 0; x < 100; x++ {
		go run(&memoryPool, &wg1)
	}

	wg.Wait()

	fmt.Println(memorySize)

}

var counter1, counter2 int

func worker1(cond *sync.Cond, wg *sync.WaitGroup) {
	defer wg.Done()
	cond.L.Lock()
	cond.Wait()
	counter1++
	fmt.Println("counter1 ->", counter1)
	cond.L.Unlock()
}

func worker2(cond *sync.Cond, wg *sync.WaitGroup) {
	defer wg.Done()
	cond.L.Lock()
	cond.Wait()
	counter2++
	fmt.Println("counter2 ->", counter2)
	cond.L.Unlock()
}

func producer(buffer chan<- int, wg *sync.WaitGroup, finish chan<- bool) {
	defer wg.Done()

	for x := 0; x < 100; x++ {
		buffer <- x
	}

	finish <- true

}

func consumer(buffer <-chan int, wg *sync.WaitGroup, finish <-chan bool) {
	for {
		select {
		case <-finish:
			wg.Done()
			return

		case a := <-buffer:
			fmt.Println(a)
		}
	}
}

func main3() {

	var wg sync.WaitGroup
	buffer := make(chan int)
	finish := make(chan bool)

	wg.Add(2)
	go producer(buffer, &wg, finish)
	go consumer(buffer, &wg, finish)
	wg.Wait()

	close(buffer)

}

func fetch() chan int {
	//time.Sleep(2 * time.Second)

	v := make(chan int)

	go func() {
		v <- 4
		close(v)
	}()

	return v
}

func dumb(c int, d int) {
	fmt.Println(c, d)
}

func main4() {

	a := fetch()
	b := fetch()
	time.Sleep(1 * time.Second)
	fmt.Println("Started")
	dumb(<-a, <-b)

}
