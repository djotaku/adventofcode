#!/usr/bin/perl

use v5.20;
use warnings;
use Array::GroupBy qw(igroup_by);

sub rule_one{

    my $password = $_[0];
    
    my @password_chars = split("", $password);
    
    my $rule_one_iterator = igroup_by(data => \@password_chars, compare => sub{++$_[0] eq $_[1]},);

    while (my $group = $rule_one_iterator->())
    {
        my $length = @{$group};
        if ($length >= 3)
        {
            return 1;
        }
    }
    # if we got here, it didn't find a 3 character straight
    return 0;
}

sub rule_two{

    my $password = $_[0];
    
    $password !~ m/[iol]/
}

# Testing examples:
# Rule 1:
# say "TRUE!" if rule_one("hijklmmn");
# say "TRUE!" if rule_one("abbceffg");  # should be false

# Rule 2:
say "TRUE!" if rule_two("hijklmmn"); # should be false
say "TRUE!" if rule_two("abbcegjk");
