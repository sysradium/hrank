package main

import "fmt"

type QuickFind struct {
	arr []int
}

func (q *QuickFind) Union(i, j int) {
	p1 := q.arr[i]
	p2 := q.arr[j]

	for k := 0; k < len(q.arr); k++ {
		if q.arr[k] == p2 {
			q.arr[k] = p1
		}
	}
}

func (q *QuickFind) AreConnected(i, j int) bool {
	return q.arr[i] == q.arr[j]
}

func (q *QuickFind) Elements() []int {
	return q.arr
}

func newQuickFind(n int) *QuickFind {
	arr := make([]int, n)

	for i := 0; i < len(arr); i++ {
		arr[i] = i
	}

	a := QuickFind{arr: arr}
	return &a
}

func main() {
	var N, I int
	fmt.Scanf("%d %d", &N, &I)

	finder := newQuickFind(N)

	for i := 0; i < N; i++ {
		var p1, p2 int
		fmt.Scanf("%d %d", &p1, &p2)
		finder.Union(p1, p2)
	}

	counter := 0
	elements := finder.Elements()

	fmt.Print(elements)

	for i := 0; i < N; i++ {
		for j := i + 1; j < N; j++ {
			if elements[i] != elements[j] {
				counter++
			}
		}
	}
	fmt.Println(counter)
}
