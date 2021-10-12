#! /usr/bin/perl

use v5.20;

open (DIRECTIONS, "../input.txt") || die "No directions!!";

my $directions = <DIRECTIONS>;

my @directions = split(",", $directions);

my @direction = (0, 1);
my @location = (0, 0);
my %seen_locations;
$seen_locations{'0,0'} = 1;
my @part_two_answer = (0, 0);
my $part_two_found = 0;

foreach my $orientation_distance (@directions){

    my ($orientation, $distance) = $orientation_distance =~ /(\w)(\d+)/g;
    if ($orientation eq "L")
    {
        my $temp_0 = $direction[0];
        $direction[0] = -$direction[1];
        $direction[1] = $temp_0;
    }else
    {
        my $temp_0 = $direction[0];
        $direction[0] = $direction[1];
        $direction[1] = -$temp_0;
    }
    foreach my $step (0..($distance-1)){
        $location[0] += $direction[0];
        $location[1] += $direction[1];
        if ($seen_locations{"$location[0],$location[1]"} == 1 and $part_two_found == 0){
            $part_two_answer[0] = $location[0];
            $part_two_answer[1] = $location[1];
            $part_two_found = 1;
        }else
        {
            $seen_locations{"$location[0],$location[1]"} = 1;
        }
    }
}

my $answer_part_one = abs($location[0]) + abs($location[1]);
my $answer_part_two = abs($part_two_answer[0]) + abs($part_two_answer[1]);

say "According to part 1's instructions, Easter Bunny HQ is $answer_part_one blocks away.";
say "According to part 2's instructions, Easter Bunny HQ is $answer_part_two blocks away.";
