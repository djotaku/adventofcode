#!/usr/bin/perl

use v5.14;

use Set::Object qw(set);  # note to self: CPAN module used, so need to use in toolbox

open(EGGNOGDIRECTIONS, "../input.txt") || die "Couldn't open the egg nog directions!!!";

my $directions = <EGGNOGDIRECTIONS>;

my @directions_array = split("", $directions);

my $houses_visited = set();

my $current_house_x = 0;
my $current_house_y = 0;

$houses_visited->insert("$current_house_x, $current_house_y");

for my $direction (@directions_array){
    
    if ($direction eq "^"){
        $current_house_y++;
        $houses_visited->insert("$current_house_x, $current_house_y");
    }
    elsif ($direction eq "v"){
        $current_house_y--;
        $houses_visited->insert("$current_house_x, $current_house_y");
    }
    elsif ($direction eq "<"){
        $current_house_x--;
        $houses_visited->insert("$current_house_x, $current_house_y");
    }
    elsif ($direction eq ">"){
        $current_house_x++;
        $houses_visited->insert("$current_house_x, $current_house_y");
    }
}

print $houses_visited->size();
print " houses were visited at least once by Santa";
