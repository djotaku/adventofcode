#!/usr/bin/perl

use v5.14;
use warnings;

my @rule_two_checks = ('xx', 'abcdde', 'dd', 'h');

for my $line (@rule_two_checks){

    if ($line =~ /(.)\1/)
    {
        say "$line matches rule two";
    }

}
