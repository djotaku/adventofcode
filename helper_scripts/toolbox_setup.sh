echo "Run me inside the toolbox: toolbox enter adventofcode"

echo "Install perl"
sudo dnf install perl -y

echo "Install CPAN Minus"
sudo cpan App:cpanminus

echo "Install The Haskell Platform"
sudo dnf install haskell-platform -y
