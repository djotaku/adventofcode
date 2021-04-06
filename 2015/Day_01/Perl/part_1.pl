#!/usr/bin/perl

use v5.14;

open(DIRECTIONS, , "../input.txt") || die "Can't open input.txt: $!\n";

my $directions = <DIRECTIONS>;

my @directions_split = split("", $directions);

my $floor = 0;
for my $direction (@directions_split){
    say $direction;
    if ($direction eq '(')
    {
        $floor++;
    }
    elsif ($direction eq ')')
    {
        $floor--;
    }
    say $floor;
}

say $floor;
