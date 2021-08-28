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
    my @ingredient_list = $_[1];
    
    # dump(@ingredient_list);
    # dump($teaspoon_list);
    # ungeneralizing because arrays of arrays in Perl is a real PITA
    # say "Ingredient list at 0,0: $ingredient_list[0][0]";
    my @new_ingredient_list;
    $new_ingredient_list[0][0] = @$teaspoon_list[0]*$ingredient_list[0][0][0];
    $new_ingredient_list[0][1] = @$teaspoon_list[0]*$ingredient_list[0][0][1];
    $new_ingredient_list[0][2] = @$teaspoon_list[0]*$ingredient_list[0][0][2];
    $new_ingredient_list[0][3] = @$teaspoon_list[0]*$ingredient_list[0][0][3];
    $new_ingredient_list[1][0] = @$teaspoon_list[1]*$ingredient_list[0][1][0];
    $new_ingredient_list[1][1] = @$teaspoon_list[1]*$ingredient_list[0][1][1];
    $new_ingredient_list[1][2] = @$teaspoon_list[1]*$ingredient_list[0][1][2];
    $new_ingredient_list[1][3] = @$teaspoon_list[1]*$ingredient_list[0][1][3];
    $new_ingredient_list[2][0] = @$teaspoon_list[2]*$ingredient_list[0][2][0];
    $new_ingredient_list[2][1] = @$teaspoon_list[2]*$ingredient_list[0][2][1];
    $new_ingredient_list[2][2] = @$teaspoon_list[2]*$ingredient_list[0][2][2];
    $new_ingredient_list[2][3] = @$teaspoon_list[2]*$ingredient_list[0][2][3];
    $new_ingredient_list[3][0] = @$teaspoon_list[3]*$ingredient_list[0][3][0];
    $new_ingredient_list[3][1] = @$teaspoon_list[3]*$ingredient_list[0][3][1];
    $new_ingredient_list[3][2] = @$teaspoon_list[3]*$ingredient_list[0][3][2];
    $new_ingredient_list[3][3] = @$teaspoon_list[3]*$ingredient_list[0][3][3];
    
    my $final_score = 1;
    my $property_count = 1;
    my @properties = transpose(\@new_ingredient_list); 
    #say "New ingredient list:";
    #dump(@new_ingredient_list);
    #say "Transposed";
    #dump(@properties);
    foreach(@properties)
    {
        #dump($_);
        if(sum( @$_) > 0)
        {
            #say "Am I in the first sum?";
            #say (sum @$_);
            if($property_count < 5)
            {
                #say "Am I in the second sum?";
                $final_score *= sum(@$_);
            }
        }
        $property_count += 1;
    }
    return $final_score;
}

sub count_calories{

    my $teaspoon_list = $_[0];
    my @ingredient_list = $_[1];
    my $calorie_score = 0;
    
    foreach(0 .. 3)
    {
        $calorie_score += @$teaspoon_list[$_] * $ingredient_list[0][$_][-1];
    }
    
    return $calorie_score;
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
            my $calorie_score = count_calories(\@combination, \@$ingredients);
            if (($combo_score > $score) && ($calorie_score == 500))
            {
                say $score;
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

# Test score
#ingredient_score([1,2,3], [[1,2,3],[4,5,6]]);
# the sample input
#say ingredient_score([44,56], [[-1, -2, 6,3,8],[2,3,-2,-1,3]]);


my $cookie_score = brute_force_cookie_score(\@parsed_ingredients);
#my $cookie_score = brute_force_cookie_score([[-1, -2, 6,3,8],[2,3,-2,-1,3]]);

say "The cookie score is.....";
say $cookie_score;
