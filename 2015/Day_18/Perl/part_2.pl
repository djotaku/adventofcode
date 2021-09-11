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

#dump(%initial_board);
#my $initial_total = sum(values %initial_board);
#say "Initial total: $initial_total";

sub new_status
{

    my $x = $_[0];
    my $y = $_[1];
    my %board = @_;
    
    #dump(%board);

    my $live_neighbors = 0;
    my $alive = $board{"($x, $y)"};
    # say "Alive: $alive";
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
    if ($board{"($minus_x, $plus_y)"})
    {
        $live_neighbors += 1;
    }
    if ($board{"($minus_x, $y)"})
    {
        $live_neighbors += 1;
    }
    if ($alive)
    {
        # say "Alive is: $alive which meant true!"; 
        if (2<= $live_neighbors <=3)
        {
        # say "Live neighbors: $live_neighbors and is between 2 and 3?";
            return 1;
        }
        else
        {
            return 0;
        }
    }
    if (not $alive and $live_neighbors == 3)
    {
        # say "Alive is: $alive which meant false! and live_neighbors=$live_neighbors"; 
        return 1;
    }
    else
    {
        return 0;
    }
}

sub play_round
{
    my %original_board = @_;
    
    #dump(%original_board);
    
    my %new_board;
    foreach my $x (0..99)
    {
        foreach my $y (0..99)
        {
            $new_board{"($x, $y)"} = new_status($x, $y, %original_board);
        }
    }
    $new_board{"(0, 0)"} = 1;
    $new_board{"(0, 99)"} = 1;
    $new_board{"(99, 0)"} = 1;
    $new_board{"(99, 99)"} = 1;
    return %new_board;
}

my %final_board = %initial_board;

#say "-----------------";
#dump(%final_board);
#say "-----------------";

foreach my $round (0..99)
{
    say "Round: $round";
    %final_board = play_round(%final_board);
}

#say "-----------------";
#dump(%final_board);
#say "-----------------";

my $total = sum(values %final_board);

say "There are $total lights on.";
