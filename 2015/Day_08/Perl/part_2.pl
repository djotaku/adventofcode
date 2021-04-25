#!/usr/bin/perl

use v5.14;
use warnings;

open (ALLLINES, "../input.txt") || die "couldn't find the file";

my @lines_to_test = <ALLLINES>;


my $raw_line_length = 0;
my $encoded_line_length = 0;

for my $line (@lines_to_test){

    my $regex_length = 0;

    my $line_length = length($line);
    $raw_line_length += $line_length;
    
    my @encoded_strings = $line =~ m/[\"\\]/g;
    
    my $encoded_string_count = @encoded_strings;
    
    $encoded_line_length += $line_length - ($encoded_string_count + 2);
}

my $subtraction = $raw_line_length - $encoded_line_length;

say "Answer is $subtraction";
