#!/usr/bin/perl

use v5.20;
use warnings;
use Array::Transpose;
use Algorithm::Permute;
use List::Util qw/sum/;
use Data::Dump qw/dump/;

open(COOKIE_LIST, "../input.txt") || die "No cookies!";

my @cookie_list = <COOKIE_LIST>;

sub parse_ingredients{

    my $ingredients = $_[0];
    
    my @parse_ingredients;
    
    foreach my $ingredient (@$ingredients){
    
        my @ingredient_parsed = ($ingredient =~ m/(-*\d)/g);
        #dump(@ingredient_parsed);
        push (@parse_ingredients, \@ingredient_parsed);
    }
    return @parse_ingredients;
}

sub ingredient_score{

    my $teaspoon_list = $_[0];
    my $ingredient_list = $_[1];
    
    #dump($ingredient_list);
    
    my $x = 0;
    foreach my $teaspoon (@$teaspoon_list)
    {
        foreach my $ingredient (@$ingredient_list)
        {
            say "Dumping ingredient";
            dump($ingredient);
            $ingredient *= $teaspoon;
        }
        $x += 1;
    }
    my $final_score = 1;
    my $property_count = 1;
    my @properties = transpose(\@$ingredient_list);
    foreach(@properties)
    {
        if(sum($_) > 0)
        {
            $final_score *= sum($_);
        }
        $property_count += 1;
        if($property_count ==5){
            break;
        }
    }
    return $final_score;
}


sub brute_force_cookie_score{

    my $ingredients = $_[0];
    
    #dump($ingredients);
    
    my $ingredient_combos = Algorithm::Permute->new([1..100], 4);
    my $score = 0;
    while (my @combination = $ingredient_combos->next)
    {
        if (sum(@combination) == 100)
        {
            my $combo_score = ingredient_score(\@combination, \@$ingredients);
            if ($combo_score > $score)
            {
                $score = $combo_score;
            }
        }
    }
    return $score;
}

# Test that I have the cookies
#say "Checking cookies!";
#say @cookie_list;

my @parsed_ingredients = parse_ingredients(\@cookie_list);

# Test this step
#say "Testing ingredient parsing!";
#dump(@parsed_ingredients);

my $cookie_score = brute_force_cookie_score(\@parsed_ingredients);

say "The cookie score is.....";
say $cookie_score;
