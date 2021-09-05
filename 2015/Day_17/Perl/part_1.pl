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
	say $number;
	my $permutations = combinations(\@container_sizes, $number);
	while (my $combination = $permutations->next)
	{
		say "A combination";
		dump(@$combination);
		if(sum(@$combination) == $CONTAINER_SUM)
		{
			push @all_ways, \@$combination;
		}	
	# dump(@all_ways);
	say "size " . scalar @all_ways;
	say "----------";
	}
}
my $combo_numbers = scalar @all_ways;
print "The number of combinations for using my contains is $combo_numbers";
