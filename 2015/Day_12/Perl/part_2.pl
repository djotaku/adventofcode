#!/usr/bin/perl

use JSON::PP;
use Scalar::Util qw(looks_like_number);
use v5.20;
use warnings;

sub json_sums{
    my $summation = 0;
    my $json_item = $_[0];
    if (ref($json_item) eq "ARRAY"){
        for my $item (@{$json_item}){
            $summation += json_sums($item);
        }
    }
    elsif (looks_like_number($json_item)){
        return $json_item;
    }
    elsif (ref($json_item) eq "HASH"){
        my @values = (values %{$json_item});
        for my $value (@values){
            if ($value eq "red"){
                return 0;
            }
        }
        for my $value (@values){
            if (looks_like_number($value)){
                $summation += $value;
            }
            elsif (ref($value) eq "ARRAY"){
                $summation += json_sums($value);
            }
            elsif (ref($value) eq "HASH"){
                $summation += json_sums($value);
            }
            else{
                $summation += 0;
            }
        }
    }
    return $summation;
}

open(ELFJSON, "../input.txt") || die "NO ELF JSON!";

my $elf_json = decode_json <ELFJSON>;

# test
# say "Array!" if ref($elf_json) eq 'ARRAY';
# say "Hash!" if ref($elf_json) eq 'HASH';

my $final_sum = json_sums($elf_json);

say "The total is $final_sum";
