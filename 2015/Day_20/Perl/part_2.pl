#!/usr/bin/perl

use v5.20;
use  Data::Dump qw/dump/;


my $PUZZLE_INPUT = 34000000;

my $house_number = 786240;

my $presents_delivered = 0;

while ($presents_delivered < $PUZZLE_INPUT){

    my $presents_at_this_house = 0;
    for my $elf (1..51)
    {
        if ($house_number % $elf == 0)
        {
            $presents_at_this_house += $house_number / $elf;
        }
    }
    $presents_delivered = 11 * $presents_at_this_house;
    $house_number += 1;
}

$house_number -= 1;

say "The lowest house number is $house_number";
