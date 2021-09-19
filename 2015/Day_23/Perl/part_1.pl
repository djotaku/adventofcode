#!/usr/bin/perl

use v5.20;
use  Data::Dump qw/dump/; 

open(ASSEMBLY, "../input.txt") || die "No assembly code!!";

# setup
my @assembly = <ASSEMBLY>;
my $pointer = 0;
my $register_a = 0;
my $register_b = 0;

while ($pointer < (scalar @assembly)){

    my @current_instruction = split(' ', $assembly[$pointer]);
    if ((scalar @current_instruction) == 2)
    {
        if ($current_instruction[0] eq "hlf")
        {
            if ($current_instruction[1] eq "a")
            {
                $register_a = $register_a / 2;
            }
            else
            {
                $register_b = $register_b / 2;
            }
            $pointer += 1;
        }
        elsif ($current_instruction[0] eq "tpl")
        {
            if ($current_instruction[1] eq "a")
            {
                $register_a *= 3;
            }
            else
            {
                $register_b *= 3;
            }
            $pointer += 1;
        }
        elsif ($current_instruction[0] eq "inc")
        {
            if ($current_instruction[1] eq "a")
            {
                $register_a += 1;
            }
            else
            {
                $register_b += 1;
            }
            $pointer += 1;
        }
        elsif ($current_instruction[0] eq "jmp")
        {
            $pointer += $current_instruction[1];
        }
    }
    elsif ((scalar @current_instruction) == 3)
    {
        if ($current_instruction[0] eq "jie")
        {
            chop($current_instruction[1]);
            if ($current_instruction[1] eq "a")
            {
                if ($register_a % 2 == 0)
                {
                    $pointer += $current_instruction[2];
                }
                else
                {
                    $pointer += 1;
                }
            }
            else
            {
                if ($register_b % 2 == 0)
                {
                    $pointer += $current_instruction[2];
                }
                else
                {
                    $pointer += 1;
                }
            }
        }
        if ($current_instruction[0] eq "jio")
        {
            chop($current_instruction[1]);
            if ($current_instruction[1] eq "a")
            {
                if ($register_a == 1)
                {
                    $pointer += $current_instruction[2];
                }
                else
                {
                    $pointer += 1;
                }
            }
            else
            {
                if ($register_b == 1)
                {
                    $pointer += $current_instruction[2];
                }
                else
                {
                    $pointer += 1;
                }
            }
        }
    }

}

say "The value in register b is $register_b";
