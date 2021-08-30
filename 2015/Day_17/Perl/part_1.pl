#!/usr/bin/perl

use v5.20;                                                                                     
use warnings;                                                                                  
use List::Util qw/sum/;
use  Data::Dump qw/dump/; 
use Algorithm::Permute;


open(CONTAINER_SIZES, "../input.txt") || die "No containers!";

my @container_sizes = <CONTAINER_SIZES>;

my @all_ways;

my $size_all_ways = scalar @container_sizes;

foreach my $number (1.. $size_all_ways)
{
	say $number;
	my $permutations = Algorithm::Permute->new(\@container_sizes, $number);
	while (my @combination = $permutations->next)
	{
		say "A combination";
		dump(@combination);
		if(sum(@combination) == 150)
		{
			push @all_ways, \@combination;
		}	
	dump(@all_ways);
	say "size " . scalar @all_ways;
	say "----------";
	}
}
my $combo_numbers = scalar @all_ways;
print "The number of combinations for using my contains is $combo_numbers";
