#!/usr/bin/perl

use v5.20;
use warnings;
use Algorithm::Permute;
use List::Util qw(max);

sub parse_connections {

    my $lines = $_[0];   # just doing this for a friendly name
    my %guest_dict;
    foreach my $line (@$lines){
    
    my @preference_parse = $line =~ m/(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)\./g;
    
    my $number = "-$preference_parse[2]" if $preference_parse[1] == "lose" else $preference_parse[2]
    
    $guest_dict{$preference_parse[0]}{$preference_parse[3]} = $number;
    }
    return %guest_dict;
}

sub create_matrix{

    my %guest_dict = %{$_[0]};
    
    my @guest_dict_keys = (sort keys %guest_dict);
    
    my %index_dictionary = %guest_dict_keys[0..$#guest_dict_keys];
    
    my @matrix;
    
    my $index_dictionary_size = keys %index_dictionary;
    
    for(my $first_number = 0; $first_number < $index_dictionary_size; $first_number++)
    {
        my @temp_internal_list;
        
        my $current_city = $index_dictionary{$first_number};
        
        for (my $second_number = 0; $second_number < $index_dictionary_size; $second_number++)
        {
            if ($second_number == $first_number)
            {
                push(@temp_internal_list, 0);
            }
            else
            {
            push(@temp_internal_list, int($guest_dict{$current_city}{$index_dictionary{$second_number}}));
            }        
        }
        push(@matrix, \@temp_internal_list);
    }    
    return @matrix;
}

sub guest_happiness_maximizer{

    my ($graph, $starting_person, $number_of_people) = @_;  # later need to refer to $graph as @$graph or $$graph for a single value
    
    my @vertex;
    
    for my $number (0..($number_of_people-1)){
        if ($number != $starting_person){
            push(@vertex, $number);
        }
    }
    my $max_happiness = 0;
    
    my $vertix_iterator = Algorithm::Permute->new(\@vertex);
    
    while (my @perm = $vertix_iterator->next)
    {
        my $current_path_weight = 0;
        
        # compute path weight
        my $outer_array_index = $starting_person;
        
        for my $inner_array_index (@perm)
        {
            $current_path_weight += $$graph[$outer_array_index][$inner_array_index];
            $current_path_weight += $$graph[$inner_array_index][$outer_array_index];
            $outer_array_index = $inner_array_index;
        }
        $current_path_weight += $$graph[$outer_array_index][$starting_person];
        $current_path_weight += $$graph[$starting_person][$outer_array_index];
        
        $max_happiness = max($max_happiness, $current_path_weight);
    
    }
    return $max_happiness;
}

open(HAPPINESSPREFERENCELIST, "../input.txt") || die "Couldn't find it!!!";

my @full_set = <HAPPINESSPREFERENCELIST>;
my %guest_preference_hash = &parse_connections(\@full_set);
my @guest_preference_matrix = create_matrix(\%guest_preference_hash);
my $guest_preference_matrix_size = @guest_preference_matrix;
my $maximum_seating_happiness = guest_happiness_maximizer(\@guest_preference_matrix, 0, $guest_preference_matrix_size);
say "With this seating arrangement, the happiness level is $maximum_seating_happiness.";
