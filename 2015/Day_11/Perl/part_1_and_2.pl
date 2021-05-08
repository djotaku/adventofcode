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

sub rule_three{

    my $password = $_[0];
    
    my @matches = $password =~ m/(\w)\1/g;
    
    my $match_length = @matches;

    if ($match_length >= 2)
    {
        return 1;
    }
    return 0;
}

# Testing examples:
# Rule 1:
# say "TRUE!" if rule_one("hijklmmn");
# say "TRUE!" if rule_one("abbceffg");  # should be false

# Rule 2:
#say "First";
#say "TRUE!" if rule_two("hijklmmn"); # should be false
#say "Second";
#say "TRUE!" if rule_two("abbcegjk");

# Rule 3:
#say "First";
#say "TRUE!" if rule_three("abbcegjk"); # should be false
#say "Second";
#say "TRUE!" if rule_three("abbceffg");

my $current_password = "hxbxwxba";
say "Santa's starting password is: $current_password";
until (rule_one($current_password) and rule_two($current_password) and rule_three($current_password))
{
    ++$current_password;
}
say "Santa's next password should be: $current_password";
say "Now Santa's password has expired again! Oh No!";
++$current_password;
until (rule_one($current_password) and rule_two($current_password) and rule_three($current_password))
{
    ++$current_password;
}
say "Santa's next password should be: $current_password";
