#!/usr/bin/perl

use v5.14;

use Set::Object qw(set);  # note to self: CPAN module used, so need to use in toolbox

open(EGGNOGDIRECTIONS, "../input.txt") || die "Couldn't open the egg nog directions!!!";

my $directions = <EGGNOGDIRECTIONS>;

my @directions_array = split("", $directions);

my $houses_visited = set();

my $santa_current_house_x = 0;
my $santa_current_house_y = 0;
my $robo_santa_current_house_x = 0;
my $robo_santa_current_house_y = 0;
my $count = 0;

$houses_visited->insert("$santa_current_house_x, $santa_current_house_y");

for my $direction (@directions_array){
    
    if ($direction eq "^"){
        if ($count == 0 or $count % 2 == 0){
            $santa_current_house_y++;
            $houses_visited->insert("$santa_current_house_x, $santa_current_house_y");
        }
        else
        {
            $robo_santa_current_house_y++;
            $houses_visited->insert("$robo_santa_current_house_x, $robo_santa_current_house_y");
        }
    }
    elsif ($direction eq "v"){
        if ($count == 0 or $count % 2 == 0){
            $santa_current_house_y--;
            $houses_visited->insert("$santa_current_house_x, $santa_current_house_y");
        }
        else
        {
            $robo_santa_current_house_y--;
            $houses_visited->insert("$robo_santa_current_house_x, $robo_santa_current_house_y");
        }
    }
    elsif ($direction eq "<"){
        if ($count == 0 or $count % 2 == 0){
            $santa_current_house_x--;
            $houses_visited->insert("$santa_current_house_x, $santa_current_house_y");
        }
        else
        {
            $robo_santa_current_house_x--;
            $houses_visited->insert("$robo_santa_current_house_x, $robo_santa_current_house_y");
        }
    }
    elsif ($direction eq ">"){
        if($count == 0 or $count % 2 == 0){
            $santa_current_house_x++;
            $houses_visited->insert("$santa_current_house_x, $santa_current_house_y");
        }
        else
        {
            $robo_santa_current_house_x++;
            $houses_visited->insert("$robo_santa_current_house_x, $robo_santa_current_house_y");
        }
    }
    $count++;
}

print $houses_visited->size();
print " houses were visited at least once by Santa or Robo-Santa";
