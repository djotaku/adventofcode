#!/usr/bin/perl

use v5.20;
use  Data::Dump qw/dump/;


my $PRESENTS_DELIVERED = 34000000;

my @house_array;

for (my $i=1; $i< ($PRESENTS_DELIVERED/10); $i+=1)
{
	for (my $j=$i; $j< ($PRESENTS_DELIVERED/10); $j += $i)
	{
		$house_array[$j] += $i * 10;
	}
}

while (my ($house_number, $house) = each @house_array)
{
    if ($house >= $PRESENTS_DELIVERED)
    {
        say "House is $house_number";
        last;
    }
}
