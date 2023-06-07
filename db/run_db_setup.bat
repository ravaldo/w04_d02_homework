@echo off
psql -U postgres -d music -f db_setup.sql
pause

