#! /usr/bin/perl

use v5.20;

open (TRIANGLES, "../input.txt") || die "No triangles!";

my @potential_triangles = <TRIANGLES>;

sub is_it_a_triangle{

    my $side_1 = $_[0];
    my $side_2 = $_[1];
    my $side_3 = $_[2];
    
    if (($side_1 + $side_2 > $side_3) && ($side_2 + $side_3 > $side_1) && ($side_1 + $side_3 > $side_2)){
        return 1;
    }
    return 0;
}

my $part_one_count = 0;
my $part_two_count = 0;

foreach my $triple (@potential_triangles){
    my @useful_triple = split(" ", $triple);
    $part_one_count += is_it_a_triangle($useful_triple[0], $useful_triple[1], $useful_triple[2]);
}

say "If we are looking across rows, we have $part_one_count triangles.";
