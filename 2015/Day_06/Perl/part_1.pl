#!/usr/bin/perl

use v5.14;
use warnings;

open(LIGHTING, <"../input.txt">) || die "Couldn't get lighting instructions!";

my @lighting_instructions = <LIGHTING>;

my %lights;

for my $instruction (@lighting_instructions){

    my @regex = $instruction =~ /([a-z]* [a-z]*|[a-z]*) (\d*),(\d*)/g;
    
    say @regex

}
