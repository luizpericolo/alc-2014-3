echo on
cd C:\FILMES
ren *.txt *.cv
for /f %%f in ('dir /b c:\FILMES') do more +1 %%f > %%fs
del *.cv
pause