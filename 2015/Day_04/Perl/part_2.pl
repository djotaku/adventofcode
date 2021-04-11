#!/usr/bin/perl

use v5.14;

use Digest::MD5 qw(md5_hex);

my $puzzle_input = "iwrupvqb";

my $number = 0;

my $hex_test = md5_hex("$puzzle_input$number");

until ($hex_test =~ /^000000/){

	$number++;
	$hex_test = md5_hex("$puzzle_input$number");
}

say "Santa's magic number is $number";
