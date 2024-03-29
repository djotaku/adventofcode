#!/usr/bin/perl

use v5.20;
use warnings;
use  Data::Dump qw/dump/;


open(AUNT_LIST, "../input.txt") || die "No Aunt Sue!";

my @aunt_list = <AUNT_LIST>;

my %aunts;

foreach(@aunt_list)
{
    my @regex_results = $_ =~ m/Sue (\d*): (\w*): (\d*), (\w*): (\d*), (\w*): (\d*)/g;
    $aunts{$regex_results[0]} = {$regex_results[1]=>$regex_results[2],$regex_results[3]=>$regex_results[4],$regex_results[5]=>$regex_results[6]}; 
}

foreach my $key (keys %aunts)
{
    if(exists $aunts{$key}{"children"} and $aunts{$key}{"children"} != 3 )
    {
        delete $aunts{$key};
    }
    elsif(exists $aunts{$key}{"cats"} and $aunts{$key}{"cats"} <= 7 )
    {
        delete $aunts{$key};
    }
    elsif(exists $aunts{$key}{"samoyeds"} and $aunts{$key}{"samoyeds"} != 2 )
    {
        delete $aunts{$key};
    }
    elsif(exists $aunts{$key}{"pomeranians"} and $aunts{$key}{"pomeranians"} >= 3 )
    {
        delete $aunts{$key};
    }
    elsif(exists $aunts{$key}{"akitas"} and $aunts{$key}{"akitas"} != 0 )
    {
        delete $aunts{$key};
    }
    elsif(exists $aunts{$key}{"vizslas"} and $aunts{$key}{"vizslas"} != 0 )
    {
        delete $aunts{$key};
    }
    elsif(exists $aunts{$key}{"goldfish"} and $aunts{$key}{"goldfish"} >= 5 )
    {
        delete $aunts{$key};
    }
    elsif(exists $aunts{$key}{"trees"} and $aunts{$key}{"trees"} <= 3 )
    {
        delete $aunts{$key};
    }
    elsif(exists $aunts{$key}{"cars"} and $aunts{$key}{"cars"} != 2 )
    {
        delete $aunts{$key};
    }
    elsif(exists $aunts{$key}{"perfumes"} and $aunts{$key}{"perfumes"} != 1 )
    {
        delete $aunts{$key};
    }
}

dump(%aunts);

foreach my $key (keys %aunts)
{
    say $key;
}
