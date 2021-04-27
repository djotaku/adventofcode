#!/usr/bin/perl

use v5.14;
use warnings;

sub parse_connections {

    my @lines = @_[0];   # just doing this for a friendly name
    my %hamilton_dict = {};
    foreach my $line (@lines){
    
    my @destinations = $line =~ m/(\w+) to (\w+) = (\d+)/g;
    
    # just for test below
    say @destinations;
    }
}

my @full_set = ["London to Dublin = 464", "London to Belfast = 518", "Dublin to Belfast = 141"];

parse_connections(@full_set);
