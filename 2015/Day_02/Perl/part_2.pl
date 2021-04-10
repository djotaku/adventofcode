#!/usr/bin/perl

use v5.14;

open(PRESENTDIMENSIONS, , "../input.txt") || die "Can't open input.txt: $!\n";

my @present_dimension_list = <PRESENTDIMENSIONS>;

my @accumulated_lengths;

for my $present_dimension (@present_dimension_list){

    my($length, $width, $height) = $present_dimension =~ /(\d+)x(\d+)x(\d+)/;
    
    push (@accumulated_lengths, $length*$width*$height); # ribbon for bow
    
    my @temp_dimensions = sort{ $a <=> $b }($length, $width, $height);
    
    push (@accumulated_lengths, 2 * $temp_dimensions[0] + 2 * $temp_dimensions[1]);
}

# reduce is not in the standard Perl library

my $total_length = 0;
for my $length (@accumulated_lengths){
    $total_length += $length;
}

say "The Elves need $total_length feet of ribbon."
