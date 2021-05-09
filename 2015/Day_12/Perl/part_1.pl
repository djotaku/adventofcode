#!/usr/bin/perl

use v5.20;
use warnings;

open(CRAZYJS, '../input.txt') || die "NO INPUT!";

my @lines = <CRAZYJS>; 

my @numbers;

for my $line (@lines){

    my @line_numbers = $line =~ m/(-*\d+)/g;
    push (@numbers, @line_numbers);
}

my $total = 0;

for my $number (@numbers)
{
        $total += $number;
}

say "The number total is $total";
