#!/usr/bin/perl

use v5.20;
use warnings;

use Digest::MD5 qw(md5_hex);
use Scalar::Util qw(looks_like_number);

my $puzzle_input = "ugkcyxxp";

# part one
my $part_one_answer = "";
my $number = 0;

sub part_one_hash{    
    my $hex_test = md5_hex("$puzzle_input$number");
    until ($hex_test =~ /^00000/){
        $number++;
        $hex_test = md5_hex("$puzzle_input$number");
    }
    return substr($hex_test, 5, 1);
}


for (0..7){
    $number++;
    $part_one_answer .= part_one_hash;
}

# part 2
$number = 0;
my @part_two_answer;
my $part_two_counter = 0;

sub part_two_hash{
    my $hex_test = md5_hex("$puzzle_input$number");
    until ($hex_test =~ /^00000/){
        $number++;
        $hex_test = md5_hex("$puzzle_input$number");
    }
    my $position = substr($hex_test, 5, 1);
    my $value = substr($hex_test, 6, 1);
    if (looks_like_number($position) && $position < 8){
            if (not defined $part_two_answer[$position]){
                $part_two_answer[$position] = $value;
                $part_two_counter++;
            }
    }
}

until ($part_two_counter == 8){
    $number++;
    part_two_hash;
}

my $part_two_string_answer = (join '', @part_two_answer);

say "The first door's password is: $part_one_answer";
say "The second door's password is: $part_two_string_answer";
