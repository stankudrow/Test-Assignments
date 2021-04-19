# Decomposition


0. `cd ./data` (context)

1. *./tables_structure.sql* changed according to assumptions from *Test_instructions.docx* with conversion from commercial Oracle to less commercial PostgreSQL.This post came in handy [https://habr.com/ru/post/335716/].

2. *./data_in_sql* sql scripts - COMMIT statements were left out since no transactions were started.

3. After having the files from steps 1 and 2 worked out, they are to be run via `psql -f %filepath%`. Attention! If you type in postgres `echo $HOME`, you may be surprised to find out the result as "/var/lib/postgres", so if you have an sql script inside your home directory, you might need to provide something like "/home/%YOUR_USERNAME%/...". You can also type `echo $USER` to see the difference with system ${USER} variable value.

4. The schema is built, tables are created and populated, so the tests can be done, the solutions are in _./solution.sql_ file.


__Important message__: please look through the mentioned files to read additional commentaries and compare their structure with original data (in .zip archive).
