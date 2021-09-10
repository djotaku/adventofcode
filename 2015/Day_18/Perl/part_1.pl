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

sub new_status
{

    my $x = $_[0];
    my $y = $_[1];
    my %board = $_[2];

    my $live_neighbors = 0;
    my $alive = $board{"($x, $y)"};
    my $minus_x = $x - 1;
    my $plus_x = $x + 1;
    my $minux_y = $y -1;
    my $plus_y = $y +1;
    if ($board{"($minus_x, $minux_y)"})
    {
        $live_neighbors += 1;
    }
    if ($board{"($x, $minux_y)"})
    {
        $live_neighbors += 1;
    }
    if ($board{"($plus_x, $minux_y)"})
    {
        $live_neighbors += 1;
    }
    if ($board{"($plus_x, $y)"})
    {
        $live_neighbors += 1;
    }
    if ($board{"($plus_x, $plus_y)"})
    {
        $live_neighbors += 1;
    }
    if ($board{"($x, $plus_y)"})
    {
        $live_neighbors += 1;
    }
    if ($board{"($minus_x, $minux_y)"})
    {
        $live_neighbors += 1;
    }
    if ($board{"($minus_x, $y)"})
    {
        $live_neighbors += 1;
    }
    if ($alive)
    {
        if (2<= $live_neighbors <=3)
        {
            return 1;
        }
        else
        {
            return 0;
        }
        
    }
    if (not $alive and $live_neighbors == 3)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

## Test for when I return to this
my $number_as_string = 1;
say $number_as_string;
say "$number_as_string";
say "$number_as_string" + 1;
my $coordinates = "(0, 2)";
my ($x, $y) = $coordinates =~ /(\d+), (\d+)/g;  # <- use this to pull out the coords for the coord math in new_status sub
say "x is $x and y is $y";
