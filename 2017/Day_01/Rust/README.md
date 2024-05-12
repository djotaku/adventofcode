# What I learned about Rust from this day's problem
    
## Part 1
- if you have a str and want to get characters out of it, you can use .chars() it's like .iter, but beware that if you have UTF-8, you might not get what you expect.    
- collect allows you to transform one type of iterator into another
- because rust wants to be safe, if something like a type conversion might not work, to turn an Option<T> into T youneed you use unwrap_or()
- for some reason getting the last element of an array requires an unwrap (why might there not be a last element?)
## Part 2
    
