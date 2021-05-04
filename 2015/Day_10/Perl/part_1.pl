#!/usr/bin/perl

use v5.20;
use warnings;

use Array::GroupBy qw(igroup_by);

sub look_and_say_round{

    my $game_input = $_[0];
    
    my @numbers = split("", $game_input);

    my $number_iterator = igroup_by(data => \@numbers, compare => sub{$_[0] eq $_[1]},);
    
    my $look_and_say_text = '';
    
    while (my $grouped_array = $number_iterator->())
    {
    
        my $length = @{$grouped_array};
        my $number = @{$grouped_array}[0];
        $look_and_say_text = $look_and_say_text . "$length$number";
    }
    
    return $look_and_say_text;
}

my $puzzle_input = "1321131112";
my $loop_count = 0;
my $puzzle_output;

until ($loop_count == 40){

    $puzzle_output = look_and_say_round($puzzle_input);
    $puzzle_input = $puzzle_output;
    $loop_count++;

}

my $output_length = length($puzzle_output);

say "The final number is $puzzle_output with a length of $output_length";
