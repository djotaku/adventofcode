#!/usr/bin/perl

use v5.14;
use warnings;

open(LIGHTING, <"../input.txt">) || die "Couldn't get lighting instructions!";

my @lighting_instructions = <LIGHTING>;

my %lights;

for my $instruction (@lighting_instructions){

    my ($verb, $starting_x, $starting_y, $through, $end_x, $end_y) = $instruction =~ /([a-z]* [a-z]*|[a-z]*) (\d*),(\d*)/g;
    
    my @coordinates = [];
    
    for (my $x = $starting_x; $x < $end_x + 1; $x++)
    {
        for (my $y= $starting_y; $y < $end_y + 1; $y++)
        {
            push(@coordinates, "($x,$y)");
        }
    }
    for my $coordinate (@coordinates)
    {
        if ($verb eq "turn on")
        {
            $lights{$coordinate} = 1;
        }
        elsif ($verb eq "turn off")
        {
            $lights{$coordinate} = 0;
        }
        elsif ($verb eq "toggle")
        {
            if (exists $lights{$coordinate})
            {
                $lights{$coordinate} ^= 1;
            }
            else
            {
                $lights{$coordinate} = 1;
            }
        }
        else
        {
            say "I should never get here.";
        }
    }
}

my $active_lights = 0;
for my $value (values %lights)
{
    $active_lights += $value;
}

say "Santa has asked me to turn on $active_lights lights.";
