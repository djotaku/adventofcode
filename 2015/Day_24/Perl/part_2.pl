#!/usr/bin/perl

use v5.20;                                                                                     
use warnings;                                                                                  
use List::Util qw/sum product min/;
use  Data::Dump qw/dump/; 
use Algorithm::Combinatorics qw(combinations);

open(PACKAGES, "../input.txt") || die "No packages";

my @packages = <PACKAGES>;
#my @packages = (1,2,3,4,5,7,8,9,10,11);

my $weight_per_section = (sum (@packages)/4);

my @package_combinations;

my $number_of_packages = scalar @packages;

foreach my $number (1.. $number_of_packages)
{
	my $permutations = combinations(\@packages, $number);
	while (my $combination = $permutations->next)
	{
		if(sum(@$combination) == $weight_per_section)
		{
			push @package_combinations, \@$combination;
		}	
	}
}

my $santa_leg_room_packages = 100000000000000000;

foreach my $package_combo (@package_combinations)
{
    $santa_leg_room_packages = min ((scalar @$package_combo), $santa_leg_room_packages);
}

my @group_1_contenders;

foreach my $package_combo (@package_combinations)
{
    if ((scalar @$package_combo) == $santa_leg_room_packages)
    {
        push @group_1_contenders, \@$package_combo;
    }
}


if (scalar @group_1_contenders == 1)
{
    my $quantum_entanglement = product @{$group_1_contenders[0]};
    say "The quantum entanglement of the packages in Santa's leg area is: $quantum_entanglement";
}
else
{
    my $quantum_entanglement = 10000000000000000000000;
    foreach my $presents (@group_1_contenders)
    {
        $quantum_entanglement = min ($quantum_entanglement, (product @{$presents}))
    }
    say "The quantum entanglement of the packages in Santa's leg area is: $quantum_entanglement";
}

