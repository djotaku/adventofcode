#!/usr/bin/perl

use v5.14;
use warnings;

open(NAUGHTY_OR_NICE, <"../input.txt">) || die "Couldn't open that list!";

my @naughty_or_nice_list = <NAUGHTY_OR_NICE>;

my $nice_count = 0;

for my $line (@naughty_or_nice_list){
    if (my @matches = $line =~ m/[aeiou]/g >= 3 && $line =~ /(.)\1/ && $line =~ !/ab|cd|pq|xy/)
    {
	    say scalar @matches; # this outputs 1.....
    	$nice_count++;
    }
}

say "Santa has $nice_count nice kids to deliver presents to."
