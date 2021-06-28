use v5.20;
use warnings;


open(REINDEERSTATS, "../input.txt") || die "Not there!!";

my @reindeer_stats = <REINDEERSTATS>;

my $furthest_distance = 0;

foreach my $reindeer (@reindeer_stats){
    my ($speed, $flying_time, $resting_time) = $reindeer =~ m/\w+ can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds./g;
    my $remaining_time = 2503;
    my $flown_distance = 0;
    while ($remaining_time > 0){
        if ($remaining_time >= $flying_time){
            $flown_distance += $speed * $flying_time;
            $remaining_time -= $flying_time;
        }
        else{
            $flown_distance += $speed * $remaining_time;
            $remaining_time = 0;
        }
        if ($remaining_time >= $resting_time){
            $remaining_time -= $resting_time;
        }
        else{
            $remaining_time = 0;
        }
    }
    if ($flown_distance > $furthest_distance){
        $furthest_distance = $flown_distance;
    }
}

say "The fatest reindeer went $furthest_distance km.";
