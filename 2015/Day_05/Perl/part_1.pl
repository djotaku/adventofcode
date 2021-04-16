#!/usr/bin/perl

use v5.14;
use warnings;

open(NAUGHTY_OR_NICE, <"../input.txt">) || die "Couldn't open that list!";

my @naughty_or_nice_list = <NAUGHTY_OR_NICE>;

my $nice_count = 0;

for my $line (@naughty_or_nice_list){
    
    my $vowel_count = 0;
    
    while ($line =~ m/[aeiou]/g)
    {
        $vowel_count++;
    }
    
    if ($vowel_count >= 3 && $line =~ /(.)\1/ && $line !~ /ab|cd|pq|xy/)
    {
    	$nice_count++;
    }
}

say "Santa has $nice_count nice kids to deliver presents to."
