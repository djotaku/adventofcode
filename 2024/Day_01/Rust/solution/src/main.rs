use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use counter::Counter;

// The output is wrapped in a Result to allow matching on errors.
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
fn main() {
    // File hosts.txt must exist in the current path
    if let Ok(lines) = read_lines("../../input.txt") {
        let mut left_side: Vec<i64> = Vec::new();
        let mut right_side: Vec<i64> = Vec::new();
        // Consumes the iterator, returns an (Optional) String
        for line in lines.flatten() {
            let mut line_vals = line.split_whitespace();
            left_side.push(line_vals.next().expect("Something went wrong").parse().expect("Something else went wrong?"));
            right_side.push(line_vals.next().expect("Something went wrong").parse().expect("Something else went wrong?"));
        }
        left_side.sort();
        right_side.sort();
        let mut sum: Vec<i64> = Vec::new();
        for n in 0..left_side.len(){
            sum.push((right_side[n]-left_side[n]).abs())
        }
        let num_counts = right_side.iter().collect::<Counter<_>>();
        let mut products: Vec<i64> = Vec::new();
        for n in 0..left_side.len(){
            products.push(left_side[n]*num_counts[&left_side[n]] as i64);
        }
        println!("The total distance is {}", sum.iter().sum::<i64>());
        println!("The similarity is {}", products.iter().sum::<i64>())
    }else { println!("no input.txt") }

}
