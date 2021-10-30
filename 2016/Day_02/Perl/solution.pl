#! /usr/bin/perl

use v5.20;
use Set::Scalar;
use Switch;
use Data::Dump qw(dump);

open (INSTRUCTIONS, "../input.txt") || die "No directions!!";

my @instructions = <INSTRUCTIONS>;

my @KEYPAD_PART_1 = ([1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]);
                    
my @KEYPAD_PART_2 = ([0, 0, 1, 0, 0],
                     [0, 2, 3, 4, 0],
                     [5, 6, 7, 8, 9],
                     [0, "A", "B", "C", 0],
                     [0, 0, "D", 0, 0]);

my $VALID_KEYS_PART_1 = Set::Scalar->new('0,0', '0,1','0,2', '1,0', '1,1', '1,2', '2,0', '2,1', '2,2');

my $VALID_KEYS_PART_2 = Set::Scalar->new('0,2', '1,1', '1,2', '1,3', '2,0', '2,1', '2,2', '2,3', '2,4', '3,1', '3,2', '3,3', '4,2');

sub find_next_key{

    my $this_outer_matrix = $_[0];
    my $this_inner_matrix = $_[1];
    my $directions_this_key = $_[2];
    my $part = $_[3];
    
    my @this_keypad;
    my $this_valid_keys;
    
    if ($part == 1){
        @this_keypad = @KEYPAD_PART_1;
        $this_valid_keys = $VALID_KEYS_PART_1;
    }else{
    
        @this_keypad = @KEYPAD_PART_2;
        $this_valid_keys = $VALID_KEYS_PART_2;
    }
    foreach my $char (split //, $directions_this_key)
    {
        switch($char){
            case "U" {
                my $new_outer_matrix = $this_outer_matrix - 1;
                my $test_coordinates = "$new_outer_matrix,$this_inner_matrix";
                if ($this_valid_keys->has($test_coordinates)){ $this_outer_matrix = $new_outer_matrix;}}
            case "D" {
                my $new_outer_matrix = $this_outer_matrix + 1;
                my $test_coordinates = "$new_outer_matrix,$this_inner_matrix";
                if ($this_valid_keys->has($test_coordinates)){ $this_outer_matrix = $new_outer_matrix;}}
            case "L" {
                my $new_inner_matrix = $this_inner_matrix - 1;
                my $test_coordinates = "$this_outer_matrix,$new_inner_matrix";
                if ($this_valid_keys->has($test_coordinates)){$this_inner_matrix = $new_inner_matrix;}}
            case "R" {
                my $new_inner_matrix = $this_inner_matrix + 1;
                my $test_coordinates = "$this_outer_matrix,$new_inner_matrix";
                if ($this_valid_keys->has($test_coordinates)){$this_inner_matrix = $new_inner_matrix;}}
        }
    }
    return ($this_keypad[$this_outer_matrix][$this_inner_matrix], $this_outer_matrix, $this_inner_matrix);
}

my $part_one_inner_matrix = 1;
my $part_one_outer_matrix = 1;
my $part_one_code;

foreach my $instruction (@instructions){

    my @answer = find_next_key($part_one_outer_matrix, $part_one_inner_matrix, $instruction, 1);
    $part_one_code .= $answer[0];
    $part_one_outer_matrix = $answer[1];
    $part_one_inner_matrix = $answer[2];
}

my $part_two_inner_matrix = 1;
my $part_two_outer_matrix = 1;
my $part_two_code;

foreach my $instruction (@instructions){

    my @answer = find_next_key($part_two_outer_matrix, $part_two_inner_matrix, $instruction, 2);
    $part_two_code .= $answer[0];
    $part_two_outer_matrix = $answer[1];
    $part_two_inner_matrix = $answer[2];
}

say "We thought the code to the bathroom was $part_one_code.";
say "But the actual bathroom code turned out to be $part_two_code.";
