#! /usr/bin/perl

use v5.20;

open (CAPTCHA, "../input.txt") || die "No captcha!";

my $captcha = <CAPTCHA>;

my @double_numbers = $captcha =~ /(\d)(?=\1)/g;

my $number_sum = 0;

foreach my $number (@double_numbers){

    $number_sum += $number;

}

my @numberlist = split('', $captcha);

if (@numberlist[0] == @numberlist[-1]){

    $number_sum += @numberlist[0];

}

say "Part 1 captcha is $number_sum";

$number_sum = 0;

my $lookahead = (scalar @numberlist) / 2;

my $index = 0;

foreach my $number (@numberlist){

    my $check = ($index + $lookahead) % (scalar @numberlist);
    
    if ($number == @numberlist[$check]){
    
        $number_sum += $number;
    
    }
    
    $index++;

}

say "Part 2 captcha is $number_sum";
