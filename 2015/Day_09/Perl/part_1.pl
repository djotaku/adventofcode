#!/usr/bin/perl

use v5.20;
use warnings;

sub parse_connections {

    my $lines = $_[0];   # just doing this for a friendly name
    my %hamilton_dict;
    foreach my $line (@$lines){
    
    my @destinations = $line =~ m/(\w+) to (\w+) = (\d+)/g;
    
    $hamilton_dict{$destinations[0]}{$destinations[1]} = $destinations[2];
    $hamilton_dict{$destinations[1]}{$destinations[0]} = $destinations[2];
    }
    
    return %hamilton_dict;
}

sub create_matrix{

    my %city_dict = %{$_[0]};
    
    my @city_dict_keys = (sort keys %city_dict);
    
    my %index_dictionary = %city_dict_keys[0..$#city_dict_keys];
    
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
            
            push(@temp_internal_list, int($city_dict{$current_city}{$index_dictionary{$second_number}}));
            
            }
        
        }
        push(@temp_internal_list, 0);
        push(@matrix, \@temp_internal_list);
    }
    my @final_zeroes = (0) x ($index_dictionary_size + 1);
    push(@matrix, \@final_zeroes);
    
    return @matrix;
}


sub traveling_salesman{

    

}

my @full_set = ("London to Dublin = 464", "London to Belfast = 518", "Dublin to Belfast = 141");

my %city_connection_hash = &parse_connections(\@full_set);

say $city_connection_hash{"London"}{"Dublin"};

my @city_matrix = create_matrix(\%city_connection_hash);

