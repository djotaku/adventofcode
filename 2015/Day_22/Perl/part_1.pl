#! /usr/bin/perl

use v5.20;
use List::Util qw/sum product min sample/;
use Switch;
use  Data::Dump qw/dump/; 


my %magic_missile = (cost=>53, damage=>4);
my %drain = (cost=>73, damage=>2, heal=>2);
my %shield = (cost=>113, armor=>7, effect_length=>6, timer=>0);
my %poison = (cost=>173, damager=>3, effect_length=>6, timer=>0);
my %recharge = (cost=>229, mana_refill=>101, effect_length=>5, timer=>0);

my @spell_list = ("shield", "drain", "recharge", "poison", "magic_missile");

my %wizard = (hit_points=>50, mana_points=>500, armor=>0);
my %boss = (hit_points=>55, damage=>8);

sub decide_spell
{
    while (1)
    {
        my $cast_this_spell = sample 1, @spell_list;
        switch($cast_this_spell)
        {
            case "shield"
            {
                if ($shield{timer} == 0 and $wizard{mana_points} >= $shield{cost})
                {
                    say "chose shield";
                    return "shield";
                }
            }
            case "drain"
            {
                if ($wizard{mana_points} >= $drain{cost})
                {
                    say "chose drain";
                    return "drain"
                }
            }
            case "recharge"
            {
                if ($wizard{mana_points} >= $recharge{cost} and $recharge{timer} == 0)
                {
                    say "chose recharge";
                    return "recharge";
                }
            }
             case "poison"
             {
                 if ($poison{timer} == 0 and $wizard{mana_points} >= $poison{cost})
                 {
                    say "chose poison";
                    return "poison";
                 }
             }
             case "magic_missile"
             {
                 if ($wizard{mana_points} >= $magic_missile{cost})
                 {
                     say "chose magic missile";
                     return "magic_missile";
                 }
             }
        }
    }
}


sub run_timer_spells
{
    say "Running Timer Spells...";
    if ($shield{timer} > 0)
    {
        say "Shield active";
        $shield{timer} -= 1;
        say "Shield timer drops to $shield{timer}";
        if ($shield{timer} == 0)
        {
            say "Shield has expired, lowering wizard armor";
            $wizard{armor} -= $shield{armor};
        }
    }
    if ($poison{timer} > 0)
    {
        say "Poison active";
        $boss{hit_points} -= $poison{damage};
        say "Poison attacks boss for $poison{damage}";
        $poison{timer} -= 1;
        say "Poison timer drops to $poison{timer}";
    }
    if ($recharge{timer} > 0)
    {
        say "Recharge active";
        $wizard{mana_points} += $recharge{mana_refill};
        say "Mana refilled by +$recharge{mana_refill}";
        $recharge{timer} -= 1;
        say "Recharge drops to $recharge{timer}";
    }
}


sub cast_spell
{
    my $spell_name = @_[0];
    say "spell name: $spell_name";
    switch($spell_name)
    {
        case "drain"
        {
            say "casting drain";
            $wizard{mana_points} -= $drain{cost};
            $wizard{hit_points} += $drain{heal};
            $boss{hit_points} -= $drain{damage};
            return $drain{cost};
        }
        case "magic_missile"
        {
            say "casting magic missile";
            $wizard{mana_points} -= $magic_missile{cost};
            $boss{hit_points} -= $magic_missile{damage};
            return $magic_missile{cost};
        }
        case "poison"
        {
            say "cast poison";
            $wizard{mana_points} -= $poison{cost};
            $poison{timer} = $poison{effect_length};
            return $poison{cost};
        }
        case "recharge"
        {
            say "cast recharge";
            $wizard{mana_points} -= $recharge{cost};
            $recharge{timer} = $recharge{effect_length};
            return $recharge{cost};
        }
        case "shield"
        {
            say "cast shield";
            $wizard{mana_points} -= $shield{cost};
            $wizard{armor} += $shield{armor};
            $shield{timer} = $shield{effect_length};
            return $shield{cost};
        }
    }
}

sub battle_sim
{
    my $mana_spent = 0;
    while (1)
    {
        #player turn
        run_timer_spells;
        if ($wizard{mana_points} <= 53 or $wizard{hit_points} <= 0)
        {
            return (0, $mana_spent);
        }
        $mana_spent += cast_spell(decide_spell);
        # boss turn
        run_timer_spells;
        if ($boss{hit_points} <= 0)
        {
            return (1, $mana_spent);
        }
        $wizard{hit_points} = $wizard{hit_points} - ($boss{damage} - $wizard{shield});
        if ($wizard{hit_points} <= 0)
        {
            return (0, $mana_spent);
        }
    }
}

my $mana_spent_to_win = 10000000000000000000;
foreach my $trial (1..1000000)
{
    say "Trial: $trial";
    # set/reset player stats
    %wizard = (hit_points=>50, mana_points=>500, armor=>0);
    %boss = (hit_points=>55, damage=>8);   
    # set/reset spell timers
    $shield{timer} = 0;
    $poison{timer} = 0;
    $recharge{timer} = 0;
    my @battle_results = battle_sim;
    dump @battle_results;
    say "Result: $battle_results[0]";
    say "Mana spent: $battle_results[1]";
    if ($battle_results[0])
    {
        say "Player won";
        $mana_spent_to_win = min ($mana_spent_to_win, $battle_results[1]);
    }
}

say "To win required $mana_spent_to_win mana points.";
