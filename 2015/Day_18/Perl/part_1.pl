#!/usr/bin/perl

use v5.20;
use warnings;
use List::Util qw(sum);
use  Data::Dump qw/dump/;

open(INITIAL_BOARD, "../input.txt") || die "Couldn't get lighting instructions!";

my @initial_board = <INITIAL_BOARD>;

my %initial_board;

while(my ($row_index, $row) = each @initial_board)
{
    my @columns = split('', $row);
    while(my ($column_index, $column) = each @columns)
    {
        if ($column eq "#")
        {
            $initial_board{"($row_index, $column_index)"} = 1;
        }
    }
}

# print dump(%initial_board);

## Test for when I return to this
my $number_as_string = 1;
say $number_as_string;
say "$number_as_string";
say "$number_as_string" + 1;
my $coordinates = "(0, 2)";
my ($x, $y) = $coordinates =~ /(\d+), (\d+)/g;
say "x is $x and y is $y";
