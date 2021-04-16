#!/usr/bin/perl

use v5.14;
use warnings;

my @rule_one_tests = ('aei', 'xazegov', 'aeiouaeiouaeiou', 'adey');

for my $line (@rule_one_tests){
    
    my $vowel_count = 0;
    
    while ($line =~ m/[aeiou]/g)
    {
        $vowel_count++;
    }
    
    if($vowel_count >= 3)
    {
        say "$line matches rule one";
    }

}
