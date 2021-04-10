#!/usr/bin/perl

use v5.14;

open(PRESENTDIMENSIONS, , "../input.txt") || die "Can't open input.txt: $!\n";

my @present_dimension_list = <PRESENTDIMENSIONS>;

my @accumulated_areas;

for my $present_dimension (@present_dimension_list){

    my($length, $width, $height) = $present_dimension =~ /(\d+)x(\d+)x(\d+)/;
    
    push (@accumulated_areas, 2*$length*$width+2*$width*$height+2*$height*$length);
    
    my @temp_dimensions = sort{ $a <=> $b }($length, $width, $height);
    
    push (@accumulated_areas, $temp_dimensions[0] * $temp_dimensions[1]);
}

# reduce is not in the standard Perl library

my $total_area = 0;
for my $area (@accumulated_areas){
    $total_area += $area;
}

say "The Elves need $total_area square feet of wrapping paper"
