#! /usr/bin/perl

use v5.20;

open (ROOMS, "../input.txt") || die "No rooms!";

my @encrypted_rooms = <ROOMS>;

foreach my $encrypted_room (@encrypted_rooms){

    my @my_room = $encrypted_room =~ /(\w+)-/g;
    my @sector_and_checksum = $encrypted_room =~ /(\d+)\[(\w+)\]/g;
    
    say "@my_room";
    say "$my_room[0]";
}
