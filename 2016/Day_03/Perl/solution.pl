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
my @part_2_triangle_1;
my @part_2_triangle_2;
my @part_2_triangle_3;
my $part_two_iterator = 0;

foreach my $triple (@potential_triangles){
    my @useful_triple = split(" ", $triple);
    $part_one_count += is_it_a_triangle($useful_triple[0], $useful_triple[1], $useful_triple[2]);
    $part_two_iterator += 1;
    push @part_2_triangle_1, $useful_triple[0];
    push @part_2_triangle_2, $useful_triple[1];
    push @part_2_triangle_3, $useful_triple[2];
    if ($part_two_iterator % 3 == 0){
        $part_two_count += is_it_a_triangle(pop @part_2_triangle_1, pop @part_2_triangle_1, pop @part_2_triangle_1);
        $part_two_count += is_it_a_triangle(pop @part_2_triangle_2, pop @part_2_triangle_2, pop @part_2_triangle_2);
        $part_two_count += is_it_a_triangle(pop @part_2_triangle_3, pop @part_2_triangle_3, pop @part_2_triangle_3);
    }
}

say "If we are looking across rows, we have $part_one_count triangles.";
say "If we are looking across columns, we have $part_two_count triangles.";
