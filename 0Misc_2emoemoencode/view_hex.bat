@echo off
rem coding: ascii
rem 2020/05/24 @HirMtsd
rem Code for 'SECCON Beginners CTF 2020'

pushd %~dp0

certutil -encodehex emoemoencode.txt hex 11 & type hex & del hex

pause
