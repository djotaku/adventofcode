my $PRESENTS_DELIVERED = 34000000;

my @house_array;

for my $i in (1...($PRESENTS_DELIVERED/10))
{
	for my $j in (i, ($PRESENTS_DELIVERED/10), i)
	{
		$house_array[j] += i * 10;
	}
}


