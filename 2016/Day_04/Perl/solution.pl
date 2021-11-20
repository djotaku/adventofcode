#! /usr/bin/perl

use v5.20;

open (ROOMS, "../input.txt") || die "No rooms!";

my @encrypted_rooms = <ROOMS>;
# Debug
#my @encrypted_rooms = ("aaaaa-bbb-z-y-x-123[abxyz]", "a-b-c-d-e-f-g-h-987[abcde]", "not-a-real-room-404[oarel]", "totally-real-room-200[decoy]");
my $part_one_answer;
my $part_two_answer;

foreach my $encrypted_room (@encrypted_rooms){

    my %letter_count;
    my @my_room = $encrypted_room =~ /(\w+)-/g;
    my $room = join("", @my_room);
    my ($sector, $checksum) = $encrypted_room =~ /(\d+)\[(\w+)\]/g;
    foreach my $character (split //, $room){
        $letter_count{$character}++;
    }
    my @letters = sort {$letter_count{$b} <=> $letter_count{$a}
        or
        $a cmp $b
    } keys %letter_count;
    
    my @checksum_letters = (split //, $checksum);
    my $checksum_letters_len = @checksum_letters;
    my $truth_count = 0;
    foreach my $number (0..($checksum_letters_len-1)){
        if ($letters[$number] eq $checksum_letters[$number]){
            $truth_count++;
        }
    }
    if ($truth_count == 5){
        $part_one_answer += $sector;
        my $cipher_increment = $sector % 26;
        my $decrypted_room;
        foreach my $character (split //, $room){
            foreach my $num (1..$cipher_increment){
                if ($character eq "z"){
                    $character = "a";
                }else{
                    $character++;
                }
                #say "character in loop = $character";
            }
            #say "-----------------";
            $decrypted_room .= $character;
        }
        #say "$decrypted_room";
        if ($decrypted_room eq "northpoleobjectstorage"){
            $part_two_answer = $sector;
        }
    }
}

say "The sum of valid sector IDs is $part_one_answer.";
say "The correct room is in sector $part_two_answer.";
