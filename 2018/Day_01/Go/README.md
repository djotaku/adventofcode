# What I learned about Go from this day's problem
    
## Part 1
- nothing
## Part 2
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