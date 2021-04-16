#!/usr/bin/perl

use v5.14;
use warnings;

my @rule_three_checks = ('abbey', 'help', 'ch', 'pq', 'xylophone');

for my $line (@rule_three_checks){

    if ($line !~ /ab|cd|pq|xy/)
    {
        say "$line matches rule three";
    }

}
