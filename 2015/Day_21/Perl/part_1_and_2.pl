#!/usr/bin/perl

use v5.20;                                                                                                                                                          
use Data::Dump qw/dump/;
use List::Util qw/min max/;
use Math::Cartesian::Product;

my %WEAPONS = (dagger => {cost=> 8, damage=>4},
            shortsword => {cost=>10, damage=>5},
            warhammer => {cost=>25, damage=>6},
            longsword => {cost=>40, damage=>7},
            greataxe => {cost=>74, damage=>8});
            
my %ARMOR = (leather=> {cost=>13, armor=>1},
            chainmail=> {cost=>31, armor=>2},
            splintmail=> {cost=>53, armor=>3},
            bandedmail=> {cost=>75, armor=>4},
            platemail=> {cost=>102, armor=>5},
            nomail=> {cost=>0, armor=>0});
            
my %RINGS = (damage_1=> {cost=>25, damage=>1, armor=>0},
            damage_2=> {cost=>50, damage=>2, armor=>0},
            damage_3=> {cost=>100, damage=>3, armor=>0},
            defense_1=> {cost=>20, damage=>0, armor=>1},
            defense_2=> {cost=>40, damage=>0, armor=>2},
            defense_3=> {cost=>80, damage=>0, armor=>3},
            noring=> {cost=>0, damage=>0, armor=>0});

my @weapons = (keys %WEAPONS);

my @armor = (keys %ARMOR);

my @left_hand = (keys %RINGS);

my @right_hand = (keys %RINGS);

my @all_battle_combinations;

cartesian {push @all_battle_combinations, \@_} [@weapons], [@armor], [@left_hand], [@right_hand];

my $cost_to_win = 1000000000000000;
my $cost_to_lose = 0;

foreach my $combination (@all_battle_combinations)
{
    my @combos = $combination;
    my %player = (hit_points=>100, damage=>($WEAPONS{$combos[0][0]}{'damage'} + $RINGS{$combos[0][2]}{'damage'} + $RINGS{$combos[0][3]}{'damage'}), armor=>($ARMOR{$combos[0][1]}{'armor'} + $RINGS{$combos[0][2]}{'armor'} + $RINGS{$combos[0][3]}{'armor'}), cost=>($WEAPONS{$combos[0][0]}{'cost'} + $ARMOR{$combos[0][1]}{'cost'} + $RINGS{$combos[0][2]}{'cost'} + $RINGS{$combos[0][3]}{'cost'}));
    my %boss = (hit_points=>100, damage=>8, armor=>2);
    my $player_wins = 0;
    my $continue_loop = 1;
    while ($continue_loop)
    {
        $boss{hit_points} = $boss{hit_points} - ($player{damage} - $boss{armor});
        if ($boss{hit_points} <= 0)
        {
            $player_wins = 1;
            $continue_loop = 0;
            last;
        }
        $player{hit_points} = $player{hit_points} - ($boss{damage} - $player{armor});
        if ($player{hit_points} <= 0)
        {
            $continue_loop = 0;
            last;
        }
    }
    if ($player_wins)
    {
        $cost_to_win = min ($cost_to_win, $player{cost});
    }
    else
    {
        $cost_to_lose = max ($cost_to_lose, $player{cost});
    }
}

say "Cost to win is $cost_to_win";
say "Cost to lose is $cost_to_lose";
