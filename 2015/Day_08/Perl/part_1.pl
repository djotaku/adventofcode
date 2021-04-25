#!/usr/bin/perl

use v5.14;
use warnings;

open (ALLLINES, "../input.txt") || die "couldn't find the file";

my @lines_to_test = <ALLLINES>;


my $raw_line_length = 0;
my $cleaned_line_length = 0;

for my $line (@lines_to_test){

    my $regex_length = 0;

    my $line_length = length($line);
    $raw_line_length += $line_length;
    
    my $stripped_line = substr $line, 1, -1;

    my @found_regexes = $stripped_line =~ m/(\\\\)|(\\["])|(\\x[0-9a-f]{2})/g;
    
    for my $regex (@found_regexes){
        if($regex){
            if ($regex =~ m/(\\\\)|(\\["])/){
    
                $regex_length++;
            }
            elsif ($regex =~ m/(\\x[0-9a-f]{2})/){
    
                $regex_length += 3;
            }
        }
    }
    $cleaned_line_length += $line_length - ($regex_length + 2);
}

my $subtraction = $raw_line_length - $cleaned_line_length;

say "Answer is $subtraction";
