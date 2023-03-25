# Day 1: Chronal Calibration

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2018/day/1).

## Part 1
Answer: 516
## Part 2
Answer: 

## Commentary / Approach to the Problem
### Part 1
Part 1 seems relatively easy. Seems like we should just be able to do a sum (reductio) on the array.
### Part 2
My initial guess is that this isn't too hard, but it does require a bit more to it. I have to keep looping over my array until I get to a sum I've seen before. 

Go doesn't have sets built in. I ended up using sets to keep track of whether I'd seen a number before. I think the canonical way to mimic sets when you don't have them built in is to use a dictionary/hash/map? 
[This page](https://stackoverflow.com/questions/34018908/golang-why-dont-we-have-a-set-datastructure) seems to back that up. Interestingly, folks in that answer say that it's because Go doesn't have generics. More recent
versions of Go *do* have generics. So I wonder how it would be implemented now. At any rate, I intend to use a map as described in that page.
## What I Learned

### Generic

### Python
- Nothing
### Ruby

### Perl

### Go (Golang)
- since Go doesn't have sets and to not have to import a set, you can use a map[int]bool
- Go doesn't have while loops. To have an infinite loop, just put something inside for{} or, more explicitly:

```go
for ok := true; ok; ok = condition {
	work()
}
```

or

```go
for {
	work()
	if !condition {
		break
	}
}
```
### Haskell

### Rust

### Julia

### Java

### Kotlin
    