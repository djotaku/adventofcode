#!/usr/bin/perl

use JSON::PP;
use v5.20;
use warnings;


open(ELFJSON, "../input.txt") || die "NO ELF JSON!";

my $elf_json = decode_json <ELFJSON>;

say "Array!" if ref($elf_json) eq 'ARRAY';
say "Hash!" if ref($elf_json) eq 'HASH';
