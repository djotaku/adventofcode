#!/usr/bin/perl

use v5.14;

open(DIRECTIONS, , "../input.txt") || die "Can't open input.txt: $!\n";

my $directions = <DIRECTIONS>;

my @directions_split = split("", $directions);

my $floor = 0;
my $position = 1;
for my $direction (@directions_split){
    if ($direction eq '(')
    {
        $floor++;
    }
    elsif ($direction eq ')')
    {
        $floor--;
    }
    if ($floor == -1)
    {
        last
    }
    $position++
}

say $position;
