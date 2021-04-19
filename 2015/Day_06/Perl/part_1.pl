#!/usr/bin/perl

use v5.14;
use warnings;

open(LIGHTING, <"../input.txt">) || die "Couldn't get lighting instructions!";

my @lighting_instructions = <LIGHTING>;

my %lights;

for my $instruction (@lighting_instructions){

    my ($verb, $starting_x, $starting_y, $through, $end_x, $end_y) = $instruction =~ /([a-z]* [a-z]*|[a-z]*) (\d*),(\d*)/g;
    
    

}
