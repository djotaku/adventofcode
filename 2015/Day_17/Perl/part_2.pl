#!/usr/bin/perl

use v5.20;                                                                                     
use warnings;                                                                                  
use List::Util qw/sum/;
use  Data::Dump qw/dump/; 
use Algorithm::Combinatorics qw(combinations);


open(CONTAINER_SIZES, "../input.txt") || die "No containers!";

my @container_sizes = <CONTAINER_SIZES>;
# my @container_sizes = (20, 15, 10, 5, 5);
# my @container_sizes = ("20\n", "15\n", "10\n", "5\n", "5\n");


my $CONTAINER_SUM = 150;

my @all_ways;

my $size_all_ways = scalar @container_sizes;

foreach my $number (1.. $size_all_ways)
{
	my $permutations = combinations(\@container_sizes, $number);
	while (my $combination = $permutations->next)
	{
		if(sum(@$combination) == $CONTAINER_SUM)
		{
			push @all_ways, \@$combination;
		}	
	}
}

say "Done creating the containers from part 1....";

my $minimum_number_of_containers = 99999999999999999999;

foreach my $combination (@all_ways)
{
    if (scalar @$combination < $minimum_number_of_containers)
    {
        $minimum_number_of_containers = scalar @$combination;
    }
}

my @final_combinations;

foreach my $combination (@all_ways)
{
    if (scalar @$combination == $minimum_number_of_containers)
    {
        push @final_combinations,\@$combination;
    }
}

my $combo_numbers = scalar @final_combinations;
print "The number of minimum combinations for using my contains is $combo_numbers";
