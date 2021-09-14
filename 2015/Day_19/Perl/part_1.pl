#!/usr/bin/perl

use v5.20;
use warnings;
use  Data::Dump qw/dump/;
use Set::Scalar;


open(MOLECULE_INFO, "../input.txt") || die "Couldn't get molecule info!";

my @molecule_info = <MOLECULE_INFO>;
# test
#my @molecule_info = ("H => HO", "H => OH", "O => HH", "", "HOH");

my $molecule_to_change = pop @molecule_info;

# debug
# say $molecule_to_change;

# an extra pop to remove the blank line
pop @molecule_info;

my @list_of_molecule_conversions;

foreach my $molecule_conversion (@molecule_info)
{
    my @one_molecule_conversion = $molecule_conversion =~ m/(\w+) => (\w+)/g;
    push @list_of_molecule_conversions, \@one_molecule_conversion;
}

# debug
# dump @list_of_molecule_conversions;

my @new_molecules;

foreach my $current_conversion (@list_of_molecule_conversions)
{
    while ($molecule_to_change =~ /@$current_conversion[0]/g)
    {
        my $change_me = $molecule_to_change;
        my $result = substr $change_me, $-[0], length(@$current_conversion[0]), @$current_conversion[1];
        push @new_molecules, $change_me;
    }
}

# debug
# dump @new_molecules;

my $distinct_molecules = Set::Scalar->new(@new_molecules);

my $distinct_molecules_size = $distinct_molecules->size;

say "We have $distinct_molecules_size distinct molecules";
