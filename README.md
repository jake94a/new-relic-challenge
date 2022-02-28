### Purpose:

Read words from text files and return the 100 most common 3-word phrases.

#### My Notes

I spent around 5 hours writing this program. Functionality came first, then settings up tests. I began with `pytest` but had issues importing my `util` functions into test files. Having experience with Django built-in testing frameworks, I wrongly assumed that `pytest` would work the same or similarly.

I eventually moved on to containerizing the program and setting up scripts. I have set up this program to run via docker image and to accept CLI arguments. The scripts handle a list of inputs so that many text files are allowed, so long as they exist.

#### Description

- This program is built in Python and leverages Docker. It assumes that you have Docker installed.
- Various comments, bugs, and TODO items are documented throughout
- Time constraints resulted in poor testing (read: no testing)
- I leverage .sh scripts to use as little user input as possible, but this creates issues, noted below.

#### Issues/Improvements

- Encompassing testing
- Leveraging file paths so that the user does not have to create a `/texts/` directory
- Particular exception handling
- The current scripts depend on the user setting things up in a particular way
  - More flexibility would yield a more useful and user-friendly program
- Accept "common word count" (assumed to be 100) via CLI
- Accept "phrase length" (assumed to be 3) via CLI
- Disallow extremely large files
- Handle empty files
- Security issue of injecting whatever files you want into the container via `docker run` and/or `bin/start.sh`
  - Should only allow `.txt` and should do some checking to verify non-malicious files

#### Instructions

This is executable from the command line.

###### Directions:

1. Pull image
   1. `docker pull jake94a/jake-new-relic-word-search`
2. Create `/texts/` directory
   1. `mkdir texts/`
3. Put some .txt files into `/texts/`
   1. `cd texts`
   2. `echo "hello hello hello" >> <some_filename>.txt`
   3. Or copy a .txt file into `/texts/`
4. Two options for running this program:
   1. Single files:
      1. From `/texts/` parent directory
      2. Run `docker run -v $(pwd)/texts/a_file.txt:/texts/a_file.txt jake94a/jake-new-relic-word-search python main.py a_file.txt`
         1. This mounts your local directory to the container directory, injecting whatever files you specify
         2. This is potentially a security issue
   2. Multiple files:
      1. Copy `/bin/start.sh` from [Jake's Github](https://github.com/jake94a/new-relic-challenge)
      2. Run `./bin/start.sh <text_file.txt> <another_text.txt> ...`
      3. Add as many txt files as you desire, as long as they exist in your current `/texts/` directory
5. Tests...
   1. If testing was built into this program, I would describe it here. Probably in this way:
      1. Run `docker run --rm jake94a/jake-new-relic-word-search python -m pytest`
