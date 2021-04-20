#!/usr/bin/perl

use v5.14;
use warnings;
use List::Util qw(sum);

open(LIGHTING, <"../input.txt">) || die "Couldn't get lighting instructions!";

my @lighting_instructions = <LIGHTING>;

my %lights;

for my $instruction (@lighting_instructions){

    my ($verb, $starting_x, $starting_y, $through, $end_x, $end_y) = $instruction =~ /([a-z]* [a-z]*|[a-z]*) (\d*),(\d*)/g;
    
    my @coordinates;
    
    for (my $x = $starting_x; $x < $end_x + 1; $x++)
    {
        for (my $y= $starting_y; $y < $end_y + 1; $y++)
        {
            push(@coordinates, "($x,$y)");
        }
    }
    for my $coordinate (@coordinates)
    {
        if (exists $lights{$coordinate})
        {
            if ($verb eq "turn on")
            {
                $lights{$coordinate} += 1;
            }
            elsif ($verb eq "turn off")
            {
                if ($lights{$coordinate} > 0)
                {
                    $lights{$coordinate} -= 1;
                }
            }
            elsif ($verb eq "toggle")
            {
                $lights{$coordinate} += 2;
            }
        }
        else
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
                $lights{$coordinate} = 2;
            }
        }
    }
}

my $active_lights = sum(values %lights);

say "After translating from Ancient Nordic Elvish, I realized Santa has asked me to turn the brightness to $active_lights.";
