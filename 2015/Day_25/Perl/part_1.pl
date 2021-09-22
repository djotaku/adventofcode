#! /usr/bin/perl

use v5.20;

my $row = 6;
my $col = 6;
my $code = 27995004;

while ($row != 2947 or $col != 3029)
{
    if ($row == 1)
    {
        $row = $col + 1;
        $col = 1;
    }
    else
    {
        $row = $row - 1;
        $col = $col + 1;
    }
    $code = ($code * 252533) % 33554393;
}

say "The code at row: $row, col $col is $code";
