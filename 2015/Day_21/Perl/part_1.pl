#!/usr/bin/perl

use v5.20;                                                                                                                                                          
use  Data::Dump qw/dump/; 

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
            damage_3=> {cost=>25, damage=>3, armor=>0});

say $WEAPONS{dagger}{cost};
